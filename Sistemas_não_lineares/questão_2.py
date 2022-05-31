import numpy as np
from numpy.linalg import inv
from numpy import array, outer, dot
from numpy.linalg import solve, norm, det
def f(xy):
  x,y = xy
  return [5*(x**2)-(y**2),
          y- ((np.sin(x)+np.cos(y))/4)]
  
                   
def jacobiana(xy):
  x,y = xy
  return [[10*x, -2*y],
          [-np.cos(x)/4, 1+(np.sin(y)/4)]]

def hessiana(xy):
  x,y = xy
  return [[10, -2],
          [np.sin(x)/4, np.cos(y)/4]]

def newton_rhapson(x0,ea):
  x = x0
  delta = 1
  while np.linalg.norm(delta) > ea:
    J = np.array(jacobiana(x))
    F = np.array(f(x))
    delta = np.linalg.solve(J,-F)
    x = x + delta
  return x

def modified_newton_rhapson(x0,ea):
  x = x0
  delta = 1
  J = np.array(jacobiana(x0))
  while np.linalg.norm(delta) > ea:
    F = np.array(f(x))
    delta = np.linalg.solve(J,-F)
    x = x + delta
  return x
def quasi_newton(x0,ea):
  x = x0
  delta = 1
  while np.linalg.norm(delta) > ea:
    J = np.array(hessiana(x))
    F = np.array(f(x))
    delta = np.linalg.solve(J,-F)
    x = x + delta
  return x
def broyden(x0,ea):
  x = x0  
  J = np.array(jacobiana(x0))
  z = np.array(f(x))
  while np.linalg.norm(z) > ea:
    F = np.array(f(x))
    s = np.linalg.solve(J,-F)
    x = s+x
    F1 = f(x)
    z = F1 - F
    J = J + (np.outer ((z - np.dot(J,s)),s)) / (np.dot(s,s))
    F = F1

  return x
def sherman_morrison(x0,ea):
  x = x0
  J = inv(jacobiana(x0))
  F = np.array(f(x))
  z = F
  while np.linalg.norm(z) > ea:
    s = J.dot(F)
    x = x-s
    F1 = np.array(f(x))
    z = F1 - F
    u = J.dot(z)
    d = - 1 * s
    J = J  + np.dot(((d-u).dot(d)), J) / np.dot(d,u) 
    F = F1
  return x


x0 = [1,1]
ea = 10**(-6)
print("método de newton modificado: ",modified_newton_rhapson(x0,ea))
print("método de quasi newton: ",quasi_newton(x0,ea))
print("método de broyden: ",broyden(x0,ea))
print("método de sherman morrison: ",sherman_morrison(x0,ea))   
