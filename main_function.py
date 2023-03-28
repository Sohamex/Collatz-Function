import math
import cmath
    
def Clz(x):
        
    cosx = (cmath.cos(x*cmath.pi))**(x)

    cosx1 = (cmath.cos(x*cmath.pi))**(x + 1)

    Cxp = (cosx1 + cosx)/2
    Cxm = (cosx1 - cosx)/2

    result = ((3*x)/(1 + 5*(Cxp))) + Cxm

    return result
