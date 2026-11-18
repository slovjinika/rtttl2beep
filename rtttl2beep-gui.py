import os
import platform
import struct
import math
import subprocess
import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from typing import Dict, Tuple

# Ініціалізація Pygame для звуку
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

IS_WINDOWS = platform.system() == "Windows"
if IS_WINDOWS:
    import winsound

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

# Словник перекладів
TRANSLATIONS = {
    'en': {
        'window_title': "RTTTL2BEEP",
        'title_label': "🎵 RTTTL2BEEP",
        'lang_label': "Language:",
        'backend_label': "Audio Engine:",
        'backend_speaker': "PC Speaker",
        'backend_pygame': "Pygame (Muted/Soft)",
        'backend_alsa': "ALSA (aplay / Pulse)",
        'frame_single': " Play a single RTTTL melody ",
        'play_melody': "▶ Play Melody",
        'save_wav': "💾 Save as WAV",
        'stop': "⏹ Stop",
        'reset_nokia': "Reset",
        'frame_editor': " Melody Constructor ",
        'dur_label': "Duration:",
        'oct_label': "Octave:",
        'btn_clear': "🗑 Clear Notes",
        'btn_backspace': "⌫ Backspace",
        'frame_folder': " Play folder with files (.txt) ",
        'browse': "📁 Browse...",
        'play_folder': "▶ Play Folder",
        'frame_log': " Event Log ",
        'ready': "Ready. Choose a melody or a folder.\n",
        'warning_playing': "Warning",
        'error': "Error",
        'empty_melody': "Melody string cannot be empty.",
        'empty_folder': "Please specify a folder path.",
        'log_loaded_nokia': "Loaded default Nokia tune.",
        'log_selected_folder': "Selected folder:",
        'log_playing_melody': "🎵 Playing melody:",
        'log_saved_wav': "💾 Melody saved to WAV:",
        'log_save_error': "[Error] Failed to save WAV:",
        'log_stopped_user': "⏹ Playback stopped by user.",
        'log_error_format': "[Error] Invalid RTTTL string format.",
        'log_playback_error': "[Error] Failed to play melody:",
        'log_playback_completed': "Playback completed.",
        'log_folder_not_valid': "[Error] Path is not a valid directory.",
        'log_no_txt_files': "No .txt files found in the directory.",
        'log_found_melodies': "Found melodies in directory:",
        'log_reading_file': "Reading file:",
        'log_empty_file': "  [Warning] File is empty. Skipping.",
        'log_error_file': "[Error] Failed to process file:",
        'log_folder_stopped': "⏹ Folder playback stopped by user.",
        'log_folder_completed': "📁 Folder playback fully completed.",
        'log_stop_requested': "Stop playback requested...",
        'log_pygame_missing': "[Error] Pygame is not installed! Run: pip install pygame",
        'lang_en': "English",
        'lang_uk': "Українська"
    },
    'uk': {
        'window_title': "RTTTL2BEEP",
        'title_label': "🎵 RTTTL2BEEP",
        'lang_label': "Мова:",
        'backend_label': "Аудіо-рушій:",
        'backend_speaker': "PC Speaker",
        'backend_pygame': "Pygame (М'який звук)",
        'backend_alsa': "ALSA (aplay / Pulse)",
        'frame_single': " Програти одну RTTTL-мелодію ",
        'play_melody': "▶ Грати мелодію",
        'save_wav': "💾 Зберегти у WAV",
        'stop': "⏹ Зупинити",
        'reset_nokia': "Скинути",
        'frame_editor': " Конструктор мелодій ",
        'dur_label': "Тривалість:",
        'oct_label': "Октава:",
        'btn_clear': "🗑 Очистити ноти",
        'btn_backspace': "⌫ Видалити ноту",
        'frame_folder': " Програти папку з файлами (.txt) ",
        'browse': "📁 Огляд...",
        'play_folder': "▶ Прослухати папку",
        'frame_log': " Журнал подій ",
        'ready': "Готово до роботи. Оберіть мелодію або папку.\n",
        'warning_playing': "Увага",
        'error': "Помилка",
        'empty_melody': "Рядок мелодії не може бути порожнім.",
        'empty_folder': "Будь ласка, вкажіть шлях до папки.",
        'log_loaded_nokia': "Завантажено стандартну мелодію Nokia.",
        'log_selected_folder': "Обрано папку:",
        'log_playing_melody': "🎵 Відтворення мелодії:",
        'log_saved_wav': "💾 Мелодію збережено у WAV:",
        'log_save_error': "[Помилка] Не вдалося зберегти WAV:",
        'log_stopped_user': "⏹ Відтворення зупинено користувачем.",
        'log_error_format': "[Помилка] Невірний формат RTTTL рядка.",
        'log_playback_error': "[Помилка] Не вдалося відтворити мелодію:",
        'log_playback_completed': "Відтворення завершено.",
        'log_folder_not_valid': "[Помилка] Шлях не є валідною директорією.",
        'log_no_txt_files': "У папці не знайдено файлів .txt.",
        'log_found_melodies': "Знайдено мелодій у папці:",
        'log_reading_file': "Читання файлу:",
        'log_empty_file': "  [Попередження] Файл порожній. Пропускаємо.",
        'log_error_file': "[Помилка] Не вдалося обробити файл:",
        'log_folder_stopped': "⏹ Відтворення папки зупинено користувачем.",
        'log_folder_completed': "📁 Відтворення папки повністю завершено.",
        'log_stop_requested': "Запит на зупинку відтворення...",
        'log_pygame_missing': "[Помилка] Бібліотеку Pygame не знайдено! Встановіть: pip install pygame",
        'lang_en': "English",
        'lang_uk': "Українська"
    }
}


class RtttlParser:
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
    def __init__(self, bpm: int, backend: str = "speaker", logger_callback=None):
        self.whole_note_duration_ms = (60000 * 4) / bpm
        self.backend = backend
        self.sample_rate = 22050
        self.logger = logger_callback
        
        if self.backend == "pygame" and PYGAME_AVAILABLE:
            try:
                if not pygame.mixer.get_init():
                    pygame.mixer.init(frequency=self.sample_rate, size=-16, channels=1, buffer=512)
            except Exception as e:
                if self.logger:
                    self.logger(f"[Error initializing pygame mixer] {e}")

    def calculate_duration(self, note: Dict) -> float:
        duration = self.whole_note_duration_ms / note['duration_denominator']
        if note['has_dot']:
            duration *= 1.5
        return duration

    def calculate_frequency(self, note: Dict) -> float:
        base_frequency = OCTAVE_4_FREQUENCIES.get(note['name'], 440.0)
        octave_shift = note['octave'] - 4
        return base_frequency * (2 ** octave_shift)

    def generate_note_samples(self, frequency: float, duration_ms: float) -> bytearray:
        """Генерує PCM семпли для однієї ноти (звук + коротка пауза після ноти)."""
        samples = bytearray()
        sound_duration_ms = duration_ms * 0.85
        silence_duration_ms = duration_ms * 0.15

        num_sound_samples = int(self.sample_rate * (sound_duration_ms / 1000.0))
        if num_sound_samples > 0:
            for i in range(num_sound_samples):
                t = i / self.sample_rate
                envelope = 1.0
                if i < 300:
                    envelope = i / 300.0
                elif i > num_sound_samples - 300:
                    envelope = (num_sound_samples - i) / 300.0
                    
                val = int(16383 * envelope * math.sin(2 * math.pi * frequency * t))
                samples.extend(struct.pack('<h', val))

        num_silence_samples = int(self.sample_rate * (silence_duration_ms / 1000.0))
        if num_silence_samples > 0:
            samples.extend(b'\x00\x00' * num_silence_samples)

        return samples

    def generate_rest_samples(self, duration_ms: float) -> bytearray:
        """Генерує PCM семпли тиші для паузи."""
        num_samples = int(self.sample_rate * (duration_ms / 1000.0))
        if num_samples > 0:
            return bytearray(b'\x00\x00' * num_samples)
        return bytearray()

    def save_to_wav(self, notes_segment: str, default_duration: int, default_octave: int, file_path: str) -> None:
        """Рендерить усю мелодію в буфер та зберігає у WAV-файл."""
        all_samples = bytearray()
        for note_token in notes_segment.split(','):
            note = RtttlParser.parse_note(note_token, default_duration, default_octave)
            if not note:
                continue
            duration_ms = self.calculate_duration(note)
            if note['name'] == 'p':
                all_samples.extend(self.generate_rest_samples(duration_ms))
            else:
                frequency = self.calculate_frequency(note)
                all_samples.extend(self.generate_note_samples(frequency, duration_ms))

        wav_header = self._create_wav_header(len(all_samples))
        with open(file_path, 'wb') as f:
            f.write(wav_header)
            f.write(all_samples)

    def play_sound(self, frequency: float, duration_ms: float, stop_event: threading.Event = None) -> None:
        sound_duration = int(duration_ms * 0.85)
        silence_duration_ms = duration_ms * 0.15
        
        try:
            num_samples = int(self.sample_rate * (sound_duration / 1000.0))
            if num_samples < 1:
                return
            
            # Генерація синусоїдального буфера з огинаючою (envelope) проти клацань
            samples = bytearray()
            for i in range(num_samples):
                t = i / self.sample_rate
                envelope = 1.0
                if i < 300:
                    envelope = i / 300.0
                elif i > num_samples - 300:
                    envelope = (num_samples - i) / 300.0
                    
                val = int(16383 * envelope * math.sin(2 * math.pi * frequency * t))
                samples.extend(struct.pack('<h', val))

            if self.backend == "pygame":
                if not PYGAME_AVAILABLE:
                    return
                sound = pygame.mixer.Sound(buffer=bytes(samples))
                sound.play()
                self._interruptible_sleep(sound_duration / 1000.0, stop_event)
                
            elif self.backend == "alsa":
                wav_data = self._create_wav_header(len(samples)) + samples
                try:
                    proc = subprocess.Popen(['aplay', '-q', '-t', 'wav'], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    proc.stdin.write(wav_data)
                    proc.stdin.close()
                    
                    slept = 0.0
                    step = 0.02
                    while slept < (sound_duration / 1000.0):
                        if stop_event and stop_event.is_set():
                            proc.terminate()
                            break
                        time.sleep(step)
                        slept += step
                    proc.wait()
                except Exception as ex:
                    if self.logger:
                        self.logger(f"[ALSA Error] {ex}")
            else:
                if IS_WINDOWS:
                    freq_int = max(37, min(32767, int(frequency)))
                    winsound.Beep(freq_int, max(1, sound_duration))
                else:
                    os.system(f"beep -f {frequency:.2f} -l {sound_duration}")
        except Exception:
            pass
        
        self._interruptible_sleep(silence_duration_ms / 1000.0, stop_event)

    def play_rest(self, duration_ms: float, stop_event: threading.Event = None) -> None:
        self._interruptible_sleep(duration_ms / 1000.0, stop_event)

    def _interruptible_sleep(self, duration_sec: float, stop_event: threading.Event = None):
        slept = 0.0
        step = 0.02
        while slept < duration_sec:
            if stop_event and stop_event.is_set():
                break
            time.sleep(step)
            slept += step

    def _create_wav_header(self, data_size: int) -> bytearray:
        header = bytearray()
        header.extend(b'RIFF')
        header.extend(struct.pack('<I', 36 + data_size))
        header.extend(b'WAVE')
        header.extend(b'fmt ')
        header.extend(struct.pack('<I', 16))
        header.extend(struct.pack('<H', 1))
        header.extend(struct.pack('<H', 1))
        header.extend(struct.pack('<I', self.sample_rate))
        header.extend(struct.pack('<I', self.sample_rate * 2))
        header.extend(struct.pack('<H', 2))
        header.extend(struct.pack('<H', 16))
        header.extend(b'data')
        header.extend(struct.pack('<I', data_size))
        return header


class RtttlApp:
    def __init__(self, root):
        self.root = root
        self.current_lang = 'en'

        self.root.title(TRANSLATIONS[self.current_lang]['window_title'])
        self.root.geometry("720x740")
        self.root.minsize(620, 620)

        self.stop_event = threading.Event()
        self.is_playing = False
        self.playing_mode = None

        self.create_widgets()

    def t(self, key: str) -> str:
        return TRANSLATIONS[self.current_lang].get(key, key)

    def create_widgets(self):
        top_bar = tk.Frame(self.root)
        top_bar.pack(fill="x", padx=15, pady=5)

        self.lang_label = tk.Label(top_bar, text=self.t('lang_label'), font=("Arial", 10))
        self.lang_label.pack(side="left")

        self.lang_var = tk.StringVar(value="English")
        self.lang_menu = tk.OptionMenu(top_bar, self.lang_var, "English", "Українська", command=self.change_language)
        self.lang_menu.config(font=("Arial", 9), cursor="hand2")
        self.lang_menu.pack(side="left", padx=5)

        self.backend_label = tk.Label(top_bar, text=self.t('backend_label'), font=("Arial", 10))
        self.backend_label.pack(side="left", padx=(15, 2))

        # Порядок: PC Speaker на першому місці, ALSA на останньому
        self.backend_var = tk.StringVar(value="PC Speaker")
        self.backend_menu = tk.OptionMenu(top_bar, self.backend_var, "PC Speaker", "Pygame (Muted/Soft)", "ALSA (aplay / Pulse)")
        self.backend_menu.config(font=("Arial", 9), cursor="hand2")
        self.backend_menu.pack(side="left", padx=5)

        self.title_label = tk.Label(self.root, text=self.t('title_label'), font=("Arial", 16, "bold"))
        self.title_label.pack(pady=5)

        # Секція: Одна мелодія
        self.melody_frame = tk.LabelFrame(self.root, text=self.t('frame_single'), font=("Arial", 11, "bold"), padx=10, pady=10)
        self.melody_frame.pack(fill="x", padx=15, pady=5)

        melody_container = tk.Frame(self.melody_frame)
        melody_container.pack(fill="x", pady=5)

        self.melody_text = tk.Text(melody_container, height=3, font=("Courier", 10), wrap="word")
        melody_scrollbar = tk.Scrollbar(melody_container, orient="vertical", command=self.melody_text.yview)
        self.melody_text.configure(yscrollcommand=melody_scrollbar.set)

        self.melody_text.pack(side="left", fill="x", expand=True)
        melody_scrollbar.pack(side="right", fill="y")

        self.melody_text.insert("1.0", DEFAULT_NOKIA_TUNE)
        self.melody_text.bind("<Control-a>", self.select_all_text)
        self.melody_text.bind("<Control-A>", self.select_all_text)

        btn_frame1 = tk.Frame(self.melody_frame)
        btn_frame1.pack(fill="x", pady=5)

        self.play_melody_btn = tk.Button(
            btn_frame1, text=self.t('play_melody'), bg="#4CAF50", fg="white", 
            activebackground="#45a049", activeforeground="white", font=("Arial", 10, "bold"), 
            cursor="hand2", command=self.start_play_melody
        )
        self.play_melody_btn.pack(side="left", padx=5)

        self.save_wav_btn = tk.Button(
            btn_frame1, text=self.t('save_wav'), bg="#2196F3", fg="white",
            activebackground="#0b7dda", activeforeground="white", font=("Arial", 10, "bold"),
            cursor="hand2", command=self.save_melody_wav
        )
        self.save_wav_btn.pack(side="left", padx=5)

        self.default_btn = tk.Button(btn_frame1, text=self.t('reset_nokia'), font=("Arial", 10), cursor="hand2", command=self.load_default_tune)
        self.default_btn.pack(side="left", padx=5)

        # Секція: Інтерактивний редактор нот (Конструктор)
        self.editor_frame = tk.LabelFrame(self.root, text=self.t('frame_editor'), font=("Arial", 11, "bold"), padx=10, pady=10)
        self.editor_frame.pack(fill="x", padx=15, pady=5)

        editor_top_row = tk.Frame(self.editor_frame)
        editor_top_row.pack(fill="x", pady=5)

        self.dur_label_widget = tk.Label(editor_top_row, text=self.t('dur_label'), font=("Arial", 9))
        self.dur_label_widget.pack(side="left", padx=(0, 2))
        
        self.dur_var = tk.StringVar(value="4")
        dur_menu = tk.OptionMenu(editor_top_row, self.dur_var, "1", "2", "4", "8", "16", "32")
        dur_menu.config(font=("Arial", 9), width=3, cursor="hand2")
        dur_menu.pack(side="left", padx=(0, 15))

        self.oct_label_widget = tk.Label(editor_top_row, text=self.t('oct_label'), font=("Arial", 9))
        self.oct_label_widget.pack(side="left", padx=(0, 2))
        
        self.oct_var = tk.StringVar(value="5")
        oct_menu = tk.OptionMenu(editor_top_row, self.oct_var, "3", "4", "5", "6", "7")
        oct_menu.config(font=("Arial", 9), width=3, cursor="hand2")
        oct_menu.pack(side="left", padx=(0, 15))

        self.btn_clear_notes = tk.Button(editor_top_row, text=self.t('btn_clear'), font=("Arial", 9), cursor="hand2", command=self.clear_melody_notes)
        self.btn_clear_notes.pack(side="right", padx=2)

        self.btn_backspace_note = tk.Button(editor_top_row, text=self.t('btn_backspace'), font=("Arial", 9), cursor="hand2", command=self.remove_last_note)
        self.btn_backspace_note.pack(side="right", padx=2)

        notes_grid = tk.Frame(self.editor_frame)
        notes_grid.pack(fill="x", pady=5)

        notes_data = [
            ("C", "c"), ("C#", "c#"), ("D", "d"), ("D#", "d#"), ("E", "e"),
            ("F", "f"), ("F#", "f#"), ("G", "g"), ("G#", "g#"), ("A", "a"),
            ("A#", "a#"), ("B", "b"), ("Pause (p)", "p")
        ]

        for index, (label, note_code) in enumerate(notes_data):
            btn = tk.Button(
                notes_grid, text=label, font=("Arial", 9, "bold"), width=7,
                bg="#f0f0f0", activebackground="#d0d0d0", cursor="hand2",
                command=lambda n=note_code: self.append_note(n)
            )
            row = index // 7
            col = index % 7
            btn.grid(row=row, column=col, padx=3, pady=3, sticky="ew")

        # Секція: Папка з мелодіями
        self.folder_frame = tk.LabelFrame(self.root, text=self.t('frame_folder'), font=("Arial", 11, "bold"), padx=10, pady=10)
        self.folder_frame.pack(fill="x", padx=15, pady=5)

        folder_sub_frame = tk.Frame(self.folder_frame)
        folder_sub_frame.pack(fill="x", pady=5)

        self.folder_var = tk.StringVar()
        self.folder_var.trace_add("write", self.on_folder_changed)

        self.folder_path_entry = tk.Entry(folder_sub_frame, textvariable=self.folder_var, font=("Arial", 10))
        self.folder_path_entry.pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.browse_btn = tk.Button(folder_sub_frame, text=self.t('browse'), font=("Arial", 10), cursor="hand2", command=self.browse_folder)
        self.browse_btn.pack(side="right")

        self.play_folder_btn = tk.Button(
            self.folder_frame, text=self.t('play_folder'), bg="#2196F3", fg="white", 
            activebackground="#0b7dda", activeforeground="white", font=("Arial", 10, "bold"), 
            cursor="hand2", command=self.start_play_folder
        )

        # Консоль логів
        self.log_frame = tk.LabelFrame(self.root, text=self.t('frame_log'), font=("Arial", 11, "bold"), padx=10, pady=10)
        self.log_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.log_text = scrolledtext.ScrolledText(self.log_frame, wrap=tk.WORD, font=("Courier", 9), bg="#1e1e1e", fg="#00ff00")
        self.log_text.pack(fill="both", expand=True)
        self.log_text.insert(tk.END, self.t('ready'))
        self.log_text.config(state="disabled")

    def select_all_text(self, event):
        event.widget.tag_add("sel", "1.0", "end-1c")
        return "break"

    def on_folder_changed(self, *args):
        folder_path = self.folder_var.get().strip()
        if folder_path and os.path.isdir(folder_path):
            if not self.play_folder_btn.winfo_ismapped() and not self.is_playing:
                self.play_folder_btn.pack(anchor="w", pady=5)
        else:
            if self.play_folder_btn.winfo_ismapped():
                self.play_folder_btn.pack_forget()

    def change_language(self, selected_lang: str):
        if selected_lang == "Українська":
            self.current_lang = 'uk'
        else:
            self.current_lang = 'en'
        self.update_ui_texts()

    def update_ui_texts(self):
        self.root.title(self.t('window_title'))
        self.lang_label.config(text=self.t('lang_label'))
        self.backend_label.config(text=self.t('backend_label'))
        self.title_label.config(text=self.t('title_label'))
        self.melody_frame.config(text=self.t('frame_single'))
        
        if not self.is_playing or self.playing_mode != 'melody':
            self.play_melody_btn.config(text=self.t('play_melody'))
        else:
            self.play_melody_btn.config(text=self.t('stop'))

        self.save_wav_btn.config(text=self.t('save_wav'))
        self.default_btn.config(text=self.t('reset_nokia'))
        
        self.editor_frame.config(text=self.t('frame_editor'))
        self.dur_label_widget.config(text=self.t('dur_label'))
        self.oct_label_widget.config(text=self.t('oct_label'))
        self.btn_clear_notes.config(text=self.t('btn_clear'))
        self.btn_backspace_note.config(text=self.t('btn_backspace'))

        self.folder_frame.config(text=self.t('frame_folder'))
        self.browse_btn.config(text=self.t('browse'))
        
        if not self.is_playing or self.playing_mode != 'folder':
            self.play_folder_btn.config(text=self.t('play_folder'))
        else:
            self.play_folder_btn.config(text=self.t('stop'))
            
        self.log_frame.config(text=self.t('frame_log'))

    def log(self, message: str):
        def _log():
            self.log_text.config(state="normal")
            self.log_text.insert(tk.END, message + "\n")
            self.log_text.see(tk.END)
            self.log_text.config(state="disabled")
        self.root.after(0, _log)

    def load_default_tune(self):
        self.melody_text.delete("1.0", "end")
        self.melody_text.insert("1.0", DEFAULT_NOKIA_TUNE)
        self.log(self.t('log_loaded_nokia'))

    def save_melody_wav(self):
        melody_str = self.melody_text.get("1.0", "end-1c").strip()
        if not melody_str:
            messagebox.showerror(self.t('error'), self.t('empty_melody'))
            return

        segments = melody_str.split(':')
        if len(segments) < 3:
            messagebox.showerror(self.t('error'), self.t('log_error_format'))
            self.log(self.t('log_error_format'))
            return

        song_name, settings_segment, notes_segment = segments[0].strip(), segments[1], segments[2]
        safe_name = "".join(c for c in song_name if c.isalnum() or c in (' ', '-', '_')).strip() or "melody"

        file_path = filedialog.asksaveasfilename(
            defaultextension=".wav",
            initialfile=f"{safe_name}.wav",
            filetypes=[("WAV audio", "*.wav"), ("All files", "*.*")]
        )
        if not file_path:
            return

        try:
            defaults = RtttlParser.parse_header(settings_segment)
            synthesizer = AudioSynthesizer(bpm=defaults['b'], backend="wav", logger_callback=self.log)
            synthesizer.save_to_wav(notes_segment, defaults['d'], defaults['o'], file_path)
            self.log(f"{self.t('log_saved_wav')} {file_path}")
        except Exception as e:
            messagebox.showerror(self.t('error'), f"{self.t('log_save_error')} {e}")
            self.log(f"{self.t('log_save_error')} {e}")

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_var.set(folder)
            self.log(f"{self.t('log_selected_folder')} {folder}")

    def append_note(self, note_name: str):
        dur = self.dur_var.get()
        octave = self.oct_var.get()
        
        if note_name == 'p':
            token = f"{dur}p"
        else:
            token = f"{dur}{note_name}{octave}"
            
        current_text = self.melody_text.get("1.0", "end-1c").strip()
        
        if ':' in current_text:
            parts = current_text.split(':')
            if len(parts) >= 3:
                notes_segment = parts[2].strip()
                if notes_segment and not notes_segment.endswith(','):
                    notes_segment += f",{token}"
                elif notes_segment:
                    notes_segment += token
                else:
                    notes_segment = token
                parts[2] = notes_segment
                new_text = ":".join(parts)
                self.melody_text.delete("1.0", "end")
                self.melody_text.insert("1.0", new_text)
            else:
                self._fallback_append(token)
        else:
            self._fallback_append(token)

    def _fallback_append(self, token: str):
        current_text = self.melody_text.get("1.0", "end-1c")
        if current_text and not current_text.endswith(',') and not current_text.endswith(':'):
            self.melody_text.insert("end", f",{token}")
        else:
            self.melody_text.insert("end", token)

    def clear_melody_notes(self):
        current_text = self.melody_text.get("1.0", "end-1c").strip()
        if ':' in current_text:
            parts = current_text.split(':')
            if len(parts) >= 3:
                parts[2] = ""
                self.melody_text.delete("1.0", "end")
                self.melody_text.insert("1.0", ":".join(parts))
        else:
            self.melody_text.delete("1.0", "end")

    def remove_last_note(self):
        current_text = self.melody_text.get("1.0", "end-1c").strip()
        if ':' in current_text:
            parts = current_text.split(':')
            if len(parts) >= 3:
                notes = [n.strip() for n in parts[2].split(',') if n.strip()]
                if notes:
                    notes.pop()
                    parts[2] = ",".join(notes)
                    self.melody_text.delete("1.0", "end")
                    self.melody_text.insert("1.0", ":".join(parts))

    def set_playing_state(self, playing: bool, mode: str = None):
        self.is_playing = playing
        self.playing_mode = mode
        
        if playing:
            if mode == 'melody':
                self.play_melody_btn.config(text=self.t('stop'), bg="#d9534f", activebackground="#c9302c", command=self.stop_playback)
                self.save_wav_btn.config(state="disabled")
                self.default_btn.config(state="disabled")
                self.backend_menu.config(state="disabled")
                if self.play_folder_btn.winfo_ismapped():
                    self.play_folder_btn.pack_forget()
            elif mode == 'folder':
                self.play_folder_btn.config(text=self.t('stop'), bg="#d9534f", activebackground="#c9302c", command=self.stop_playback)
                self.play_melody_btn.config(state="disabled")
                self.save_wav_btn.config(state="disabled")
                self.default_btn.config(state="disabled")
                self.browse_btn.config(state="disabled")
                self.backend_menu.config(state="disabled")
        else:
            self.play_melody_btn.config(text=self.t('play_melody'), bg="#4CAF50", activebackground="#45a049", command=self.start_play_melody, state="normal")
            self.save_wav_btn.config(state="normal")
            self.default_btn.config(state="normal")
            self.browse_btn.config(state="normal")
            self.backend_menu.config(state="normal")
            
            folder_path = self.folder_var.get().strip()
            self.play_folder_btn.config(text=self.t('play_folder'), bg="#2196F3", activebackground="#0b7dda", command=self.start_play_folder)
            if folder_path and os.path.isdir(folder_path):
                if not self.play_folder_btn.winfo_ismapped():
                    self.play_folder_btn.pack(anchor="w", pady=5)

    def get_selected_backend(self) -> str:
        val = self.backend_var.get()
        if "Pygame" in val:
            return "pygame"
        elif "ALSA" in val:
            return "alsa"
        else:
            return "speaker"

    def start_play_melody(self):
        if self.is_playing:
            return
        
        backend_type = self.get_selected_backend()
        if backend_type == "pygame" and not PYGAME_AVAILABLE:
            messagebox.showerror(self.t('error'), self.t('log_pygame_missing'))
            self.log(self.t('log_pygame_missing'))
            return

        melody_str = self.melody_text.get("1.0", "end-1c").strip()
        if not melody_str:
            messagebox.showerror(self.t('error'), self.t('empty_melody'))
            return

        self.stop_event.clear()
        self.set_playing_state(True, mode='melody')
        
        threading.Thread(target=self._run_melody, args=(melody_str, backend_type), daemon=True).start()

    def _run_melody(self, melody_str: str, backend_type: str):
        try:
            segments = melody_str.strip().split(':')
            if len(segments) < 3:
                self.log(self.t('log_error_format'))
                return

            song_name, settings_segment, notes_segment = segments[0], segments[1], segments[2]
            self.log(f"{self.t('log_playing_melody')} {song_name}")

            defaults = RtttlParser.parse_header(settings_segment)
            synthesizer = AudioSynthesizer(bpm=defaults['b'], backend=backend_type, logger_callback=self.log)

            for note_token in notes_segment.split(','):
                if self.stop_event.is_set():
                    self.log(self.t('log_stopped_user'))
                    break
                note = RtttlParser.parse_note(note_token, defaults['d'], defaults['o'])
                if not note:
                    continue

                duration_ms = synthesizer.calculate_duration(note)

                if note['name'] == 'p':
                    synthesizer.play_rest(duration_ms, self.stop_event)
                else:
                    frequency = synthesizer.calculate_frequency(note)
                    synthesizer.play_sound(frequency, duration_ms, self.stop_event)
        except Exception as e:
            self.log(f"{self.t('log_playback_error')} {e}")
        finally:
            self.set_playing_state(False)
            self.log(f"{self.t('log_playback_completed')}\n" + "-" * 40)

    def start_play_folder(self):
        if self.is_playing:
            return
            
        backend_type = self.get_selected_backend()
        if backend_type == "pygame" and not PYGAME_AVAILABLE:
            messagebox.showerror(self.t('error'), self.t('log_pygame_missing'))
            self.log(self.t('log_pygame_missing'))
            return

        folder_path = self.folder_var.get().strip()
        if not folder_path:
            messagebox.showerror(self.t('error'), self.t('empty_folder'))
            return

        self.stop_event.clear()
        self.set_playing_state(True, mode='folder')
        
        threading.Thread(target=self._run_folder, args=(folder_path, backend_type), daemon=True).start()

    def _run_folder(self, folder_path: str, backend_type: str):
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            self.log(self.t('log_folder_not_valid'))
            self.set_playing_state(False)
            return

        txt_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.txt')]
        if not txt_files:
            self.log(self.t('log_no_txt_files'))
            self.set_playing_state(False)
            return

        self.log(f"{self.t('log_found_melodies')} {len(txt_files)}\n")

        for file_name in sorted(txt_files):
            if self.stop_event.is_set():
                break
            file_path = os.path.join(folder_path, file_name)
            self.log(f"{self.t('log_reading_file')} {file_name}")

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    rtttl_content = f.read().strip()
                    if not rtttl_content:
                        self.log(self.t('log_empty_file'))
                        continue

                segments = rtttl_content.strip().split(':')
                if len(segments) < 3:
                    self.log(f"{self.t('log_error_format')} '{file_name}'")
                    continue

                song_name, settings_segment, notes_segment = segments[0], segments[1], segments[2]
                self.log(f"{self.t('log_playing_melody')} {song_name}")

                defaults = RtttlParser.parse_header(settings_segment)
                synthesizer = AudioSynthesizer(bpm=defaults['b'], backend=backend_type, logger_callback=self.log)

                for note_token in notes_segment.split(','):
                    if self.stop_event.is_set():
                        break
                    note = RtttlParser.parse_note(note_token, defaults['d'], defaults['o'])
                    if not note:
                        continue
                    duration_ms = synthesizer.calculate_duration(note)
                    if note['name'] == 'p':
                        synthesizer.play_rest(duration_ms, self.stop_event)
                    else:
                        frequency = synthesizer.calculate_frequency(note)
                        synthesizer.play_sound(frequency, duration_ms, self.stop_event)

                time.sleep(1.0)
            except Exception as e:
                self.log(self.t('log_error_file') + f" '{file_name}': {e}")

            self.log("-" * 40)

        if self.stop_event.is_set():
            self.log(self.t('log_folder_stopped'))
        else:
            self.log(self.t('log_folder_completed'))
        self.set_playing_state(False)

    def stop_playback(self):
        self.stop_event.set()
        self.log(self.t('log_stop_requested'))


def main():
    root = tk.Tk()
    app = RtttlApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
