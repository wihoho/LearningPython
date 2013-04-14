def main():
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r")
    
    wordCounts = {}
    for line in infile:
        processLine(line, wordCounts)
    
    keys = wordCounts.keys()
    for key in keys:
        print(key,wordCounts.get(key))

def processLine(line, wordCounts):
    line = replacePunctuations(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, " ")
    
    return line

main()