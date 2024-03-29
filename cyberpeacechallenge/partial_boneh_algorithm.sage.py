

# This file was *autogenerated* from the file partial_boneh_algorithm.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_64 = Integer(64); _sage_const_16 = Integer(16); _sage_const_3 = Integer(3)
import hashlib

def xor(xs, ys):
    return "".join(chr(ord(x).__xor__(ord(y))) for x, y in zip(xs, ys))

def to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % _sage_const_2 ) + h).zfill(length*_sage_const_2 ).decode('hex')
    return s if endianess == 'big' else s[::-_sage_const_1 ]

#Encodes using canonical representation: ax+b is b||a
def canonic(gID):
    poly = gID.polynomial().coefficients(sparse = False)
    return to_bytes(poly[_sage_const_0 ], _sage_const_64 ) + to_bytes(poly[_sage_const_1 ],_sage_const_64 )

#Precomputes some values for the computation of the twisted Weil pairing. 
def computeTwistedWeilParams(p):
    Fp = Integers(p)
    Pol = PolynomialRing(Fp, names=('btemp',)); (btemp,) = Pol._first_ngens(1)
    F2 = GF(p**_sage_const_2 , modulus=btemp**_sage_const_2 +_sage_const_1 , names=('a',)); (a,) = F2._first_ngens(1)
    E2 = EllipticCurve(F2,[_sage_const_0 ,_sage_const_1 ])
    xtemp1 = -Fp(_sage_const_1 )/Fp(_sage_const_2 )
    xtemp2 = sqrt(xtemp1**_sage_const_2 +xtemp1+_sage_const_1 )
    z = xtemp1+xtemp2*a 
    return (E2, z, p)

#Computes the "twisted" Weil pairing between P1 and P2. 
#You need to pass as an additionnal argument twistedWeilParams that are generated by the method computeTwistedWeilParams(p) during key generation
def twistedWeil(P1,P2, twistedWeilParams):
    (E2, z, p) = twistedWeilParams 
    P1E2 = E2(P1.xy()) 
    P2E2 = E2(P2.xy()) 
    qx,qy = P1E2.xy() 
    P1twisted =E2(qx*z,qy) 
    return P1twisted.weil_pairing(P2E2,p+_sage_const_1 ) 


def H2(input):
    return hashlib.sha512(canonic(input)).digest()

#Hash id to point on E
def HTP(E,p,q,id):
    h = int(hashlib.sha512(str(id) + "0").hexdigest()+hashlib.sha512(str(id) + "1").hexdigest(),_sage_const_16 ) 
    Fp = GF(p)
    y = Fp(h) 
    x = (y**_sage_const_2 -_sage_const_1 )**((_sage_const_2 *p-_sage_const_1 )/_sage_const_3 )
    Q_1 = E(x,y) 
    a_1 = (p+_sage_const_1 )//q
    Q = a_1 * Q_1 
    return Q

