#!/usr/bin/env python3
"""
check_scaffolds_without_genes.py

"""

import argparse
from Bio import SeqIO

def parse_args():
    parser = argparse.ArgumentParser(
        description="Find scaffolds in genome FASTA without annotated genes in GTF"
    )
    parser.add_argument("-f", "--fasta", required=True, help="Genome assembly FASTA file")
    parser.add_argument("-g", "--gtf", required=True, help="Genome annotation GTF file")
    parser.add_argument("-o", "--output", default="scaffolds_no_genes.txt",
                        help="Output file with scaffold names without genes")
    return parser.parse_args()

def get_scaffolds_from_fasta(fasta_file):
    """Returns all FASTA names"""
    scaffolds = set()
    for record in SeqIO.parse(fasta_file, "fasta"):
        scaffolds.add(record.id)
    return scaffolds

def get_scaffolds_with_genes(gtf_file):
    """Returns scaffolds that do have genes"""
    scaffolds_with_genes = set()
    with open(gtf_file) as f:
        for line in f:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            if len(fields) < 3:
                continue
            feature_type = fields[2]
            if feature_type.lower() == "gene":
                scaffolds_with_genes.add(fields[0])
    return scaffolds_with_genes

def main():
    args = parse_args()
    
    all_scaffolds = get_scaffolds_from_fasta(args.fasta)
    scaffolds_with_genes = get_scaffolds_with_genes(args.gtf)
    
    scaffolds_without_genes = sorted(all_scaffolds - scaffolds_with_genes)
    
    with open(args.output, 'w') as out:
        for scaffold in scaffolds_without_genes:
            out.write(scaffold + '\n')
    
    print(f"Found {len(scaffolds_without_genes)} scaffolds without genes.")
    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
