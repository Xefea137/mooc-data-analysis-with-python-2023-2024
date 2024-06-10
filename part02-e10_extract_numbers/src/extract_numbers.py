#!/usr/bin/env python3
def extract_numbers(s):
    new_list = []
    words = s.split()
    for item in words:
        try:
            new_list.append(int(item))
        except ValueError:
            try:
                new_list.append(float(item))
            except:
                continue

    return new_list

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()