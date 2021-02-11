#!/bin/env python3

import sys

fin = sys.stdin
fout = sys.stdout

def solve(N, K, V):
    V.sort()

    maxV = V[-K-1:]
    return sum(maxV)
    

def main():

    (N, K) = map(int, fin.readline().strip().split())
    V = list(map(int, input().strip().split()))

    # WRITE YOUR SOLUTION HERE
    solution = solve(N, K, V)
    
    print(solution)


if __name__ == "__main__":
    main()
