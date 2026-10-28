# 🎵 RTTTL Player for Linux/System Sound

A Python-based command-line tool that parses and plays **RTTTL (Ring Tone Text Transfer Language)** melodies using system speaker sounds (`beep`). 

It supports playing a default tune, executing custom RTTTL strings directly from the command line, or batch-playing all `.txt` melody files stored in a directory.

## 🚀 Features

* **RTTTL Parser:** Full support for note durations, octaves, accidentals (`#`, `b`), dotted notes, and rests (`p`).
* **Batch Folder Playback:** Automatically scans a folder for `.txt` files containing RTTTL strings and plays them sequentially.
* **Error Resilience:** Gracefully handles malformed or empty files during batch playback, skipping them and continuing to the next tune.
* **Standard CLI:** Uses Python's built-in `argparse` with standard options (`-d`, `--directory`) and a built-in help menu (`--help`).

---

## 📋 Requirements

* **Python 3.x**
* **Linux `beep` utility:** The script uses the system `beep` command to drive the PC speaker.
  ```bash
  sudo apt install beep```

*(Ensure your user has permission to access the PC speaker or run with appropriate privileges if needed).

---

## 🛠️ Installation

1. Clone the repository or download the script:
```bash
git clone https://github.com/slovjinika/rtttl2beep
cd rtttl-player

```


2. Make sure the script is executable (optional):
```bash
chmod +x script.py

```



---

## 📖 Usage

Run the script from your terminal using different options depending on what you want to play:

### 1. View Help Instructions

```bash
python script.py --help

```

### 2. Play the Default Tune (Nokia Tune)

If no arguments are provided, the script plays the classic Nokia tune by default.

```bash
python script.py

```

### 3. Play a Custom RTTTL String

Pass your RTTTL string directly in quotes as an argument:

```bash
python script.py "Simpsons:d=4,o=5,b=160:32p,c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#"

```

### 4. Play All Melodies from a Folder

Specify a directory containing `.txt` files with RTTTL content using the `-d` or `--directory` flag:

```bash
python script.py -d /path/to/your/rtttl_folder/

```

*The script will sort the files alphabetically, play them one by one with a 1-second pause in between, and skip any invalid/empty files without crashing.*

---

## 📝 Example `.txt` File Format

Inside your target directory, create `.txt` files containing standard RTTTL strings. For example, `zelda.txt`:

```text
ZeldaTheme:d=4,o=5,b=125:8a#5,16f5,8a#5,16a#5,16c6,16d6,16e6,8f6,8f6,8a#5,16f5,8a#5,16a#5,16c6,16d6,16e6,8f6,8f6,8g6,16f6,8d#6,16d6,8c6,16a#5,2a#5

```

---

## 📜 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).




