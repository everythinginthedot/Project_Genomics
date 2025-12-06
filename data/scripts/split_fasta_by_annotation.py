#!/usr/bin/env python3
"""
split_fasta_by_annotation.py

Разделяет FASTA-сборку на:
1) аннотированные секвенции
2) неаннотированные секвенции

На основе списка scaffold'ов без генов.
"""

import argparse
from Bio import SeqIO


def parse_args():
    parser = argparse.ArgumentParser(
        description="Split genome FASTA into annotated and non-annotated scaffolds"
    )
    parser.add_argument(
        "-f", "--fasta",
        required=True,
        help="Genome assembly FASTA file"
    )
    parser.add_argument(
        "-l", "--list",
        required=True,
        help="Text file with scaffold IDs without genes"
    )
    parser.add_argument(
        "--annotated",
        default="annotated_scaffolds.fasta",
        help="Output FASTA with annotated scaffolds"
    )
    parser.add_argument(
        "--non_annotated",
        default="non_annotated_scaffolds.fasta",
        help="Output FASTA with non-annotated scaffolds"
    )
    return parser.parse_args()


def load_non_annotated_list(list_file):
    """Загружает список scaffold'ов без генов"""
    scaffolds = set()
    with open(list_file) as f:
        for line in f:
            scaffolds.add(line.strip())
    return scaffolds


def split_fasta(fasta_file, non_annotated_set, annotated_out, non_annotated_out):
    annotated_records = []
    non_annotated_records = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.id in non_annotated_set:
            non_annotated_records.append(record)
        else:
            annotated_records.append(record)

    SeqIO.write(annotated_records, annotated_out, "fasta")
    SeqIO.write(non_annotated_records, non_annotated_out, "fasta")

    print(f"Annotated scaffolds: {len(annotated_records)}")
    print(f"Non-annotated scaffolds: {len(non_annotated_records)}")


def main():
    args = parse_args()

    non_annotated_set = load_non_annotated_list(args.list)
    split_fasta(
        args.fasta,
        non_annotated_set,
        args.annotated,
        args.non_annotated
    )

    print("\n✅ Splitting completed:")
    print(f"Annotated FASTA: {args.annotated}")
    print(f"Non-annotated FASTA: {args.non_annotated}")


if __name__ == "__main__":
    main()