
#!/usr/bin/env python

import numpy as np
import pickle

def read_constants():

    with open("constant_dict.pkl","rb") as f:
        constant_dict = pickle.load(f)

    return constant_dict

def read_coeffs():

    with open("coeff_dict.pkl","rb") as f:
        coeff_dict = pickle.load(f)

    return coeff_dict

def write_constants(constant_dict):

    fname = "Magnetic_Anisotropy_Constants.txt"
    ff = open(fname,"w")

    print("{:>3s} {:>3s} {:>10s}".format("k", "q", "MA Const."),file=ff)

    for LL in list(range(2,8,2)):
        for MM in list(range(-LL,LL+1)):

            value = constant_dict.get((LL,MM)).real

            if abs(value) > 1E-4 :
                print("{:>3d} {:>+3d} {:>+10.2f}".format(LL,MM,np.round(value,2)),file=ff)

            else:
                value = 0
                print("{:>3d} {:>+3d} {:>10d}".format(LL,MM,value),file=ff)

    return

def write_coeffs(coeff_dict):

    fname = "Magnetic_Anisotropy_Coefficients.txt"
    ff = open(fname,"w")

    print("{:>3s} {:>3s} {:>10s}".format("k", "q", "MA Coeff."),file=ff)

    for LL in list(range(2,8,2)):
        for MM in list(range(-LL,LL+1)):

            value = coeff_dict.get((LL,MM)).real

            if abs(value) > 1E-4 :
                print("{:>3d} {:>+3d} {:>+10.2f}".format(LL,MM,np.round(value,2)),file=ff)

            else:
                value = 0
                print("{:>3d} {:>+3d} {:>10d}".format(LL,MM,value),file=ff)


    return


def main():

    constant_dict = read_constants()
    coeff_dict = read_coeffs()

    write_constants(constant_dict)
    write_coeffs(coeff_dict)

    return

main()
