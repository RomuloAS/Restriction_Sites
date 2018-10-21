# Restriction Sites

It finds restriction sites in a DNA sequence. Restriction sites are positions where restriction enzymes cut the DNA.

It use the respective restriction enzymes PpuMI, MspA1I and MslI.

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
