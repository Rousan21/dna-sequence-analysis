# DNA Sequence Analysis

A small Python project that analyzes and compares two DNA sequences.

I made this project to practice Python while working with something related to biology.

## What It Does

The program:

- Counts the number of A, T, C, and G nucleotides
- Calculates GC content
- Compares two DNA sequences
- Shows where the sequences are different
- Calculates Hamming distance
- Calculates sequence similarity

## Example Input

```text
ATGCGTACGCTA
ATGCGTATGCTA
```

## Example Output

```text
DNA Sequence 1: ATGCGTACGCTA

Nucleotide Counts:
A: 3
T: 3
C: 3
G: 3

GC Content:
50.0 %

DNA Sequence 2: ATGCGTATGCTA

Sequence Differences:
Position 8 : C -> T

Hamming Distance: 1
Matching Positions: 11
Sequence Similarity: 91.67 %
```

## How It Works

The program uses basic Python string methods, loops, and conditionals.

For the nucleotide counts, it checks how many times each base appears in the first DNA sequence.

GC content is calculated by finding the percentage of the sequence made up of G and C nucleotides.

The two sequences are then compared position by position. If the nucleotides at a position are different, the program prints the position and the change.

The total number of differences is used as the Hamming distance, and the number of matching positions is used to calculate sequence similarity.

## Technologies

- Python

## What I Practiced

This project helped me practice:

- Python strings
- Loops
- Conditionals
- Indexing
- Using built-in string methods
- Basic calculations
- Comparing values between sequences
- Applying Python to biological data

## Future Ideas

I may expand this project later by adding:

- User input for DNA sequences
- DNA sequence validation
- FASTA file support
- Support for longer sequences
- Nucleotide composition visualizations
- More bioinformatics-related analysis
