# **Genomics Project**  
---
## **Description**  
This is my bioinformatics project for the "Genomcis" course. Here will be all the necessary information

## **Data**

### **Reference genome** 
Reference genome of Rhizoctonia solani was downloaded using this command on the 29 Oct from the NCBI FTP https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/906/535/GCF_016906535.1_ASM1690653v1/:  
```wget "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/016/906/535/GCF_016906535.1_ASM1690653v1/GCF_016906535.1_ASM1690653v1_genomic.fna.gz"```

Shasum GCF_016906535.1_ASM1690653v1_genomic.fna:  
_87326de160c2cdf7436eef52a591c5abc4a1c1a8_  

### **HiFi reads**  
HiFi reads were downloaded from https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR11560043&display=data-access on the 29 Oct 2025 using this command:  
```prefetch SRR11560043
   fasterq-dump SRR11560043
```

After command *fasterq-dump SRR11560043* we get **SRR11560043.fastq** file  
Shasum SRR11560043.fastq:  
_7d0633ac6899248839021b8eac02aaa67113764d_  
