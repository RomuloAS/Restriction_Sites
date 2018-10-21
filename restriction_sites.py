import argparse
import sys
import re
from tqdm import tqdm

"""
Write a Python program, that finds restriction sites in a DNA sequence.
Restriction sites are positions where restriction enzymes cut the DNA. They are usually recog-
nised by a short, specific sequence motif.
The respective sequences for the restriction enzymes PpuMI, MspA1I and MslI are defined as:

PpuMI RG^GWCCY
MspA1I CMG^CKG
MslI CAYNN^NNRTG

Note: K stands for {G, T}, M for {A, C}, N for {A, C, G, T}, R for {A, G}, W for {A, T}
and Y is short for {C, T}. The caret (^) indicates the cut site.
Given a file with DNA sequences apply regular expressions to look for all restriction sites of
these three enzymes and print the position after the cutting site to an output file (e.g. the position
of the G for PpuMI). Make sure that the names of the input and output files can be specified as
command line arguments and exactly two command line arguments have been specified.
Use the UCSC Genome Browser (https://genome.ucsc.edu/) in order to download the
DNA sequence from the human reference genome version hg38 of chromosome 22 band q13.1
(chr22 bp 37200001-40600000). The resulting file serves as the input of your program,
whereas the header line should be skipped programmatically.
Many restriction enzymes exhibit so called palindromic recognition sequences. Read up what
palindromic means in the context of DNA sequences. Which of the three enzymes listed above
exhibits such a palindromic recognition sequence (argument your choice)? What is the advant-
age of a palindromic recognition sequence?
Hint: For biologists the first base of a sequence is at position/index 1, not 0.

References:
https://docs.python.org/3.7/library/argparse.html
https://docs.python.org/3.7/library/sys.html
https://docs.python.org/3.7/library/re.html
"""

ENZYMES = {"PpuMI": {"seq":"[AG]GG[AT]CC[CT]", "cut_pos": 3},
            "MspA1I": {"seq":"C[AC]GC[GT]G", "cut_pos": 4},
            "MslI": {"seq":"CA[CT][ACGT][ACGT][ACGT][ACGT][AG]TG", "cut_pos": 6}}

def getArgs():
    """Get arguments from terminal

    This function get arguments from terminal via argparse

    Returns
    -------------
    arguments
        Returns parse_args
    """

    parser = argparse.ArgumentParser(description='It finds restriction sites in a DNA sequence.')
    parser.add_argument('infile', type=argparse.FileType('r'),
                   help='A fasta file with DNA sequences.')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'), default=sys.stdout,
                    help='Output file to save all restriction sites found (default: print on terminal)')
    
    return parser.parse_args()

def read_sequences(args):
    """Read sequences from fasta file

    This function read all dna sequences in the file to a dictionary.

    Parameters
    -------------
    args : arguments
        First argument

    Returns
    -------------
    string
        Returns sequences
    """

    try:
        fasta = args.infile.read()
    except UnicodeDecodeError:
        print("\nThe file is in an unrecognized format\n")
        return None
    fasta = list(filter(None,fasta.split(">")))
    sequences = {f.split("\n", 1)[0]: "".join(
                f.split("\n", 1)[1].split("\n")) for f in fasta}
        
    return sequences

def search_restriction_sites(sequences):
    """Search for restriction sites in the fasta file

    This function search for restriction sites in the fasta file.
    It searches for patterns recognized by restriction enzymes.


    Parameters
    -------------
    sequences : dict
        First argument

    Returns
    -------------
    list
        Returns rest_sites
    """

    rest_sites = {}   

    for key, value in tqdm(
        sequences.items(), ascii=True, desc="Searching for restriction sites"):
        for enzyme, seq_cut in ENZYMES.items():
            rest_found = re.finditer(seq_cut["seq"], value)
            for rest in rest_found:
                if(key in rest_sites):
                    if(enzyme in rest_sites[key]):
                        rest_sites[key][enzyme].append(rest.start() + seq_cut["cut_pos"])
                    else:
                        rest_sites[key][enzyme] = [rest.start() + seq_cut["cut_pos"]]
                else:
                    rest_sites[key] = {enzyme: [rest.start() + seq_cut["cut_pos"]]}

    return rest_sites

def write_file(r_sites, args):
    """Write all restriction sites found to an output file

    Write restriction sites to an output file or to the terminal according
    to the --output argument


    Parameters
    -------------
    r_sites : dict
        First argument
    args: argument
        Second argument
    """

    if len(r_sites) == 0:
        print("\nRestriction sites not found\n")
        return ""

    print("\n------------------")
    for seq_key, seq_value in r_sites.items():
        print(seq_key, file=args.outfile)
        for enz_key, enz_value in seq_value.items():
            print("\t" + enz_key, file=args.outfile, end=": ")
            print(", ".join(str(v) for v in enz_value), file=args.outfile)
        print("\n", file=args.outfile)
    print("\n------------------\n")


if __name__ == "__main__":
    args = getArgs()
    sequences = read_sequences(args)
    if sequences is not None:
        r_sites = search_restriction_sites(sequences)
    write_file(r_sites, args)