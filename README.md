# Bookbot <div align="center"> [![GitHub stars](https://img.shields.io/github/stars/heisenberg-611/bookbot?style=for-the-badge&color=gold)](https://github.com/heisenberg-611/bookbot/stargazers) [![Python](https://img.shields.io/badge/language-Python-blue?style=for-the-badge&logo=python)](https://www.python.org/) [![Repo Size](https://img.shields.io/github/repo-size/heisenberg-611/bookbot?style=for-the-badge&color=brightgreen)](https://github.com/heisenberg-611/bookbot) </div>

A simple command-line tool built with Python to analyze the contents of books. Bookbot calculates word counts and provides a detailed breakdown of character frequency, helping you gain insights into your favorite texts.

## Features
- **Word Counting**: Quickly determine the total number of words in any text file.
- **Character Analysis**: Generates a sorted report of character frequencies (case-insensitive).
- **Easy to Use**: Simple command-line interface for rapid analysis.
- **Boot.dev Project**: My first project as part of the [Boot.dev](https://www.boot.dev) curriculum.

## Tech Stack
- **Language**: Python 3
- **Modules**: `sys` (for command-line arguments)

## How to Run

1. **Prerequisites**: Ensure you have Python 3 installed.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/heisenberg-611/bookbot.git
   cd bookbot
   ```
3. **Run the Analysis**:
   Provide the path to a text file (e.g., a book in the `books/` directory) as an argument:
   ```bash
   python3 main.py books/frankenstein.txt
   ```

## Example Output
```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
i: 24613
...
============= END ===============
```