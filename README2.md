# 🧬 **Genomics Project**

Bioinformatics project for the "Genomics" course.  
This repository contains all datasets, commands, and analyses used in the project.

---

## 📖 **Description**

This project focuses on genome assembly and quality assessment of *Rhizoctonia solani* using multiple sequencing technologies (HiFi, Nanopore, and Illumina).

---

## 🧫 **Data**

### 🧬 **Reference genome**

Reference genome of *Rhizoctonia solani* was downloaded using this command on the 29 Oct from the NCBI FTP:  
```
wget "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/906/535/GCF_016906535.1_ASM1690653v1/GCF_016906535.1_ASM1690653v1_genomic.fna.gz"
```

Shasum `GCF_016906535.1_ASM1690653v1_genomic.fna`:  
`87326de160c2cdf7436eef52a591c5abc4a1c1a8`

---

### 🧬 **HiFi reads**

**NOT USED!** HiFi **SRR11560043** reads were downloaded from [NCBI Trace Archive](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR11560043&display=data-access) on the 29 Oct 2025 using:
```
prefetch SRR11560043
fasterq-dump SRR11560043
```

Resulting file: `SRR11560043.fastq`  
Shasum: `7d0633ac6899248839021b8eac02aaa67113764d`

---

New HiFi reads were downloaded from [SRR34390379](https://trace.ncbi.nlm.nih.gov/Traces/?run=SRR34390379) on the 30 Oct 2025:
```
prefetch SRR34390379
fasterq-dump SRR34390379
```

Resulting file: `SRR34390379.fastq`  
Shasum: `f23b3523af9fe21aeef2066da8ba14444e2a0ea7`

**Reads base statistics:**  
- num_seqs: 862,936  
- sum_len: 12,507,209,914  
- min_len: 115  
- avg_len: 14,493.8  
- max_len: 61,784  

---

### 🧬 **Nanopore reads**

**NOT USED!** Nanopore (MinION) reads **SRR15096500** were downloaded from [SRR15096500 metadata](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR15096500&display=metadata) on 29 Oct 2025:
```
prefetch SRR15096500
fasterq-dump SRR15096500
```

Resulting file: `SRR15096500.fastq`  
Shasum: `f4e79543b6a3d936150af0e368712cd2b494912b`

---

New Nanopore reads **SRR19543541** (PromethION) were downloaded from [SRR19543541](https://trace.ncbi.nlm.nih.gov/Traces/?run=SRR19543541):
```
prefetch SRR19543541
fasterq-dump SRR19543541
```

Resulting file: `SRR19543541.fastq`  
Shasum: `3700c3f7a5c89eaf92beaa79b2e9379e497271c6`

---

New Nanopore reads **SRR17331923** (GridION) were downloaded from [SRR17331923 metadata](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR17331923&display=metadata):
```
prefetch SRR17331923
fasterq-dump SRR17331923
```

Resulting file: `SRR17331923.fastq`  
Shasum: `c661512388e38debe5a84347e48f3b9e00c702ae`

---

### 🧬 **Illumina reads**

Illumina (HiSeq 2000) paired-end reads **SRR11560048** were downloaded from [SRR11560048 metadata](https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR11560048&display=metadata) on 29 Oct 2025:
```
prefetch SRR11560048
fasterq-dump SRR11560048
```

Resulting files:  
`SRR11560048_1.fastq`  
`SRR11560048_2.fastq`

Shasum:  
- `400207f8cdc226f6040585bf38bd1d595a2cea36  SRR11560048_1.fastq`  
- `a89e8f9008a3a575ab8d01ccedc519795f22bdff  SRR11560048_2.fastq`

**Reads base statistics:**  
SRR11560048_1.fastq:  
- num_seqs: 27,147,396  
- sum_len: 2,714,739,600  
- avg_len: 100  

SRR11560048_2.fastq:  
- num_seqs: 27,147,396  
- sum_len: 2,714,739,600  
- avg_len: 100  

---

## 🧪 **Quality control**

### **HiFi reads**

#### **FastQC**
```
fastqc SRR11560043.fastq
```
Results of quality control were fine.

---

### **Nanopore**

#### **Preliminary QC**
```
NanoPlot --fastq SRR[number].fastq -o SRR[number]_nanoplot
```

#### **Adapter trimming**
```
porechop -i SRR[number].fastq -o SRR[number]_trimmed.fastq
```

**SRR17331923.fastq**  
- 322,194 / 332,671 reads had adapters trimmed from start (22,130,418 bp removed)  
- 187,323 / 332,671 reads had adapters trimmed from end (8,262,121 bp removed)  
- 1,287 / 332,671 reads were split  

**SRR15096500.fastq**  
- 2,274,209 / 2,311,521 reads had adapters trimmed from start (154,862,480 bp removed)  
- 1,530,260 / 2,311,521 reads had adapters trimmed from end (76,219,041 bp removed)  
- 4,102 / 2,311,521 reads were split  

#### **Reads filtering**
```
filtlong --min_length 1000 --keep_percent 90 SRR[number]_trimmed.fq > SRR[number]_clean.fastq
```

---

## 🧬 **Assembly**

### **SPAdes**

Assembly with Illumina paired-end reads:
```
spades.py -1 reads/Illumina/SRR11560048_1.fastq -2 reads/Illumina/SRR11560048_2.fastq -o spades_illumina_SRR11560048_pe --isolate
```

Assembly stats (`assembly-stats spades_illumina_SRR11560048_pe/contigs.fasta`):  
```
sum = 65398275, n = 292113, ave = 223.88, largest = 33176
N50 = 573
```

Assembly stats (`assembly-stats spades_illumina_SRR11560048_pe/scaffolds.fasta`):  
```
sum = 65623110, n = 289852, ave = 226.40, largest = 50535
N50 = 581
```

---

### **SMARTdenovo**

#### **Nanopore reads**
```
smartdenovo.pl -p SMARTdenovo_nanopore_SRR17331923 -t 8 -c 1 reads/Nanopore/SRR17331923_clean.fastq > SMARTdenovo_nanopore_SRR17331923.mak
time make -f SMARTdenovo_nanopore_SRR17331923.mak
```

#### **HiFi reads**
```
smartdenovo.pl -p SMARTdenovo_HIFI_SRR11560043 -t 8 -c 1 reads/HIFI/SRR11560043.fastq > SMARTdenovo_HIFI_SRR11560043.mak
time make -f SMARTdenovo_HIFI_SRR11560043.mak
```
