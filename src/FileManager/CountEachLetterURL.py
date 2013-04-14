import urllib.request

def main():
    url = input("Enter a url for a file: ").strip()
    infile = urllib.request.urlopen(url)
    #The data read from the URL is a raw data in bytes
    #Invoking the decode() method converts the raw data to a string
    s = infile.read().decode()
    
    counts = countLetters(s.lower())
    
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a')+i)+" appears "+str(counts[i])+(" time" if counts[i] == 1 else " times"))

def countLetters(s):
    counts = 26 * [0]
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts
    
main()