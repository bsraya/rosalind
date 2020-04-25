input_file = open("../datasets/rosalind_dna.txt", "r")
dna = input_file.read()

print("%d %d %d %d" % (dna.count("A"), dna.count('C'), dna.count("G"), dna.count("T")))