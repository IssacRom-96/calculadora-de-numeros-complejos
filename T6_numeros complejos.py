# -*- coding: utf-8 -*-
"""
@author: Issac Romero
"""
"""atributos: imaginario y real 
    - 1 constructor que permita definir desde el inicio los
        valores de la parte real y la parte imaginaria
    - funcion o metodo que permita modificar la parte real
        y la parte imaginaria 
    - funciones o metodos para:
        1. sumar (add)
        2. restar (sub)
        3. multiplicar (mull)
        4. dividir (div)
"""
class numComplex:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag =imag
    
    def setValues(self,real,imag):  
        self.real = real
        self.imag = imag
        
    def getreal(self):
        return self.real
    
    def imag(self):
        return self.imag
        
    def addComplex(self,z):
        #self.real = self.real + z.real
        self.real += z.real
        self.imag +=z.imag
        
    def subComplex(self,z):
       # self.real = self.real + z.real
        self.real -= z.real
        self.imag -= z.imag
        
       #######################################################
    def __add__(self,z):
        self.real = self.real + z.real
        #self.real += z.real
        self.imag += z.imag  
        z_aux = numComplex(self.real, self.imag)
        return z_aux
        ######################################################
        
        ######################################################
    def __sub__(self,z):
        self.real = self.real - z.real
        
        self.imag -= z.imag
        z_aux = numComplex(self.real, self.imag)
        return z_aux 
        ######################################################
        
    def mulComplex(self, z):
        a1= self.real
        b1= self.imag
        a2= z.real
        b2= z.imag
        self.real = a1*a2 - b1*b2
        self.imag = a1*b2 + a2*b1
        
        ######################################################
    def __mul__(self,z):
        
        a1= self.real
        b1= self.imag
        a2= z.real
        b2= z.imag
        self.real = a1*a2 - b1*b2
        self.imag = a1*b2 + a2*b1
        z_aux = numComplex(self.real, self.imag)
        return z_aux
        ######################################################
        
        ######################################################
    def __truediv__(self,z):
        self.mulComplex(z.conjugate())
        z.mulComplex(z.conjugate())
        
        #sel.real= self.real/z.real
        self.real /= z.real
        self.imag /= z.real
        
        z_aux = numComplex(self.real, self.imag)
        return z_aux
        ######################################################
        
        ######################################################

    def conjugate(self):
        z_conjugate = \
        numComplex(self.real, - self.imag)
        return z_conjugate
    
    def divComplex(self,z):
        self.mulComplex(z.conjugate())
        z.mulComplex(z.conjugate())
        
        #sel.real= self.real/z.real
        self.real /= z.real
        self.imag /= z.real
        
    def printComplex(self):
        print(self.real,"+", self.imag,"j")
    
z1= numComplex(1,2)
z2= numComplex(3,4)

z3 = 1 + 2j
z4 = 3 + 4j

print("........ OPERACIONES CON NUESTRA CLASES Y PYTHON......")
z1.addComplex(z2)
z1.printComplex()
print(z3+z4)

print(".............resta......")
z1.setValues(1,2)
z1.subComplex(z2)
z1.printComplex()
print(z3-z4)

print(".............multiplicacion......")
z1.setValues(1,2)
z1.mulComplex(z2)
z1.printComplex()
print(z3*z4)

print("...........division............")
z1.setValues(1,2)
z1.divComplex(z2)
z1.printComplex()
print(z3/z4)

print("..............conjugado......")
z4 = 1 + 2j
z5 = z4.conjugate()
print(z5)


print("operandores sobrecargados")
z1 = numComplex(1,2)
z2 = z1.real + z1.imag*1j
print(z2 + z4)
print(z2-z4)
print(z2*z4)
print(z2/z4)







