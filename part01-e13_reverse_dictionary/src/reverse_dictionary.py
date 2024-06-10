#!/usr/bin/env python3
def reverse_dictionary(d):
    f_e = {}
    for key, value in d.items():
        for item in value:
            if item in f_e:
                f_e[item].append(key)
            else:
                f_e[item] = [key]

    return f_e

    # return {item: [key for key, value in d.items() if item in value] for value in d.values() for item in value}

def main():
    d = {"move":["liikuttaa"], "hide":["piilottaa", "salata"]}
    print(d)
    print(reverse_dictionary(d))
    d = {"move":["liikuttaa"], "hide":["piilottaa", "salata"], "six" : ["kuusi"], "fir" : ["kuusi"]}
    print(d)
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()