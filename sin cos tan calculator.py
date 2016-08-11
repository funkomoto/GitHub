## Factorial function
def fac(n):
  a = 1
  while n > 0:
    a *= n
    n -= 1
  return(a)

##Pi calculator
def pi():
  n = s = 0## n is the polynomial degree
  check = 1
  while check != s:
    check = s
    s += ((-1)**n)(4/(2*n+1))  ##((((-1)**n) * (x**((2*n)+r)))/((fac((2*n)+r))))
    n += 1
    print(s)
      
## Sin and cos calculator
def calc(x,r):
  n = s = 0## n is the polynomial degree
  check = 1
  while check != s:
    check = s
    s += ((((-1)**n) * (x**((2*n)+r)))/((fac((2*n)+r))))
    n += 1
    print(s)
    if -10**(-16) <= s <= 10**(-16):
      print("0")
      return 0

## Tan calculator
def tan(x):
  n = s = ts = 0
  check = 0
  while 1:
    s  += ((((-1)**n) * (x**((2*n)+1)))/((fac((2*n)+1))))
    ts += ((((-1)**n) * (x**((2*n))))/((fac((2*n)))))
    n  += 1
    print(s/ts)
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
  z = 0## Used to call tan() later
  
## User inputs the desired trig function
  trig = input("\nsin, cos or tan: ")
  if trig in ["tan", "tan(x)", "tanx"]:
    z = 1## Used to call tan() later
  elif trig in ["sin", "sin(x)", "sinx"]:
    r = 1## Used in Taylor series
    z = 0
  elif trig in ["cos", "cos(x)", "cosx)"]:
    r = 0## Used in Taylor series
    z = 0
  else:
    print("Try again...")
    return 0
## User inputs the value of x
  if z == 1:
    tfun = "tan(x)"
  elif z == 0 and r == 1:
    tfun = "sin(x)"
  else:
    tfun = "cos(x)"
  x = input(tfun + "|   x =  ")
## Trig terminology dictionary
  if x in ["calc pi", "calculate pi"]:
    pi()
    return 0
  elif x in ["pi", "Pi"]:
    x=3.14159265358979323846264338327
  elif x in ["pi/2", "Pi/2", "pi / 2", "Pi / 2"]:
    x=1.57079632679489661923132169163
  elif x in ["pi/3", "Pi/3", "pi / 3", "Pi / 3"]:
    x=1.04719755119659774615421446109
  elif x in ["pi/4", "Pi/4", "pi / 4", "Pi / 4"]:
    x=1.04719755119659774615421446109
  elif x in ["pi/6", "Pi/6", "pi / 6", "Pi / 6"]:
    x=0.5235987755982988730771072305465
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
    x = float(x)
  if mod == 0:
    print("Calculating for", x, "radians")
## Radian converter
  elif mod == 1:
    print("Calculating for", x, "degrees")    
    x *= 6.28318530717958647693 / 360
## Converts negative numbers
  if x < 0:
    x = -x
## Shrinks down x for better approximation
  if mod == 0:
    if x >= 7:
      x %= 6.28318530717958647693         

  
## Trig Functions called
  if z == 1:##Defined in trig terminology dictionary
    tan(x)
  else:
    calc(x,r)
############# Runs function forever###############
go = 1
print("### This calculator approximates ###")
print("###  sin(x), cos(x), and tan(x)  ###")
print("###     using Taylor series.     ###\n")
mode = input ("\nRadians or degrees:")
if mode in ["Radians", "radians", "rad", "rads"]:
  mod = 0
elif mode in ["Degrees", "degrees", "deg", "Deg"]:
  mod = 1
else:
  print("Using Radians")
  mod = 0
while go == 1:
  f(mod)
