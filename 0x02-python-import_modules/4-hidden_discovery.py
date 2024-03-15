#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allp = dir()
    for i in range(10, len(allp)):
        if allp[i][:2] != "__":
            print("{:s}".format(allp[i]))
