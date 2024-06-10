#!/usr/bin/env python3
def merge(L1, L2):
    L3 = L1 + L2
    for i in range(len(L3)):
        x = -1
        for num in L3[i:]:
            x+=1
            if L3[i] > num:
                temp = L3[i]
                L3[i] = num
                L3[x+i] = temp
    return L3

def main():
    L1 = [1,5,9,12]
    L2 = [2,6,10]
    print(merge(L1,L2))

if __name__ == "__main__":
    main()