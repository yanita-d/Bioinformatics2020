old_file = open("data//sequence_1.seq", 'r').read()


reversed_sequence = ""
for symbol in old_file:
    reversed_sequence = symbol + reversed_sequence

print(reversed_sequence)

new_file=open("reverse_sequence_1.seq", 'w')
new_file.write(reversed_sequence)
new_file.close

