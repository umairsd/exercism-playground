codons = {
    "AUG":	"Methionine",
    "UUU":	"Phenylalanine",
    "UUC":	"Phenylalanine",
    "UUA":	"Leucine",
    "UUG":	"Leucine",
    "UCU":	"Serine",
    "UCC":	"Serine",
    "UCA":	"Serine",
    "UCG":	"Serine",
    "UAU":	"Tyrosine",
    "UAC":	"Tyrosine",
    "UGU":	"Cysteine",
    "UGC":	"Cysteine",
    "UGG":	"Tryptophan",
    "UAA":	"STOP",
    "UAG":	"STOP",
    "UGA":	"STOP",
}


def proteins(strand):
    chunks = [strand[i: i + 3] for i in range(0, len(strand), 3)]
    sequence = []

    for chunk in chunks:
        if codons[chunk] == "STOP":
            break
        sequence.append(codons[chunk])

    return sequence
