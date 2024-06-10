#!/usr/bin/env python3
def interleave(*lists):
    new_list = []
    #zip_list = (list(zip(*lists)))
    for item in zip(*lists):
        new_list.extend(item)
    
    return new_list

    return [item for list in zip(*lists) for item in list]

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()