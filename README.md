
The purpose of this suite of python scripts is to generate
the set of Magnetic Anisotropy Constants from DFT-computed energies
in which the localized moment's spin axis is oriented at different coordinates
on the unit sphere.

The DFT computations can be brute-force SCF or force-theorem energies.
The code assumes that the list of energies
and the list of spin axis orientations are ordered in the same way.

The code further assumes the use of Lebedev quadrature for
assigning the spin axis orientations, for ease of
integration for the basis set of spherical harmonics.

The code needs numpy and scipy libraries, along with
standard libraries such as pickle, sys, subprocess, and glob.

#The relation between the Anisotropy Coefficients and the Anisotropy Constants
#is worked out in Reference

The run_program.py script first runs the following scripts, automatically
(and then deleted the intermediary pickle files):

* inread.py :
    The energy data and Lebedev Quadrature points and weights are read and stored as pickles.
    ** Note: This script asks the user to specify the names of
             the ENERGY_FILE and the LEBEDEV_QUADRATURE_FILE at the command line
* mag_ani_coeffs.py :
    The magnetic anisotropy coefficients, through rank 6,
    are determined by numerical integration of the data with spherical harmonics.
* coeffs2params.py :
    The MA coefficients are rewritten to be the intermediate parameters B_kq
* params2constants.py :
    The MA constants are determined from the intermediate parameters B_kq
* write_constants.py :
    Write out the Magnetic Anisotropy Constants as well as the Coefficients to text files

NOTE: THE USER MUST SPECIFY THE DIRECTORY OF THE SCRIPTS IN run_program.py

After generating the MA Constants and MA Coefficients text files,
you may run the following script in a directory in which those files are present:

* pointgroupconstants.py :
    The non-zero values of the constants are used to guess the local point group symmetry,
    as well as the equation.
