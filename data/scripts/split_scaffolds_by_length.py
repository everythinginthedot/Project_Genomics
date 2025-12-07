#!/usr/bin/env python3

import argparse
from Bio import SeqIO

def parse_args():
    parser = argparse.ArgumentParser(
        description="Split FASTA into long and short scaffolds using TSV table and length threshold"
    )
    parser.add_argument(
        "-t", "--table",
        required=True,
        help="TSV table with scaffold statistics"
    )
    parser.add_argument(
        "-f", "--fasta",
        required=True,
        help="Genome assembly FASTA"
    )
    parser.add_argument(
        "-l", "--min_length",
        type=int,
        required=True,
        help="Minimum scaffold length to keep"
    )
    parser.add_argument(
        "-o1", "--output_long",
        required=True,
        help="Output FASTA with long scaffolds"
    )
    parser.add_argument(
        "-o2", "--output_short",
        required=True,
        help="Output FASTA with short scaffolds"
    )
    return parser.parse_args()


def load_long_scaffolds(tsv_file, min_length):
    long_scaffolds = set()

    with open(tsv_file) as f:
        header = f.readline()  # skip header
        for line in f:
            fields = line.strip().split('\t')
            scaffold = fields[0]
            length = int(fields[1])

            if length >= min_length:
                long_scaffolds.add(scaffold)

    return long_scaffolds


def split_fasta(fasta_file, long_scaffolds, out_long, out_short):
    with open(out_long, "w") as fout_long, open(out_short, "w") as fout_short:
        for record in SeqIO.parse(fasta_file, "fasta"):
            if record.id in long_scaffolds:
                SeqIO.write(record, fout_long, "fasta")
            else:
                SeqIO.write(record, fout_short, "fasta")


def main():
    args = parse_args()

    print("Loading scaffold list...")
    long_scaffolds = load_long_scaffolds(args.table, args.min_length)

    print("Splitting FASTA...")
    split_fasta(
        args.fasta,
        long_scaffolds,
        args.output_long,
        args.output_short
    )

    print("Done!")
    print(f"Long scaffolds FASTA:  {args.output_long}")
    print(f"Short scaffolds FASTA: {args.output_short}")


if __name__ == "__main__":
    main()
