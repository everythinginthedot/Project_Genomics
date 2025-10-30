# **Genomics Project**  

---

## **Description**  

This is my bioinformatics project for the "Genomcis" course. Here will be all the necessary information

<br>

## **Data**

### **Reference genome** 

Reference genome of Rhizoctonia solani was downloaded using this command on the 29 Oct from the NCBI FTP https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/906/535/GCF_016906535.1_ASM1690653v1/:  
```
wget "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/906/535/GCF_016906535.1_ASM1690653v1/GCF_016906535.1_ASM1690653v1_genomic.fna.gz"
```

Shasum GCF_016906535.1_ASM1690653v1_genomic.fna:  
_87326de160c2cdf7436eef52a591c5abc4a1c1a8_  

<br>

### **HiFi reads**  

**NOT USED!** HiFi **SRR11560043** reads were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR11560043&display=data-access on the 29 Oct 2025 using this command:  
```
prefetch SRR11560043
fasterq-dump SRR11560043
```


After command `fasterq-dump SRR11560043` we get **SRR11560043.fastq** file  

Shasum SRR11560043.fastq:  
_7d0633ac6899248839021b8eac02aaa67113764d_  

---

New HiFi reads were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?run=SRR34390379 on the 30 Oct 2025 using this command:  
```
prefetch SRR34390379
fasterq-dump SRR34390379
```

After command `fasterq-dump SRR34390379` we get **SRR34390379.fastq** file  

Shasum SRR34390379.fastq:  
_f23b3523af9fe21aeef2066da8ba14444e2a0ea7  SRR34390379.fastq_


Reads base statistics:  
num_seqs: **862,936**  
sum_len: **12,507,209,914**  
min_len: **115**  
avg_len: **14,493.8**  
max_len: **61,784**  

<br>

### **Nanopore reads**

**NOT USED!** Nanopore (MinION) reads **SRR15096500** were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR15096500&display=metadata on 29 Oct 2025 using command:  
```
prefetch SRR15096500
fasterq-dump SRR15096500
```

After command `fasterq-dump SRR15096500` we get **SRR15096500.fastq** file   

Shasum SRR15096500.fastq:  
_f4e79543b6a3d936150af0e368712cd2b494912b_

---

New Nanopore reads **SRR19543541** (PromethION) were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?run=SRR19543541 using command:  
```
prefetch SRR19543541
fasterq-dump SRR19543541
```

After command `fasterq-dump SRR19543541` we get **SRR19543541.fastq** file

Shasum SRR19543541.fastq:  
_3700c3f7a5c89eaf92beaa79b2e9379e497271c6_  


Reads base statistics:  
num_seqs: ****  
sum_len: ****  
min_len: ****  
avg_len: ****  
max_len: ****  

<br>

### **Illumina reads**

Illumina (HiSeq 2000) paired-end reads **SRR11560048** were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR11560048&display=metadata on the 29 Oct 2025 using command:  
```
prefetch SRR11560048
fasterq-dump SRR11560048
```

After command `fasterq-dump SRR11560048` we get two files: **SRR11560048_1.fastq** and  **SRR11560048_2.fastq**  

Shasum:  
400207f8cdc226f6040585bf38bd1d595a2cea36  SRR11560048_1.fastq  
a89e8f9008a3a575ab8d01ccedc519795f22bdff  SRR11560048_2.fastq  


Reads base statistics SRR11560048_1.fastq:  
num_seqs: **27,147,396**  
sum_len: **2,714,739,600**  
min_len: **100**  
avg_len: **100**  
max_len: **100**  

Reads base statistics SRR11560048_2.fastq:  
num_seqs: **27,147,396**  
sum_len: **2,714,739,600**  
min_len: **100**  
avg_len: **100**  
max_len: **100**  
