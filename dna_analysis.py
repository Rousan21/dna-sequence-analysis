# DNA Sequence Analysis Project

#Two sequences with minor differences

sequence1 = "ATGCGTACGCTA"
sequence2 = "ATGCGTATGCTA"


# 1. Nucleotide Counts

a_count = sequence1.count("A")
t_count = sequence1.count("T")
c_count = sequence1.count("C")
g_count = sequence1.count("G")

print("DNA Sequence 1:", sequence1)

print("\nNucleotide Counts:")
print("A:", a_count)
print("T:", t_count)
print("C:", c_count)
print("G:", g_count)


# 2. GC Content

gc_content = ((g_count + c_count) / len(sequence1)) * 100

print("\nGC Content:")
print(round(gc_content, 2), "%")


# 3. Compare DNA Sequences

print("\nDNA Sequence 2:", sequence2)
print("\nSequence Differences:")

differences = 0

for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i]:
        differences += 1

        print(
            "Position",
            i + 1,
            ":",
            sequence1[i],
            "->",
            sequence2[i]
        )


# 4. Hamming Distance

print("\nHamming Distance:", differences)


# 5. Sequence Similarity

matches = len(sequence1) - differences

similarity = (matches / len(sequence1)) * 100

print("Matching Positions:", matches)
print("Sequence Similarity:", round(similarity, 2), "%")