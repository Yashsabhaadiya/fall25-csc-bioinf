def gc_content(dna):
    """Calculate GC contentn percentage"""
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100 if dna else 0

def reverse_complement(dna):
    """Get reverse complement of DNA sequence"""
    comp = {'A': 'T', 'T' : A'', C'' : G'', 'G' : 'C'}
    return ''.join(comp[base] for base in reversed(dna))
