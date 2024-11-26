#!/usr/bin/env python3
import sys

def file_count(filename):
    total_lines = 0
    total_words = 0
    total_characters = 0

    with open (filename) as f:
        for line in f:
            total_lines += 1
            total_words += len(line.split())
            total_characters += len(line)

    return (total_lines, total_words, total_characters)

def main():
    for filename in sys.argv[1:]:
        data = file_count(filename)
        print(f'{data[0]}\t{data[1]}\t{data[2]}\t{filename}')
    
    # python src/file_count.py src/test.txt

if __name__ == "__main__":
    main()