#!/usr/bin/env python3
def detect_ranges(L):
    sorted_list = sorted(L)
    start = sorted_list[0]
    end = sorted_list[0]
    new_list = []

    for i in range(len(L)-1):
        if sorted_list[i] - sorted_list[i+1] == -1:
            end = sorted_list[i+1]
        else:
            if start == end:
                new_list.append(start)
            else:
                new_list.append((start, end+1))
            start = sorted_list[i+1]
            end = sorted_list[i+1]
            
    if start == end:
        new_list.append(start)
    else:
        new_list.append((start, end+1))

    return new_list

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()