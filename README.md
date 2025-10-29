# **Genomics Project**  
---
## **Description**  
This is my bioinformatics project for the "Genomcis" course. Here will be all the necessary information

## **Data**

### **Reference genome** 
Reference genome of Rhizoctonia solani was downloaded using this command on the 29 Oct from the NCBI FTP https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/906/535/GCF_016906535.1_ASM1690653v1/:  
```
wget "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/906/535/GCF_016906535.1_ASM1690653v1/GCF_016906535.1_ASM1690653v1_genomic.fna.gz"
```

Shasum GCF_016906535.1_ASM1690653v1_genomic.fna:  
_87326de160c2cdf7436eef52a591c5abc4a1c1a8_  

### **HiFi reads**  
HiFi reads were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR11560043&display=data-access on the 29 Oct 2025 using this command:  
```
prefetch SRR11560043
fasterq-dump SRR11560043
```


After command `fasterq-dump SRR11560043` we get **SRR11560043.fastq** file  
Shasum SRR11560043.fastq:  
_7d0633ac6899248839021b8eac02aaa67113764d_  


### **Nanopore reads**
Nanopore (MinION) reads were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR15096500&display=metadata on 29 Oct 2025 using command:  
```
prefetch SRR15096500
fasterq-dump SRR15096500
```

After command `fasterq-dump SRR15096500` we get **SRR15096500.fastq** file   
Shasum SRR15096500.fastq:  
_f4e79543b6a3d936150af0e368712cd2b494912b_


### **Illumina reads**
Illumina (HiSeq 2000) paired-end reads were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR11560048&display=metadata on the 29 Oct 2025 using command:  
```
prefetch SRR11560048
fasterq-dump SRR11560048
```

After command `fasterq-dump SRR11560048` we get two files: **SRR11560048_1.fastq** and  **SRR11560048_2.fastq**  
Shasum:  
400207f8cdc226f6040585bf38bd1d595a2cea36  SRR11560048_1.fastq  
a89e8f9008a3a575ab8d01ccedc519795f22bdff  SRR11560048_2.fastq  
