#!/usr/env python

import numpy as np
import pickle

def read_coeffs():

    with open('coeff_dict.pkl','rb') as f:
        coeff_dict = pickle.load(f)

    return(coeff_dict)

def coeffs_to_params_0(coeff_dict,LL):

    # retrieve the value of the MA Coefficient,
    # given values for L and M = 0:

    kappaL0 = coeff_dict.get((LL,0))

    # Wybourne normalization, instead of usually Condon-Shortley
    pref = np.sqrt((2.*LL + 1.)/(4.*np.pi))

    # Equations for BLM parameters, given Coefficients:
    BL0 = pref*kappaL0

    return(BL0)

def coeffs_to_params_non0(coeff_dict,LL,MM):

    # retrieve the value of the MA Coefficient,
    # given values for L and M > 0:

    kappaLpM = coeff_dict.get((LL,MM))

    # Same, but for L and -M:
    kappaLmM = coeff_dict.get((LL,-MM))

    # Wybourne normalization, instead of usually Condon-Shortley
    pref = np.sqrt((2.*LL + 1.)/(4.*np.pi))

    # Equations for BLM parameters, given Coefficients:
    # BAB, Aug 2026. SMG found error with BLmM equation; corrected in draft.
    # Recalculate numerical values, when appropriate. Odd MM (q) will be same.
    BLpM = pref*(1./2.)*(kappaLpM + (-1.)**(MM)*kappaLmM)
    # BLmM = 1j*pref*(1./2.)*((-1)**(MM)*kappaLpM - kappaLmM)
    BLmM = 1j*pref*(1./2.)*((-1)**(MM)*kappaLmM - kappaLpM)

    return(BLpM, BLmM)

def main():

    coeff_dict = read_coeffs()

    # Initialize Params_dict:
    params_dict = {}

    # Loop through all L and M values:
    for LL in list(range(2,8,2)):

        BL0 = coeffs_to_params_0(coeff_dict,LL)
        MM = 0
        params_dict[(LL, MM)] = BL0

        for MM in list(range(1,LL+1)):

            BLpM, BLmM = coeffs_to_params_non0(coeff_dict,LL,MM)
            params_dict[(LL,MM)] = BLpM
            params_dict[(LL,-MM)] = BLmM

    with open('params_dict.pkl','wb') as f:
        pickle.dump(params_dict,f)

    return

main()
