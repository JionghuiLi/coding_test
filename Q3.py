#!/usr/bin/env python3
# coding:utf-8

class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print('Empty')

    def push(self, v):
        self.stack.append(v)
        self.isEmpty()

    def pop(self):
        self.stack.pop()
        self.isEmpty()

    def inc(self, i, v):
        for n in range(i):
            self.stack[n] += v
        self.isEmpty()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.pop()
s.inc(2, 2)
s.pop()
s.pop()


