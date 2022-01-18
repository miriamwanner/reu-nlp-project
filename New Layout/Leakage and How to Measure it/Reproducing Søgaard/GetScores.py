with open("UDify-UDPipe-Scores.txt", "rt") as f:
    lines = [l.strip().split(" ") for l in f.readlines()[1:]]

with open("UDify-Scores.tsv", "wt") as udify:
    with open("UDPipe-Scores.tsv", "wt") as udpipe:
        for line in lines:
            if "UDPipe" in line:
                treebank = "UD_" + "_".join(line[:line.index("UDPipe") - 1]) + "-" + line[line.index("UDPipe") - 1]
                noK = str(int(float(line[line.index("UDPipe") + 9].strip("k")) * 1000)) if "k" in line[line.index("UDPipe") + 9] else line[line.index("UDPipe") + 9]
                print(treebank, *line[line.index("UDPipe") + 1:line.index("UDPipe") + 9], noK, sep="\t", file=udpipe)
            else:
                treebank = "UD_" + "_".join(line[:line.index("UDify") - 1]) + "-" + line[line.index("UDify") - 1]

            noK = str(int(float(line[line.index("UDify") + 9].strip("k")) * 1000)) if "k" in line[line.index("UDify") + 9] else line[line.index("UDify") + 9]
            print(treebank, *line[line.index("UDify") + 1:line.index("UDify") + 9], noK, sep="\t", file=udify)