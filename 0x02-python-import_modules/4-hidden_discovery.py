#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allf_them = dir()
    for i in range(10, len(allf_them)):
        if allf_them[i][:2] != "__":
            print("(:s)".format(allf_them))
