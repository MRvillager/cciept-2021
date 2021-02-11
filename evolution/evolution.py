#!/bin/env python3

import sys

def round (N, M, fG):
    G = []
    x = 0 # column
    y = 0 # row

    for i in fG:
        G.append([])
        x = 0
        for cell in i:
            ne = 0
            G[y].append(".")

            # horizontal
            if x != 0:
                if fG[y][x-1] != ".":
                    ne += 1
            if x != (M-1):
                if fG[y][x+1] != ".":
                    ne += 1

            # diagonal
            if y != 0:
                if x != 0:
                    if fG[y-1][x-1] != ".":
                        ne += 1
                if x != (M-1):
                    if fG[y-1][x+1] != ".":
                        ne += 1
            if y != (N-1):
                if x != 0:
                    if fG[y+1][x-1] != ".":
                        ne += 1
                if x != (M-1):
                    if fG[y+1][x+1] != ".":
                        ne += 1

            # vertical
            if y != 0:
                if fG[y-1][x] != ".":
                    ne += 1
            if y != (N-1):
                if fG[y+1][x] != ".":
                    ne += 1

            
            if ne > 4:
                if cell == ".":
                    G[y][x] = "+"
                elif cell == "+":
                    G[y][x] = "*"
                elif cell == "*":
                    G[y][x] = "+"
            elif ne < 4:
                G[y][x] = "."
            else:
                G[y][x] = cell

            x += 1
        y += 1
        
    return G
            

def solve(fin):

    (N, M, K) = map(int, fin.readline().strip().split())

    fG = []
    for _ in range(N):
        fG.append(list(fin.readline().strip()))

    # WRITE HERE YOUR SOLUTION
    for _ in range(K):
        fG = round(N, M, fG)

    for r in fG:
        print("".join(r))


if __name__ == "__main__":
    solve(sys.stdin)
