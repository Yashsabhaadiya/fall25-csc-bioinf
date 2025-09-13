def gc_content(dna):
    return (dna.count('G') + dna.count('C')) / len(dna) * 100

test_sequence = "ATCGATCG"
print(f"Sequence: {test_sequence}")
print(f"GC Content: {gc_content(test_sequence):.1f}%")
print("simple test completed successfully!")
