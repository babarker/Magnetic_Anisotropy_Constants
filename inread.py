#!/usr/bin/env python

import numpy as np
import sys
import pickle

# inread.py
#
# Read in data for FULL SPHERE, Lebedev Quadrature (not just irreducible portion of sphere)
# Subtract maximum of energy
# Note: Lebedev quadrature files are assumed to have data separated by commas

def read_energies(efile):

    eraw = np.loadtxt(efile)

    emax = np.amax(eraw)

    energies = [ee - emax for ee in eraw]

    return(energies)


def read_lebedev(lfile):

    lraw = np.loadtxt(lfile,delimiter=",")
    sx = [] ; sy = [] ; sz = [] ; sw = []
    sx = lraw[:,0]
    sy = lraw[:,1]
    sz = lraw[:,2]
    sw = lraw[:,3]

    return (sx,sy,sz,sw)

def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

def ask_file_names():

    efile = input("Enter the name of the file with the energy data\n")
    lfile = input("Enter the name of the file with the Lebedev Quadrature data\n")

    elines = count_lines(efile)
    llines = count_lines(lfile)

    if elines != llines:
        print("The number of lines in the files must be the same")
        sys.exit(1)

    return(efile,lfile)

def main():

    efile,lfile = ask_file_names()
    energies = read_energies(efile)
    sx,sy,sz,sw = read_lebedev(lfile)

    with open('energies.pkl', 'wb') as f:
        pickle.dump(energies, f)
    with open('sx.pkl', 'wb') as f:
        pickle.dump(sx, f)
    with open('sy.pkl', 'wb') as f:
        pickle.dump(sy, f)
    with open('sz.pkl', 'wb') as f:
        pickle.dump(sz, f)
    with open('sw.pkl', 'wb') as f:
        pickle.dump(sw, f)

    return


main()
