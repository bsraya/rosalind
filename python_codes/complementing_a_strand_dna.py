input_file = open("../datasets/rosalind_revc.txt", "r")
dna = input_file.read()

complement = {'A': 'T', 'T': 'A', "C":"G", "G":"C"}

print(''.join([complement[acid] for acid in dna[::-1]]))