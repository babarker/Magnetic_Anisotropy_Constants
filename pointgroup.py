#!/usr/bin/env python

# Given the results from the determination of the Mag. Aniso. Constants (or Coefficients)
# we can predict what the local point group symmetry is!

# Note: This identification depends on the choice of axis;
# different non-zero sets of coefficients may be found for the icosahedral group, than listed.

def read_constants(fname):

    # Store indices of non-zero constants in a list of strings K_{kk,qq}

    ff = open(fname,"r")
    lines = ff.readlines()

    nonzeroConst = []

    for line in lines[1:]:
        li = line.strip()
        data = li.split()
        kk = int(data[0])
        qq = int(data[1])
        if data[2] != "0":
            nonzeroConst.append("K"+str(kk)+str(qq))

    return(nonzeroConst)

def groups_table(nonzeroConst):

    nzC = nonzeroConst

    MC = ["K2-2","K20","K22","K4-4","K4-2","K40","K42","K44","K6-6","K6-4","K6-2","K60","K62","K64","K66"]
    RM = ["K20","K22","K40","K42","K44","K60","K62","K64","K66"]
    Tet1 = ["K20","K4-4","K40","K44","K6-4","K60","K64"]
    Tet2 = ["K20","K40","K44","K60","K64"]
    Trig1 = ["K20","K4-3","K40","K43","K6-6","K6-3","K60","K63","K66"]
    Trig2 = ["K20","K40","K43","K60","K63","K66"]
    Hex1 = ["K20","K40","K6-6","K60","K66"]
    Hex2 = ["K20","K40","K60","K66"]
    Cub1 = ["K40","K44","K60","K62","K64","K66"]
    Cub2 = ["K40","K44","K60","K64"]
    Ico1 = ["K60","K65"]

    if len(nzC) == 27:

        group = "Triclinic: C_i or C_1"

    elif nzC == MC :

        group = "Monoclinic: C_2, C_s, or C_2h"

    elif nzC == RM :

        group = "Rhombic: C_2v, D_2, or D_2h"

    elif nzC == Tet1 :

        group = "Tetragonal: C_4, S_4, or C_4h"

    elif nzC == Tet2 :

        group = "Tetragonal: D_4, C_4v, D_2d, or D_4h"

    elif nzC ==  Trig1 :

        group = "Trigonal: C_3 or S_6"

    elif nzC == Trig2 :

        group = "Trigonal: D_3, C_3v, or D_3d"

    elif nzC == Hex1 :

        group = "Hexagonal: C_6, C_3h, or C_6h"

    elif nzC == Hex2 :

        group = "Hexagonal: D_6, C_6v, D_3h, or D_6h"

    elif nzC == Cub1 :

        group = "Cubic: T or T_h"

    elif nzC == Cub2 :

        group = "Cubic: T_d, O, or O_h"

    elif nzC == Ico1 :

        group = "Icosahedral: I_h"

    else :
      
        group = "Either your z-axis is not oriented with maximal symmetry, or you do not have a crystallographic point group (or I_h)"

    print(group)

    return

def main():

    nonzeroConst = read_constants("Magnetic_Anisotropy_Constants.txt")
    groups_table(nonzeroConst)

    return

main()
