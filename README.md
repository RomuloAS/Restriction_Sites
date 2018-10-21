# Palindrome

Palindrome is a tool to find palindromes in a text. It searches for words, it does not search for phrases.

A palindrome is a word, phrase, number or other sequence of units that can be read the same way in either direction. E.g. the word level, the number 1234321, the phrase Step on no pets.

------

## Prerequisites

[Python 3][python]<br>
[tqdm][tqdm]

```
pip install tqdm
```

------

## Usage

```
palindrome.py [-h] [-o OUTFILE] infile
```
Positional arguments:

>`infile`              A file with a text to search for palindromes

Optional arguments:

>`-h`, `--help`           show a help message<br>
>`-o OUTFILE`, `--outfile OUTFILE`   Output file to save all palindromes found (*default:print on terminal*)

```
palindrome.py palindrome.txt -o palindromes_found.txt
```

------

[python]: https://www.python.org/
[tqdm]: https://github.com/tqdm/tqdm
