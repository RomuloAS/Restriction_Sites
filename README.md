# Restriction Sites

It finds restriction sites in a DNA sequence. Restriction sites are positions where restriction enzymes cut the DNA.

It uses the respective restriction enzymes PpuMI, MspA1I and MslI.

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
restriction_sites.py [-h] [-o OUTFILE] infile
```
Positional arguments:

>`infile`              A fasta file with DNA sequences.

Optional arguments:

>`-h`, `--help`           show a help message<br>
>`-o OUTFILE`, `--outfile OUTFILE`   Output file to save all restriction sites found (*default:print on terminal*)

```
restriction_sites.py sequences.fasta -o restriction_sites_found.txt
```

------

[python]: https://www.python.org/
[tqdm]: https://github.com/tqdm/tqdm
