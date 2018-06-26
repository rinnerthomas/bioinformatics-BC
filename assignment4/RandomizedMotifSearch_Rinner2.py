from random import randint

k=8
d=5
dna=["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
t=5

bestmotifs=[]

def select_random_kmer(sequence,k): #Erstellt aus der Übergebenen Sequenz einen zufällig ausgewählten substring der Länge kmer  
    r=randint(0,(len(sequence)-k))
    rkmer=sequence[r:r+k]
    return rkmer    

def create_count_matrix(motifs):
    counta=[0]*k
    countc=[0]*k
    countg=[0]*k
    countt=[0]*k
    for j in range (0,k):#geht die ZEILE durch
        for i in range (0,t):#geht die SPALTEN runter
            letter=motifs[i]#zwischenspeichern
            if letter[j] == "A":
                counta[j]=counta[j]+1#erhöht die anzahl der As in der betrachteten Spalte um 1
            if letter[j] == "C":
                countc[j]=countc[j]+1
            if letter[j] == "G":
                countg[j]=countg[j]+1
            if letter[j]== "T":
                countt[j] = countt[j]+1
    return counta,countc,countg,countt

def calculate_nucleotide_probability(counta,countc,countg,countt):
    pseudocounta=[x+1 for x in counta]
    pseudocountc=[x+1 for x in countc]
    pseudocountg=[x+1 for x in countg]
    pseudocountt=[x+1 for x in countt]
    probabilitya=[0]*k
    probabilityc=[0]*k
    probabilityg=[0]*k
    probabilityt=[0]*k
    for j in range (0,k):#geht die ZEILE durch
          probabilitya[j]=pseudocounta[j]/(pseudocounta[j]+pseudocountc[j]+pseudocountg[j]+pseudocountt[j])
          probabilityc[j]=pseudocountc[j]/(pseudocounta[j]+pseudocountc[j]+pseudocountg[j]+pseudocountt[j])
          probabilityg[j]=pseudocountg[j]/(pseudocounta[j]+pseudocountc[j]+pseudocountg[j]+pseudocountt[j])
          probabilityt[j]=pseudocountt[j]/(pseudocounta[j]+pseudocountc[j]+pseudocountg[j]+pseudocountt[j])
    return probabilitya,probabilityc,probabilityg,probabilityt

    
def get_most_probable_kmer_for_string(probabilitya,probabilityc,probabilityg,probabilityt,text):
    most_probably_kmer = text[0:k]
    current_max_prob = 0
    for i in range (0,len(text)-k):
        current_prob = 0
        if text[i]=='A': 
            current_prob = probabilitya[0]
        if text[i]=='C': 
            current_prob = probabilityc[0]
        if text[i]=='G': 
            current_prob = probabilityg[0]
        if text[i]=='T': 
            current_prob = probabilityt[0]
        for j in range (1,k):
            if text[i+j]=='A': 
                current_prob *= probabilitya[j]
            if text[i+j]=='C': 
                current_prob *= probabilityc[j]
            if text[i+j]=='G': 
                current_prob *= probabilityg[j]
            if text[i+j]=='T': 
                current_prob *= probabilityt[j]
        if current_prob>current_max_prob: 
            current_max_prob = current_prob
            most_probably_kmer = text[i:i+k]
    return most_probably_kmer
        
    


def create_motifs_from_profile(probabilitya,probabilityc,probabilityg,probabilityt,dna): 
    pass



def randomized_motif_search(dna,k,t):
    for i in range (0,t):
        sequence=dna[i]
        bestmotifs.append(select_random_kmer(sequence,k))
    #while forever
    
    
print(randomized_motif_search(dna,k,t))
print(create_count_matrix(dna))
print(calculate_nucleotide_probability(*create_count_matrix(dna)))
print(get_most_probable_kmer_for_string(*calculate_nucleotide_probability(*create_count_matrix(dna)),"TAGTACCGAGACCGAAAGAAGTATACAGGCGT"))