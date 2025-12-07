#!/usr/bin/env python3

import argparse
from Bio import SeqIO

def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract selected scaffolds from genome FASTA"
    )
    parser.add_argument(
        "-l", "--list",
        required=True,
        help="Text file with scaffold names (one per line)"
    )
    parser.add_argument(
        "-f", "--fasta",
        required=True,
        help="Input genome FASTA"
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output FASTA with selected scaffolds"
    )
    return parser.parse_args()


def load_scaffold_list(list_file):
    scaffolds = set()
    with open(list_file) as f:
        for line in f:
            name = line.strip()
            if name:
                scaffolds.add(name)
    return scaffolds


def extract_scaffolds(fasta_file, scaffold_set, output_file):
    kept = 0
    total = 0

    with open(output_file, "w") as out:
        for record in SeqIO.parse(fasta_file, "fasta"):
            total += 1
            if record.id in scaffold_set:
                SeqIO.write(record, out, "fasta")
                kept += 1

    print(f"Total scaffolds in input: {total}")
    print(f"Extracted scaffolds: {kept}")


def main():
    args = parse_args()
    scaffold_set = load_scaffold_list(args.list)
    extract_scaffolds(args.fasta, scaffold_set, args.output)


if __name__ == "__main__":
    main()
