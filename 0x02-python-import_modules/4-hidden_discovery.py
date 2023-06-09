#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    arr = dir(hidden_4)
    for i in range(len(arr)):
        if (arr[i][0] != '_'):
            print(arr[i])
