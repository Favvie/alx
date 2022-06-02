#!/usr/bin/python3
import hidden_4
lists = dir(hidden_4)
for i in lists:
    if i[0] != "_":
        print(i)
