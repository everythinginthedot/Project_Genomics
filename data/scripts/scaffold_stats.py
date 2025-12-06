#!/usr/bin/env python3

import argparse
from collections import defaultdict
from Bio import SeqIO


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate scaffold statistics from FASTA + gene GTF + repeat GTF"
    )
    parser.add_argument("-f", "--fasta", required=True, help="Genome assembly FASTA")
    parser.add_argument("-g", "--genes", required=True, help="GTF with genes")
    parser.add_argument("-r", "--repeats", required=True, help="GTF with repeats")
    parser.add_argument("-o", "--output", required=True, help="Output TSV file")
    return parser.parse_args()


def load_fasta_stats(fasta_file):
    stats = {}

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq).upper()
        length = len(seq)
        gc = (seq.count("G") + seq.count("C")) / length * 100 if length > 0 else 0
        stats[record.id] = {
            "length": length,
            "gc": round(gc, 3),
            "repeat_bp": 0,
            "n_genes": 0
        }

    return stats


def load_repeats(gtf_file, stats):
    repeats = defaultdict(list)

    with open(gtf_file) as f:
        for line in f:
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            if len(fields) < 9:
                continue

            scaffold = fields[0]
            start = int(fields[3])
            end = int(fields[4])

            repeats[scaffold].append((start, end))

    for scaffold, intervals in repeats.items():
        if scaffold not in stats:
            continue

        merged = []
        for start, end in sorted(intervals):
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        repeat_bp = sum(end - start + 1 for start, end in merged)
        stats[scaffold]["repeat_bp"] = repeat_bp


def load_genes(gtf_file, stats):
    with open(gtf_file) as f:
        for line in f:
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            if len(fields) < 9:
                continue

            if fields[2] == "gene":
                scaffold = fields[0]
                if scaffold in stats:
                    stats[scaffold]["n_genes"] += 1


def write_output(stats, output_file):
    with open(output_file, "w") as out:
        out.write("scaffold\tlength\trepeat_percent\tGC_percent\tn_genes\n")

        for scaffold, data in stats.items():
            length = data["length"]
            repeat_percent = (data["repeat_bp"] / length * 100) if length > 0 else 0

            out.write(
                f"{scaffold}\t"
                f"{length}\t"
                f"{round(repeat_percent, 3)}\t"
                f"{data['gc']}\t"
                f"{data['n_genes']}\n"
            )


def main():
    args = parse_args()

    print("[1/4] Reading FASTA...")
    stats = load_fasta_stats(args.fasta)

    print("[2/4] Reading repeats GTF...")
    load_repeats(args.repeats, stats)

    print("[3/4] Reading genes GTF...")
    load_genes(args.genes, stats)

    print("[4/4] Writing output table...")
    write_output(stats, args.output)

    print(f"\n✅ Done! Output saved to: {args.output}")


if __name__ == "__main__":
    main()
