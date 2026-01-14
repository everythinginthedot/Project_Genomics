#!/usr/bin/env python3

from Bio import SeqIO
import sys

# Проверка аргументов
if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} scaffold_list.txt assembly.fasta output.fasta")
    sys.exit(1)

scaffold_file = sys.argv[1]
assembly_file = sys.argv[2]
output_file = sys.argv[3]

# Читаем имена нужных скаффолдов в множество
with open(scaffold_file) as f:
    scaffolds_to_keep = set(line.strip() for line in f if line.strip())

# Создаём новый FASTA с выбранными скаффолдами
with open(output_file, "w") as out_f:
    for record in SeqIO.parse(assembly_file, "fasta"):
        if record.id in scaffolds_to_keep:
            SeqIO.write(record, out_f, "fasta")

print(f"Filtered FASTA created: {output_file}")
