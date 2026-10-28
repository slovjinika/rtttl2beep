import argparse
import os
import time
from typing import Dict, Tuple

# Frequencies for notes in the 4th octave (Standard Pitch + Flats mapping)
OCTAVE_4_FREQUENCIES: Dict[str, float] = {
    'c': 261.63, 'c#': 277.18, 'db': 277.18,
    'd': 293.66, 'd#': 311.13, 'eb': 311.13,
    'e': 329.63, 
    'f': 349.23, 'f#': 369.99, 'gb': 369.99,
    'g': 392.00, 'g#': 415.30, 'ab': 415.30,
    'a': 440.00, 'a#': 466.16, 'bb': 466.16,
    'b': 493.88, 'p': 0.0
}

DEFAULT_NOKIA_TUNE = "NokiaTun:d=4,o=5,b=225:8e6,8d6,f#,g#,8c#6,8b,d,e,8b,8a,c#,e,2a"


class RtttlParser:
    """Parses RTTTL format components into structured data."""
    
    @staticmethod
    def parse_header(settings_segment: str) -> Dict[str, int]:
        defaults = {'d': 4, 'o': 5, 'b': 63}
        for item in settings_segment.split(','):
            item = item.strip()
            if '=' in item:
                key, val = item.split('=')
                key = key.strip()
                val = val.strip()
                if key in defaults:
                    defaults[key] = int(val)
        return defaults

    @staticmethod
    def extract_duration_prefix(note_token: str) -> Tuple[str, str]:
        duration_digits = ""
        while note_token and note_token[0].isdigit():
            duration_digits += note_token[0]
            note_token = note_token[1:]
        return duration_digits, note_token

    @classmethod
    def parse_note(cls, note_token: str, default_duration: int, default_octave: int) -> Dict:
        note_token = note_token.strip().lower()
        
        duration_str, note_token = cls.extract_duration_prefix(note_token)
        duration = int(duration_str) if duration_str else default_duration
        
        if not note_token:
            return {}
        
        note_name = note_token[0]
        note_token = note_token[1:]
        
        if note_token and note_token[0] in ('#', 'b'):
            note_name += note_token[0]
            note_token = note_token[1:]
            
        has_dot = False
        if note_token and note_token[0] == '.':
            has_dot = True
            note_token = note_token[1:]
            
        octave = int(note_token) if note_token and note_token.isdigit() else default_octave
        
        return {
            'name': note_name,
            'duration_denominator': duration,
            'has_dot': has_dot,
            'octave': octave
        }


class AudioSynthesizer:
    """Handles the conversion of musical data into system sounds."""

    def __init__(self, bpm: int):
        self.whole_note_duration_ms = (60000 * 4) / bpm

    def calculate_duration(self, note: Dict) -> float:
        duration = self.whole_note_duration_ms / note['duration_denominator']
        if note['has_dot']:
            duration *= 1.5
        return duration

    def calculate_frequency(self, note: Dict) -> float:
        base_frequency = OCTAVE_4_FREQUENCIES.get(note['name'], 440.0)
        octave_shift = note['octave'] - 4
        return base_frequency * (2 ** octave_shift)

    def play_sound(self, frequency: float, duration_ms: float) -> None:
        sound_duration = int(duration_ms * 0.9)
        silence_duration_ms = duration_ms * 0.1
        
        os.system(f"beep -f {frequency:.2f} -l {sound_duration}")
        time.sleep(silence_duration_ms / 1000.0)

    def play_rest(self, duration_ms: float) -> None:
        time.sleep(duration_ms / 1000.0)


def play_rtttl_melody(rtttl_string: str) -> None:
    """Main orchestrator that decodes and plays an RTTTL melody string."""
    segments = rtttl_string.strip().split(':')
    if len(segments) < 3:
        raise ValueError("Invalid RTTTL string format.")

    song_name, settings_segment, notes_segment = segments[0], segments[1], segments[2]
    print(f"🎵 Playing melody: {song_name}")

    defaults = RtttlParser.parse_header(settings_segment)
    synthesizer = AudioSynthesizer(bpm=defaults['b'])

    for note_token in notes_segment.split(','):
        note = RtttlParser.parse_note(note_token, defaults['d'], defaults['o'])
        if not note:
            continue

        duration_ms = synthesizer.calculate_duration(note)

        if note['name'] == 'p':
            synthesizer.play_rest(duration_ms)
        else:
            frequency = synthesizer.calculate_frequency(note)
            synthesizer.play_sound(frequency, duration_ms)


def play_folder(folder_path: str) -> None:
    """Scans a directory for .txt files and plays them sequentially, skipping errors."""
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"[Error] Path '{folder_path}' is not a valid directory.")
        return

    txt_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.txt')]
    
    if not txt_files:
        print(f"No .txt files found in the directory '{folder_path}'.")
        return

    print(f"📁 Found melodies in directory: {len(txt_files)}\n")

    for file_name in sorted(txt_files):
        file_path = os.path.join(folder_path, file_name)
        print(f"📄 Reading file: {file_name}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                rtttl_content = f.read().strip()
                if not rtttl_content:
                    print("  [Warning] File is empty. Skipping.")
                    continue
                
                play_rtttl_melody(rtttl_content)
                time.sleep(1.0)  # Pause between tracks
                
        except Exception as e:
            print(f"  [Error] Failed to process file '{file_name}': {e}. Skipping to next...")
        
        print("-" * 40)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Play RTTTL melodies using system sounds (beep).\n\n"
            "Examples:\n"
            "  python rtttl2beep.py\n"
            '  Example: python rtttl2beep.py "NokiaTun:d=4,o=5,b=225:8e6,8d6,f#,g#,8c#6,8b,d,e,8b,8a,c#,e,2a"'
            '  Example: python rtttl2beep.py "Simpsons:d=4,o=5,b=160:32p,c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#"'
            "  python rtttl2beep.py -d /path/to/folder"
        )
    parser.add_argument(
        "-d", "--directory",
        type=str,
        help="Path to a directory containing .txt files with RTTTL strings to play sequentially."
    )
    parser.add_argument(
        "melody",
        nargs="?",
        default=None,
        help="An optional RTTTL melody string enclosed in quotes. If omitted and -d is not used, plays the default Nokia tune."
    )

    args = parser.parse_args()

    if args.directory:
        play_folder(args.directory)
    elif args.melody:
        try:
            play_rtttl_melody(args.melody)
        except Exception as e:
            print(f"[Error] Failed to play melody: {e}")
    else:
        print("Playing default Nokia tune...")
        try:
            play_rtttl_melody(DEFAULT_NOKIA_TUNE)
        except Exception as e:
            print(f"[Error] {e}")
