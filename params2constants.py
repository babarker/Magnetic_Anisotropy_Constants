#!/usr/bin/env python

import numpy as np
import pickle

def get_constant(params_dict,LL,MM):

    if LL == 2 and MM == 0 :

        # Retrieve B for (2,0), (4,0), and (6,0)
        B20 = params_dict.get((2,0))
        B40 = params_dict.get((4,0))
        B60 = params_dict.get((6,0))

        constant = -3./2.*B20 - 5.*B40 - 21./2.*B60

    elif LL == 4 and MM == 0 :

        # Retrieve B for (4,0), and (6,0)
        B40 = params_dict.get((4,0))
        B60 = params_dict.get((6,0))

        constant =  35./8.*B40 + 189./8.*B60

    elif LL == 6 and MM == 0 :

        # Retrieve B for (6,0)
        B60 = params_dict.get((6,0))

        constant = -231./16.*B60

    elif LL == 2 and MM == 1 :

        # Retrieve B for (2,1), (4,1), (6,1)
        B21 = params_dict.get((2,1))
        B41 = params_dict.get((4,1))
        B61 = params_dict.get((6,1))

        constant = -2.*np.sqrt(3./2.)*B21 +2.*np.sqrt(5.)*B41 -2.*np.sqrt(21./2.)*B61

    elif LL == 2 and MM == -1 :

        # Retrieve B for (2,-1), (4,-1), (6,-1)
        B21 = params_dict.get((2,-1))
        B41 = params_dict.get((4,-1))
        B61 = params_dict.get((6,-1))

        constant = 2.*np.sqrt(3./2.)*B21 -2.*np.sqrt(5.)*B41 +2.*np.sqrt(21./2.)*B61

    elif LL == 2 and MM == 2 :

        # Retrieve B for (2,2), (4,2), (6,2)
        B22 = params_dict.get((2,2))
        B42 = params_dict.get((4,2))
        B62 = params_dict.get((6,2))

        constant = np.sqrt(3./2.)*B22 + 3.*np.sqrt(5./2.)*B42 + np.sqrt(105.)*B62

    elif LL == 2 and MM == -2 :

        # Retrieve B for (2,-2), (4,-2), (6,-2)
        B22 = params_dict.get((2,-2))
        B42 = params_dict.get((4,-2))
        B62 = params_dict.get((6,-2))

        constant = -np.sqrt(3./2.)*B22 - 3.*np.sqrt(5./2.)*B42 - np.sqrt(105.)*B62

    elif LL == 4 and MM == 1 :

        # Retrieve B for (4,1), (6,1)
        B41 = params_dict.get((4,1))
        B61 = params_dict.get((6,1))

        constant = 7./2.*np.sqrt(5.)*B41 + 9.*np.sqrt(21./2.)*B61

    elif LL == 4 and MM == -1 :

        # Retrieve B for (4,-1), (6,-1)
        B41 = params_dict.get((4,-1))
        B61 = params_dict.get((6,-1))

        constant = -7./2.*np.sqrt(5.)*B41 - 9.*np.sqrt(21./2.)*B61

    elif LL == 4 and MM == 2 :

        # Retrieve B for (4,2), (6,2)
        B42 = params_dict.get((4,2))
        B62 = params_dict.get((6,2))

        constant = -7./2.*np.sqrt(5./2.)*B42 - 3.*np.sqrt(105.)*B62

    elif LL == 4 and MM == -2 :

        # Retrieve B for (4,-2), (6,-2)
        B42 = params_dict.get((4,-2))
        B62 = params_dict.get((6,-2))

        constant = 7./2.*np.sqrt(5./2.)*B42 + 3.*np.sqrt(105.)*B62

    elif LL == 4 and MM == 3 :

        # Retrieve B for (4,3), (6,3)
        B43 = params_dict.get((4,3))
        B63 = params_dict.get((6,3))

        constant = -1./2.*np.sqrt(35.)*B43 - np.sqrt(105.)*B63

    elif LL == 4 and MM == -3 :

        # Retrieve B for (4,-3), (6,-3)
        B43 = params_dict.get((4,-3))
        B63 = params_dict.get((6,-3))

        constant = 1./2.*np.sqrt(35.)*B43 + np.sqrt(105.)*B63

    elif LL == 4 and MM == 4 :

        # Retrieve B for (4,4), (6,4)
        B44 = params_dict.get((4,4))
        B64 = params_dict.get((6,4))

        constant = 1./4.*np.sqrt(35./2.)*B44 + 15./4.*np.sqrt(7./2.)*B64

    elif LL == 4 and MM == -4 :

        # Retrieve B for (4,-4), (6,-4)
        B44 = params_dict.get((4,-4))
        B64 = params_dict.get((6,-4))

        constant = -1./4.*np.sqrt(35./2.)*B44 - 15./4.*np.sqrt(7./2.)*B64

    elif LL == 6 and MM == 1 :

        B61 = params_dict.get((6,1))

        constant = -33./4.*np.sqrt(21./2.)*B61

    elif LL == 6 and MM == -1 :

        B61 = params_dict.get((6,-1))

        constant = 33./4.*np.sqrt(21./2.)*B61

    elif LL == 6 and MM == 2 :

        B62 = params_dict.get((6,2))

        constant = 33./16.*np.sqrt(105.)*B62

    elif LL == 6 and MM == -2 :

        B62 = params_dict.get((6,-2))

        constant = -33./16.*np.sqrt(105.)*B62

    elif LL == 6 and MM == 3 :

        B63 = params_dict.get((6,3))

        constant = 11./8.*np.sqrt(105.)*B63

    elif LL == 6 and MM == -3 :

        B63 = params_dict.get((6,-3))

        constant = -11./8.*np.sqrt(105.)*B63

    elif LL == 6 and MM == 4 :

        B64 = params_dict.get((6,4))

        constant = -33./8.*np.sqrt(7./2.)*B64

    elif LL == 6 and MM == -4 :

        B64 = params_dict.get((6,-4))

        constant = 33./8.*np.sqrt(7./2.)*B64

    elif LL == 6 and MM == 5 :

        B65 = params_dict.get((6,5))

        constant = -3./8.*np.sqrt(77.)*B65

    elif LL == 6 and MM == -5 :

        B65 = params_dict.get((6,-5))

        constant = 3./8.*np.sqrt(77.)*B65

    elif LL == 6 and MM == 6 :

        B66 = params_dict.get((6,6))

        constant = 1./16.*np.sqrt(231.)*B66

    elif LL == 6 and MM == -6 :

        B66 = params_dict.get((6,-6))

        constant = -1./16.*np.sqrt(231.)*B66

    return constant

def make_const_dict(params_dict):

    # Initialize dictionary for Mag Aniso Constants:
    constant_dict = {}

    # Loop through L and M, and add in values for dictionary
    for LL in list(range(2,8,2)):
        for MM in list(range(-LL,LL+1)):
            constant = get_constant(params_dict,LL,MM)
            constant_dict[(LL,MM)] = constant

    return(constant_dict)


def main():

    with open("params_dict.pkl","rb") as f:
        params_dict = pickle.load(f)

    constant_dict = make_const_dict(params_dict)

    with open("constant_dict.pkl","wb") as f:
        pickle.dump(constant_dict, f)
    return

main()
