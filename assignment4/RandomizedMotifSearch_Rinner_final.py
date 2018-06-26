from random import randint

k=8
d=5
dna=["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
t=5

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
    motivs = [] 
    for text in dna: 
        most_probably_kmer = get_most_probable_kmer_for_string(probabilitya,probabilityc,probabilityg,probabilityt,text)
        motivs.append(most_probably_kmer)
    return motivs

def calculate_score_from_motifs(motifs):
    score=0
    counta,countc,countg,countt=create_count_matrix(motifs)
    for i in range (0,k):
        amountpopular=max(counta[i],countc[i],countg[i],countt[i])
        amountunpopular=len(motifs)-amountpopular
        score=score+amountunpopular
    return score
        
def randomized_motif_search(dna,k,t):
    bestmotifs=[]
    for i in range (0,t):
        sequence=dna[i]
        bestmotifs.append(select_random_kmer(sequence,k))
    while True:
        profile=calculate_nucleotide_probability(*create_count_matrix(bestmotifs))#profile from bestmotifs
        newmotifs=create_motifs_from_profile(*profile,dna)
        if calculate_score_from_motifs(newmotifs) >= calculate_score_from_motifs(bestmotifs):
            return bestmotifs
        else:
            bestmotifs=newmotifs
            
def multiple_randomized_motif_searches(dna,k,t):
    rmotifs=[]
    for i in range (0,999):
        rmotifs.append(randomized_motif_search(dna,k,t))
    return rmotifs
        
            
print("count matrix",create_count_matrix(dna))
print("nucleotide probability",calculate_nucleotide_probability(*create_count_matrix(dna)))
print("motifs from profile",create_motifs_from_profile(*calculate_nucleotide_probability(*create_count_matrix(dna)),dna))
print("score from motifs matrix",calculate_score_from_motifs(create_motifs_from_profile(*calculate_nucleotide_probability(*create_count_matrix(dna)),dna)))
print("randomized motif search",randomized_motif_search(dna,k,t))
print("multiple random motif searches",multiple_randomized_motif_searches(dna,k,t))
