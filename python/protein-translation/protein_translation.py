#!/usr/bin/env python3

TRANS_TABLE = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}

def proteins(strand):
    codon_size = 3
    proteins_list = []
    codon_list = [strand[i:i+codon_size] for i in range(0, len(strand), codon_size)]
    for i in codon_list:
        if TRANS_TABLE[i] != "STOP":
            proteins_list.append(TRANS_TABLE[i])
        else:
            break
    return proteins_list
