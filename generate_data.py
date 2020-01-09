codon_usage_table = {
    "*": { "TAA": 0.333, "TAG": 0.334, "TGA": 0.333 },
    "A": { "GCA": 0.213, "GCC": 0.27, "GCG": 0.357, "GCT": 0.161 },
    "C": { "TGC": 0.556, "TGT": 0.444 },
    "D": { "GAC": 0.373, "GAT": 0.627 },
    "E": { "GAA": 0.689, "GAG": 0.311 },
    "F": { "TTC": 0.426, "TTT": 0.574 },
    "G": { "GGA": 0.108, "GGC": 0.404, "GGG": 0.151, "GGT": 0.337 },
    "H": { "CAC": 0.43, "CAT": 0.57 },
    "I": { "ATA": 0.072, "ATC": 0.42, "ATT": 0.508 },
    "K": { "AAA": 0.765, "AAG": 0.235 },
    "L": { "CTA": 0.037, "CTC": 0.104, "CTG": 0.497, "CTT": 0.104, "TTA": 0.131, "TTG": 0.128 },
    "M": { "ATG": 1.0 },
    "N": { "AAC": 0.55, "AAT": 0.45 },
    "P": { "CCA": 0.191, "CCC": 0.124, "CCG": 0.527, "CCT": 0.159 },
    "Q": { "CAA": 0.348, "CAG": 0.652 },
    "R": { "AGA": 0.038, "AGG": 0.022, "CGA": 0.064, "CGC": 0.399, "CGG": 0.098, "CGT": 0.379 },
    "S": { "AGC": 0.277, "AGT": 0.151, "TCA": 0.123, "TCC": 0.149, "TCG": 0.154, "TCT": 0.146 },
    "T": { "ACA": 0.131, "ACC": 0.435, "ACG": 0.268, "ACT": 0.166 },
    "U": { "TGA": 1.0 },
    "V": { "GTA": 0.155, "GTC": 0.217, "GTG": 0.369, "GTT": 0.259 },
    "W": { "TGG": 1.0 },
    "Y": { "TAC": 0.431, "TAT": 0.569 }
}

def processing_codon_usage():
    output_data = {}
    for aa in codon_usage_table:
        codon_freq_table = codon_usage_table[aa]
        for codon in codon_freq_table:
            for i in range(0, len(codon)):
                base = codon[i]
    return {
        "name": "Codon Usage", 
        "children": output_data
    }

[
        {
            "name": "A",
            "children": [
                {
                    "name": "A", 
                    "children": [
                        {
                            "name": "A", 
                            "size": 1,
                            "aa": "Ala"
                        }
{
            "name": "A",
            "children": [
                {
                    "name": "A", 
                    "children": [
                        {
                            "name": "A", 
                            "size": 1,
                            "aa": "Ala"
                        }, 
                        {
                            "name": "T", 
                            "size": 1,
                            "aa": "Ala"
                        },
                        {
                            "name": "C", 
                            "size": 1,
                            "aa": "Ala"
                        },
                        {
                            "name": "G", 
                            "size": 1,
                            "aa": "Ala"
                        }
                    ]
                }