#!/usr/bin/env python3
"""
sort_fasta_by_length.py

"""

from Bio import SeqIO
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Sort FASTA sequences by length")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
    parser.add_argument("-o", "--output", required=True, help="Output FASTA file")
    parser.add_argument("--reverse", action="store_true",
                        help="Sort from short to long instead of long to short")
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Read sequences
    records = list(SeqIO.parse(args.input, "fasta"))
    
    # Sort by length
    records.sort(key=lambda r: len(r.seq), reverse=not args.reverse)
    
    # Save to new file
    SeqIO.write(records, args.output, "fasta")
    print(f"FASTA sorted by length saved to {args.output}")

if __name__ == "__main__":
    main()