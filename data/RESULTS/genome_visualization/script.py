import sys
import pandas as pd
import numpy as np
from plotnine import *


def read_fasta(file_path):
    fadict = {}
    with open(file_path) as file:
        idx = ""
        for line in file:
            if line.startswith(">"):
                idx = line.strip().split()[0][1:]
                fadict[idx] = ""
            else:
                fadict[idx] += line.strip()
    return fadict


def sliding_window(seq, size, step, func):
    results = []
    for start in range(0, len(seq) - size + 1, step):
        subseq = seq[start:start + size]
        results.append([start, start + size, func(subseq)])
    return results


def gc_content(seq):
    gc_count = sum(1 for base in seq if base.lower() in ["g", "c"])
    return gc_count / len(seq)


def gc_skew(seq):
    g = seq.lower().count("g")
    c = seq.lower().count("c")
    return (g - c) / (g + c) if (g + c) > 0 else 0 


def rescale_range(x, min_x, max_x, i=0, j=1):
    return(i+((x-min_x)*(j-i)/(max_x-min_x)))


def kmer_freq(seq, k=20):
    kmer_dic = {}
    for i in range(len(seq) - k + 1):
        subseq = seq[i:i + k]
        kmer_dic[subseq] = kmer_dic.get(subseq, 0) + 1
    return kmer_dic


def kmer_pos(seq, kmer):
    pos = []
    k = len(kmer)
    start = 0
    while True:
        start = seq.find(kmer, start)
        if start == -1:
            break
        pos.append((start, start + k))
        start += 1
    return pos


def merge_overlaps(ranges):
    if not ranges:
        return []
    
    ranges = sorted(ranges)
    merged = [ranges[0]]
    
    for current in ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping intervals
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    return merged


in_fasta = "GENOME_thin.fasta"
fadict = read_fasta(in_fasta)

fadict.keys()

for key in fadict.keys():
    print(key, len(fadict[key]))

chromname = list(fadict.keys())[0]
chromname

seq = fadict[chromname]
seq_length = len(seq)
seq_length

w_size = 5000
w_step = 5000

gc = sliding_window(seq, w_size, w_step, gc_content)

gcdf = pd.DataFrame(gc, columns=["start", "stop", "gc"])
print(gcdf)


gcplot = (ggplot(gcdf, aes(x="start", y="gc")) + geom_line() + theme_minimal())
gcplot

gcdf.insert(0,"chr",chromname)
gcdf


# Definiujemy przedziały (bins) oraz odpowiadające im etykiety kolorów
bins = [0, 0.25, 0.35, float('inf')]
colors = ["fill_color=103,201,129", "fill_color=201,193,103", "fill_color=204,116,92"]

# Używamy pd.cut do zaklasyfikowania wartości w kolumnie 'gc' i przypisania odpowiednich etykiet na podstawie przedziałów
gcdf['col'] = pd.cut(gcdf['gc'], bins=bins, labels=colors, right=True)

gcdf


gcdf.to_csv("gc_content.histo", sep="\t", index=False, header=False)


skew = sliding_window(seq, w_size, w_step, gc_skew)
skewdf = pd.DataFrame(skew, columns=["start", "stop", "skew"])
skewdf

skewplot = (ggplot(skewdf, aes(x="start", y="skew")) + geom_line()) + theme_minimal()
skewplot
print('GONE')

skewdf.insert(0,"chr",chromname)
skewdf

skewdf["col"] = "fill_color=blue"
skewdf.loc[skewdf["skew"]>0, "col"] = "fill_color=red"
skewdf

skewdf.to_csv("gc_skew.histo", sep="\t", index=False, header=False)

skew_cuml = []
cumul = 0

# Dla każdego okna dodajemy skew poprzedniego okna
for idx in range(skewdf.shape[0]):
    cumul += skewdf.iloc[idx,]["skew"]
    skew_cuml.append(cumul)
    
skew_cuml = np.array(skew_cuml)