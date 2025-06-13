import numpy as np
from scipy.special import sph_harm
import sys
import pickle


# Lets use Lebedev quadrature to integrate!
# An integral I of a function f over the unit sphere is
# I[f] = Int dOmega f(Omega) = Int^pi_0 sin theta Int^2pi_0 f(theta,phi) dphi dtheta
# I[f] ~ 4pi sum^N_i w_i f(theta_i, phi_i)
# with i sampled from the N Lebedev Quadrature points

# What integrals do we want to compute on the unit sphere?

# Integrand: MCAE(theta_i, phi_i) Conjugate( Y_lm (theta_i, phi_i))
# This integral will give us the coefficient for MCAE expansion in spherical harmonics!


def read_data():

    # Open energies pickle array
    with open('energies.pkl','rb') as f:
        en = pickle.load(f)

    # Open Unit-sphere x,y,z points...
    with open('sx.pkl','rb') as f:
        sx = pickle.load(f)

    with open('sy.pkl','rb') as f:
        sy = pickle.load(f)

    with open('sz.pkl','rb') as f:
        sz = pickle.load(f)

    # Open Lebedev Quadrature weights...
    with open('sw.pkl','rb') as f:
        sw = pickle.load(f)

    return(en,sx,sy,sz,sw)

def ThetaPhi(sx,sy,sz):

    theta = [] ; phi = []
    for ii in list(range(np.size(sx))):
        temp = np.arctan2(np.sqrt(sx[ii]**2 + sy[ii]**2),sz[ii])
        theta.append(temp)

        temp = np.arctan2(sy[ii],sx[ii])
        phi.append(temp)

    return(theta,phi)

def SphHarm(l,m,theta,phi):
    return sph_harm(m,l,phi,theta)

def SphInt(en,sw,Ylm):

    fint = [a*b for a,b in zip(en,Ylm)]
    integrand = [a*b for a,b in zip(sw,fint)]
    Coeff = 4*np.pi*sum(integrand)

    return(Coeff)


def main():

    en,sx,sy,sz,sw = read_data()

    theta,phi = ThetaPhi(sx,sy,sz)

    # Store Mag Aniso Coeff data in a dictionary with L and M as keys
    coeff_dict = {}
    for LL in list(range(2,8,2)):
        for MM in list(range(-LL,LL+1)):

            Ylm = SphHarm(LL,MM,theta,phi)
            Coeff = SphInt(en,sw,Ylm)

            coeff_dict[(LL,MM)] = Coeff

    with open('coeff_dict.pkl', 'wb') as f:
        pickle.dump(coeff_dict, f)

    return

main()
