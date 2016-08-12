from decimal import *
getcontext().prec = 10000
## Factorial function

def fac(n):
  a = 1
  while n > 0:
    a *= n
    n -= 1
  return(a)

##Pi calculator

def pie():
  n = s = Decimal(0)## n is the polynomial degree
  check = 1
  print("\nPi calculated with the slow method")
  while check != s:
    rob = 0
    r = 1
    while rob < r * 1000000:
      s += ((-Decimal(1))**n)*(Decimal(4)/(Decimal(2)*n+Decimal(1)))
      n += 1
      rob += 1
    else:
      r += 1
    print(('{0:.1000f}'.format(s)))

## Gauss-Legendre algorithm
    
def pietwo():
  a = p = Decimal(1.0)
  check = 1
  b = Decimal(1.0) /(Decimal(2) ** (Decimal(0.5)))
  t = Decimal(.25)
  s = n = Decimal(0)
  while check != s:
    check = s
    an = a
    bn = b
    a = (an + bn) / Decimal(2)
    b = (an*bn)**(Decimal(0.5))
    t -= p*(an - a)**Decimal(2)
    p = Decimal(2)*p
 ##   n += 1 ##Legacy code?
    s = (a + b)**Decimal(2) / (Decimal(4) * t)
  print('{0:.10000f}'.format((a + b)**Decimal(2) / (Decimal(4) * t)))
  print("\nPi calculated with the Gauss-Legendre algorithm\n")

## Machin-like formula
  
def piethree():
  return(Decimal(16)*arctan(Decimal(1)/Decimal(5))) - (Decimal(4)*arctan(Decimal(1)/Decimal(239)))
  
def piethreex():
  print('{0:.10000f}'.format((Decimal(16)*arctan(Decimal(1)/Decimal(5))) - (Decimal(4)*arctan(Decimal(1)/Decimal(239)))))
  print("\nPi calculated with the Machin-like formula\n")

## Nonic convergence
  
def piefour():
  a = Decimal(1) / Decimal(3)
  r = (Decimal(3)**(Decimal(.5)) - Decimal(1)) / Decimal(2)
  s = (Decimal(1) - r**Decimal(3))**(Decimal(1) / Decimal(3))
  check = 1
  check1 = 2
  n = Decimal(0)
  while check != check1:
    check = check1
    t = Decimal(1) + (Decimal(2) * r)
    u = (Decimal(9) * r * (Decimal(1) + r + (r**Decimal(2))))**(Decimal(1)/Decimal(3))
    v = t**Decimal(2)+ t * u + u**Decimal(2)
    w = (Decimal(27) * (Decimal(1)+ s + (s**Decimal(2)))) / v
    a = w * a + Decimal(3)**(Decimal(2) * n - Decimal(1)) * (Decimal(1) - w)
    s = ((Decimal(1) - r)**Decimal(3)) / ((t + Decimal(2) * u) * v)
    r = (Decimal(1) - s**Decimal(3))**(Decimal(1) / Decimal(3))
    n += Decimal(1)
    check1 = Decimal(1) / a
    print('{0:.1000f}'.format(check1))
  print('{0:.10000f}'.format(check1))
  print("\nPi calculated with Borwein's algorithm in nonic convergence\n")

def arctan(x):
  s = Decimal(0)
  n = 0
  check = 1
  while check != s:
    check = s
    s  += ((((-Decimal(1))**n) * (x**((Decimal(2)*n)+Decimal(1))))/(((Decimal(2)*n)+Decimal(1))))
    n  += 1
    if -10**(-20) <= s <= 10**(-20):
      return 0
    if s > 10**20:
      return infinity
    if check == s:
      return s

def arctanx(x):
  s = Decimal(0)
  n = 0
  check = 1
  while check != s:
    check = s
    s  += ((((-Decimal(1))**n) * (x**((Decimal(2)*n)+Decimal(1))))/(((Decimal(2)*n)+Decimal(1))))
    n  += 1
    print('{0:.500f}'.format(s))
    if -10**(-20) <= s <= 10**(-20):
      print("0")
      return 0
    if s > 10**20:
      print("infinity")
      return 0
    if check == s:
      return 0

## Sin and cos calculator
    
def calc(x,r):
  s = n = 0## n is the polynomial degree
  check = 1
  while check != s:
    check = s
    s += ((((-Decimal(1))**n) * (x**((Decimal(2)*n)+r)))/((fac((Decimal(2)*n)+r))))
    n += 1
    print('{0:.500f}'.format(s))
    if -10**(-16) <= s <= 10**(-16):
      print("0")
      return 0

## Tan calculator (BROKEN FOR NUMBERS > pi/2)
    
def tan(x):
  n = s = ts = 0
  check = 0
  while 1:
    s  += ((((-1)**n) * (x**((2*n)+1)))/((fac((2*n)+1))))
    ts += ((((-1)**n) * (x**((2*n))))/((fac((2*n)))))
    n  += 1
    print('{0:.500f}'.format(s/ts))
    if -10**(-15) <= s/ts <= 10**(-15):
      print("0")
      return 0
    if s/ts > 10**16:
      print("infinity")
      return 0
    if check == s/ts:
     return 0
    check = s/ts

## Checks if its a number and handles other cases
    
def isnumber(s):
  try:
    float(s)
    return 1
  except ValueError:
    pass
  return 0

##THIS IS THE USER INTERFACE##

def f(mod):
  r = 2
  
## User inputs the desired trig function

  trig = input("\nsin, cos, tan, or arctan: ")

  bri = 0
  if trig in ["calc pi long", "calc long pi", "calc pi", "calculate pi"]:
    if trig in ["calc pi long", "calc long pi"]:
      pie()
    piethreex()
    print("*******************************************")
    pietwo()
    
    return 0
  elif trig in ["arctan", "arctan(x)", "arctanx"]:
    tfun = "arctan(x)"
    bri = 1
  elif trig in ["tan", "tan(x)", "tanx"]:
    tfun = "tan(x)"
  elif trig in ["sin", "sin(x)", "sinx"]:
    r = 1## Used in Taylor series
    tfun = "sin(x)"
  elif trig in ["cos", "cos(x)", "cosx)"]:
    r = 0## Used in Taylor series
    tfun = "cos(x)"
  else:
    print("Try again...")
    return 0
    
  x = input(tfun + "|   x =  ")

  z = 0
  if x in ["pi", "Pi"]:
    x=piethree()   ##3.14159265358979323846264338327
  elif x in ["pi/2", "Pi/2", "pi / 2", "Pi / 2"]:
    x=piethree()/2 ##1.57079632679489661923132169163
  elif x in ["pi/3", "Pi/3", "pi / 3", "Pi / 3"]:
    x=piethree()/3 ##1.04719755119659774615421446109
  elif x in ["pi/4", "Pi/4", "pi / 4", "Pi / 4"]:
    x=piethree()/4 ##1.04719755119659774615421446109
  elif x in ["pi/6", "Pi/6", "pi / 6", "Pi / 6"]:
    x=piethree()/6 ##0.5235987755982988730771072305465
  elif x in ["root3/2", "root(3)/2", "sqrt3 / 2", "sqrt3/2", "sqrt(3)/2", "Sqrt(3)/2"]:
    x=0.86602540378443864676372317075
  elif x in ["root2/2", "root(2)/2", "sqrt(2)/2", "Sqrt(2)/2)", "sqrt2/2)", "Sqrt2/2"]:
    x=0.70710678118654752440084436210
  elif not x:
    print("Try again..")
    return 0
  elif not isnumber(x):
    print("Try again...")
    return 0
  else:
    x = Decimal(x)
  if mod == 0:
    print("Calculating for", x, "radians")
    
## Radian converter

  elif mod == 1:
    print("Calculating for", x, "degrees")    
    x *= Decimal(6.28318530717958647693) / Decimal(360)
    
## Converts negative numbers

  if x < 0:
    x = -x
    
## Shrinks down x for better approximation

  if mod == 0:
    if x >= 7:
      x %= 6.28318530717958647693         

  
## Trig Functions called
      
  if z == 1:
    tan(x)
  elif bri == 1:
    arctanx(x)
  else:
    calc(x,r)
    
############# Runs function forever###############

go = 1
print("###       This calculator approximates        ###")
print("###   sin(x), cos(x), tan(x), and arctan(x)   ###")
print("###           using Taylor series.            ###\n###                                           ###")
print("###              Other Commands:              ###\n###                                           ###")
print("###  Calculate pi using | Calculate pi using  ###")
print("###  Gauss-Legendre and |   the slow method   ###")
print("###     Machin-like     |                     ###")
print("###    type \"calc pi\"   | type \"calc pi long\" ###")
mode = input ("\nRadians or degrees: ")
if mode in ["calc piefour", "calc pi long", "calc long pi", "calc pi", "calculate pi"]:
  if mode in ["calc pi long", "calc long pi"]:
    pie()
  if mode == "calc piefour":
    piefour()
  piethreex()
  print("*******************************************")
  pietwo()
  mod = 0
elif mode in ["Radians", "radians", "rad", "rads"]:
  mod = 0
elif mode in ["Degrees", "degrees", "deg", "Deg"]:
  mod = 1
else:
  print("Using Radians")
  mod = 0
while go == 1:
  f(mod)
