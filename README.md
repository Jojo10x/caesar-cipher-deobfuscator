# Caesar Cipher Deobfuscator

A Python-based tool for deobfuscating data encrypted with Caesar cipher, supporting both Latin and Cyrillic character sets.

## 🚀 Features

- Dual alphabet support (Latin and Cyrillic)
- Separate encryption keys for different data types
- Automatic key detection and storage
- CSV export with timestamp
- Modular and extensible architecture

## 📋 Requirements

- Python 3.8+
- pandas
- datetime

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/caesar-cipher-deobfuscator.git
cd caesar-cipher-deobfuscator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the main script:
```bash
python main.py
```

The program will:
1. Load the sample encrypted data
2. Deobfuscate it using appropriate Caesar cipher keys
3. Save the results to a timestamped CSV file
4. Display the first few rows of the decoded data

## 📁 Project Structure

```
caesar-cipher-deobfuscator/
├── main.py
├── data_handler.py
├── decoders/
│   ├── __init__.py
│   ├── latin_decoder.py
│   └── cyrillic_decoder.py
├── requirements.txt
└── README.md
```

## 🔍 How It Works

The deobfuscator uses two different Caesar cipher decoders:
- Latin Decoder (shift = 15)
- Cyrillic Decoder (shift = 8)

Each decoder handles its respective alphabet while preserving:
- Case sensitivity
- Special characters
- Original formatting

## 📄 Output Format

The program generates a CSV file with the following columns:
- Original email
- Original address
- Encryption key for email
- Encryption key for address
- Decoded email
- Decoded address
