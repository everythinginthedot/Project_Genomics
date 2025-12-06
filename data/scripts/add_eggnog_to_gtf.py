#!/usr/bin/env python3
"""
add_eggnog_to_gtf.py

Adds metadata from EggNOG Mapper to a GTF file.
"""

import csv
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Adds functional annotation from EggNOG to a GTF file."
    )
    parser.add_argument(
        "-g", "--gtf",
        required=True,
        help="Path to the input GTF file"
    )
    parser.add_argument(
        "-e", "--eggnog",
        required=True,
        help="Path to the EggNOG Mapper annotation file (.emapper.annotations)"
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Path to the output GTF file with added annotations"
    )
    return parser.parse_args()


def load_eggnog(eggnog_file):
    """Load EggNOG annotations into a dictionary keyed by transcript_id"""
    eggnog_dict = {}
    with open(eggnog_file, 'r') as f:
        # skip comment lines starting with ##
        for line in f:
            if line.startswith('#query'):
                header = line.lstrip('#').strip().split('\t')
                break
        
        # read remaining lines
        reader = csv.DictReader(f, fieldnames=header, delimiter='\t')
        for row in reader:
            query = row['query']
            eggnog_dict[query] = {
                'Description': row['Description'] if row['Description'] != '-' else '',
                'GOs': row['GOs'] if row['GOs'] != '-' else '',
                'KEGG_ko': row['KEGG_ko'] if row['KEGG_ko'] != '-' else '',
                'EC': row['EC'] if row['EC'] != '-' else '',
                'COG_category': row['COG_category'] if row['COG_category'] != '-' else ''
            }
    return eggnog_dict


def add_metadata_to_gtf(gtf_file, eggnog_dict, output_file):
    """Iterate over GTF and add EggNOG metadata"""
    with open(gtf_file) as fin, open(output_file, 'w') as fout:
        for line in fin:
            if line.startswith('#'):
                fout.write(line)
                continue

            fields = line.strip().split('\t')
            if len(fields) < 9:
                fout.write(line)
                continue

            attr_field = fields[8]
            
            # Extract transcript_id
            transcript_id = None
            for attr in attr_field.split(';'):
                if attr.strip().startswith('transcript_id'):
                    transcript_id = attr.split('"')[1]
                    break
            if transcript_id is None:
                fout.write(line)
                continue

            # Add annotation if available
            if transcript_id in eggnog_dict:
                meta = eggnog_dict[transcript_id]
                new_attrs = []
                if meta['Description']:
                    new_attrs.append(f'description "{meta["Description"]}"')
                if meta['GOs']:
                    new_attrs.append(f'GO "{meta["GOs"]}"')
                if meta['KEGG_ko']:
                    new_attrs.append(f'KEGG_ko "{meta["KEGG_ko"]}"')
                if meta['EC']:
                    new_attrs.append(f'EC "{meta["EC"]}"')
                if meta['COG_category']:
                    new_attrs.append(f'COG "{meta["COG_category"]}"')

                # Combine old and new attributes
                attr_field = attr_field.rstrip(';') + '; ' + '; '.join(new_attrs) + ';'
                fields[8] = attr_field

            fout.write('\t'.join(fields) + '\n')


def main():
    args = parse_args()
    eggnog_dict = load_eggnog(args.eggnog)
    add_metadata_to_gtf(args.gtf, eggnog_dict, args.output)
    print(f"New GTF with added metadata created: {args.output}")


if __name__ == "__main__":
    main()
