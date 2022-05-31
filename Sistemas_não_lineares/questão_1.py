import numpy as np
def f(xy):
  x,y = xy
  return [(10**(-6))*(np.e**(x*(10**3)/40)-1)-y,
          12-12*x-y]
                   
def jacobiana(xy):
  x,y = xy
  return [[(10**(-3)/40)*(np.e**(x*(10**3)/40)), -1],
          [-12, -1]
                                                    ]


def newton_rhapson(x0,ea):
  x = x0
  delta = 1
  while np.linalg.norm(delta) > ea:
    J = np.array(jacobiana(x))
    F = np.array(f(x))
    delta = np.linalg.solve(J,-F)
    x = x + delta
  return x
x0 = [1,0]
ea = 10**(-6)
k = newton_rhapson(x0,ea)
print(k)    
