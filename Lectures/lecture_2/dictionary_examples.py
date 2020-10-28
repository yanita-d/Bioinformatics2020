dna_1 = set("CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC")
dna_2 = set("TTTTTTTTTTTTTTTAAAAAAAAAAAAAAAAAAUUUUUUUUUUUUUUUU")
print(dna_1)
print(dna_2)
print(dna_1.union(dna_2))

value1 = ["a", "b", "C"]
key1 = "a"

dna_test = {key1:value1, 
            "key2":"B",
            1:"v",
            2:"H"}

dna_test["key3"] = "C"
dna_test.update({"key3":"G", "key2": "GC"})
copy_dna = dna_test.copy()
copy_dna[key1] = "B"

