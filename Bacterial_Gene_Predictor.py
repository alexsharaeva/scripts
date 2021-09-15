#!/usr/bin/env python
# coding: utf-8

# Task:
# 1) stop_c after start_c
# 2) len(seq) % 3 == 0 => (stop_c - start_c) % 3 == 0
# 3) lenght threshold = 10AA => 30n
# 4) save all ORF in the case of nested ORF
# 5) find Promoter before start + Terminator after stop

# Открыть FASTA файл и привести его в рабочий вид:

# In[ ]:


with open('/home/gunter/ecoli_10k.fasta') as f:
    first_line = f.readline()
    lines = f.read().split('\n')
lines = ''.join(lines)


# Разбить одну строку на кодоны со сдвигом на 1 нуклеотид:

# In[ ]:


def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers


# Старт и стоп кодоны:

# In[ ]:


start = 'ATG'
stop = ['TAG', 'TGA', 'TAA']


# Нумеровка всех триплетов:

# In[ ]:


all_kmers_1 = build_kmers(lines,3)

ind_dict = {'start': [], 'stop': []}

i = 0
for kmer in all_kmers_1:
    if kmer == start:
        ind_dict['start'].append(i)
    if kmer in stop:
        ind_dict['stop'].append(i)
    i += 1


# Подбор генов, исключая вложенные:

# In[ ]:


starts = ind_dict['start']
stops = ind_dict['stop']

locations = []
last_stop = 0
for start in starts:
    if start <= last_stop:
        continue
    for stop in stops:
        if stop < start:
            continue
        if (stop - start) % 3 != 0:
            continue
        locations.append((start, stop))
        last_stop = stop + 2
        break
locations


# Запись координат кодонов, обозначающих местоположение гена, и самой последовательности в текстовый файл:

# In[ ]:


with open('out.fasta', mode='w') as f:

    for i, (start, stop) in enumerate(locations):
        print(f'>gene{i}_{start+1}_{stop+3}\n', lines[start:stop], file=f)

