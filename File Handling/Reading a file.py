try:
    f = open('myfile.fa')
except IOError:
    print("myfile.fa does not exist")
seqs = {}
for line in f:
    # Let's discard the new line at the end (if any)
    line = line.rstrip()
    # Distinguish header from sequence
    if line[0] == '>': # or line starts with ('>')
        words = line.split()
        name = words[0][1:]
        seqs[name] = ''
    else: # sequence, not header
        seqs[name] = seqs[name] + line

f.close(f)

