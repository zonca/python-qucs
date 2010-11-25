#!/usr/bin/env python
"""
"""

TODO="""
"""

from pylab import *
from qucs import load_data 
import sys, traceback
import getopt
import pylab as pl

on = 1
off = 0


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:v", ["help", "file"])
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)
    output = None
    verbose = False
    
    global dat
    dat={}
    for o, a in opts:
        if o == "-v":
            verbose = True
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-o", "--output"):
            output = a
        if o in ("-f", "--file"):
            filename=a 
            dat=load_data(filename)

    filename=args[0]
    dat=(load_data(filename))

    from IPython.Shell import IPShellEmbed
    ipshell=IPShellEmbed()
    pl.ion()
    ipshell("Interactive Qucs Data Plotter")


if __name__ == "__main__":
    main()
