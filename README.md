# Jisho
Program that looks up a japanese word given on the command line on https://www.jisho.org.

### Required Python Modules
Requires two third party modules:

1. **requests** : A module for sending HTTP/1.1 requests using Python.

2. **beautifulsoup4** : A module for parsing HTML and XML documents.

### Using The Program

Once the modules are installed, enter the directory which contains the scripts in the terminal. The word can then be searched either by running the program then inputing the word, or the word following the program as a command line argument.

---
`python3 main.py 残響`

or

`python3 main.py` <br>
`Enter the japanese word you would like to look for: 残響`

---

When a word has been provided, the program will output the number of results for the word, the words, and each of their definitions. Following the definitions, it gives the nuber of results for the kanji, the kanji, the english meanings, the kunyomi, and the onyomi.

### Coming Soon
The ability to save these to a csv file in a format which can be exported to a software like Anki.