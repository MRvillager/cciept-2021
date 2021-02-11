#!/bin/env python3
import sys

fin = sys.stdin

def solve():
    correct = False

    P = fin.readline().strip()
    H = fin.readline().strip()

    # WRITE YOUR SOLUTION HERE
    P_len = len(P)
    
    for i in range(0, len(H) - P_len + 1):
        check = ""
        for j in range(0, P_len):
            check += H[i+j]

        PS = "".join(sorted(P))
        checkS = "".join(sorted(check))

        if PS == checkS:
            correct = True
            break

    print("1" if correct else "0")
    
def main():
    T = int(fin.readline().strip())

    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
    