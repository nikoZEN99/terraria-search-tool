# Terraria Wiki Search

A simple desktop tool built with Python and tkinter that searches the Terraria wiki — with typo auto-correction using `difflib`.

## Features

- Type an item, boss, or NPC name and it opens the matching Terraria wiki page in your browser
- Auto-corrects small typos by matching against a list of known Terraria names
- Simple, lightweight tkinter interface

## Requirements

- Python 3

No external libraries needed — uses only Python's built-in `tkinter`, `webbrowser`, and `difflib` modules.

## Setup

Make sure `terrarialist.txt` (a plain text file with one Terraria name per line) is in the same folder as the script — it's used as the reference list for typo matching.

## Usage

```bash
python terraria_wiki_search.py
```

Type a search term and click **Submit**. If it's an exact or close match to a known name, it opens that page. Otherwise, it searches the wiki with your original text.

## Author

Made by [@nikoZEN99](https://github.com/nikoZEN99)
