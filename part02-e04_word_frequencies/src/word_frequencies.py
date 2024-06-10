#!/usr/bin/env python3
def word_frequencies(filename):
    words = {}
    with open(filename) as f:
        for line in f:
            for word in line.split():
                x = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if x in words:
                    words[x] += 1
                else:
                    words[x] = 1

    return words

def main():
    x = word_frequencies("src\\alice.txt")
    for key, value in x.items():
        print(f'{key}\t{value}')

if __name__ == "__main__":
    main()