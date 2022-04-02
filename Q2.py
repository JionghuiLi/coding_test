#!/usr/bin/env python3
# coding:utf-8

def match_count(team1, team2):
    lst = []
    for i in team2:
        n = 0
        for j in team1:
            if j <= i:
                n += 1
        lst.append(n)

    return lst


A = [1, 2, 3]
B = [2, 4]
print(match_count(A, B))
