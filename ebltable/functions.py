# 03-06-2022 script containing pure model functions and model functions containing EBL absorption

import numpy as np

# read the EBL model 
from ebltable.ebl_from_model import EBL
ebl =  EBL.readmodel(model = 'dominguez')


E0 = 0.1 # TeV 
n0_scale = 1e-9

############################### pure model functions #####################################
# power law
def pl (E,N0,index):
    return n0_scale*N0*(E/E0)**(-index) 

# power law exponential cutoff
# a = 1/ecut

def epl (E,n0,index,a):
    return n0_scale*n0*(E/E0)**(-index)*np.exp(-a*E)

# Log Parabola
def logparabola(E,a,b,n0):
    return n0_scale*n0*(E/E0)**(-a-b*np.log(E/E0)) 

############################### model functions with EBL absorption ######################

# power law and EBL absorption
def pl_EBL(E, n0, index, h0, z):
    return pl(E, n0,index)*np.exp(-1.*ebl.optical_depth(z,E,H0 = h0))

# power law exponential cutoff and EBL absorption
# a = 1/ecut

def epl_EBL (E,n0,index,a,h0,z):
    return n0_scale*n0*(E/E0)**(-index)*np.exp(-a*E)*np.exp(-1.*ebl.optical_depth(z,E,H0 = h0))

# Log Parabola and EBL absorption
def logparabola_EBL(E,a,b,n0,h0,z):
    return n0_scale*n0*(E/E0)**(-a-b*np.log(E/E0))*np.exp(-1.*ebl.optical_depth(z,E,H0 = h0))