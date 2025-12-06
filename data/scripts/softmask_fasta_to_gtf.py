#!/usr/bin/env python3
"""
softmask_fasta_to_gtf.py

Converts soft-masked regions (lowercase) in a FASTA genome
into a GTF annotation of repeats.
"""

import argparse
from Bio import SeqIO


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert soft-masked FASTA (lowercase) to GTF repeat annotations"
    )
    parser.add_argument(
        "-f", "--fasta",
        required=True,
        help="Soft-masked genome FASTA file"
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output GTF file with repeat annotations"
    )
    parser.add_argument(
        "--source",
        default="RepeatMasker_soft",
        help="Source field for GTF (default: RepeatMasker_soft)"
    )
    parser.add_argument(
        "--feature",
        default="repeat_region",
        help="Feature type for GTF (default: repeat_region)"
    )
    return parser.parse_args()


def extract_softmasked_regions(seq):
    """
    Finds continuous lowercase regions in a sequence.
    Returns list of (start, end) in 1-based GTF coordinates.
    """
    regions = []
    in_repeat = False
    start = None

    for i, base in enumerate(seq, start=1):
        if base.islower():
            if not in_repeat:
                in_repeat = True
                start = i
        else:
            if in_repeat:
                regions.append((start, i - 1))
                in_repeat = False

    if in_repeat:
        regions.append((start, len(seq)))

    return regions


def fasta_to_gtf(fasta_file, gtf_out, source, feature):
    repeat_id = 1

    with open(gtf_out, "w") as fout:
        for record in SeqIO.parse(fasta_file, "fasta"):
            seq_id = record.id
            seq = str(record.seq)

            regions = extract_softmasked_regions(seq)

            for start, end in regions:
                attributes = f'repeat_id "repeat_{repeat_id}"'

                gtf_line = (
                    f"{seq_id}\t"
                    f"{source}\t"
                    f"{feature}\t"
                    f"{start}\t"
                    f"{end}\t"
                    f".\t"
                    f"+\t"
                    f".\t"
                    f"{attributes};\n"
                )

                fout.write(gtf_line)
                repeat_id += 1

    print(f"✅ GTF file created: {gtf_out}")
    print(f"✅ Total repeat regions annotated: {repeat_id - 1}")


def main():
    args = parse_args()

    fasta_to_gtf(
        fasta_file=args.fasta,
        gtf_out=args.output,
        source=args.source,
        feature=args.feature
    )


if __name__ == "__main__":
    main()
