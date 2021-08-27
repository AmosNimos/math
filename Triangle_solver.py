#acos = cos-1
from math import acos
from math import cos
from math import asin
from math import sin
from math import atan
from math import tan

#Find the sides of a right-triangle
def f-side(Angle,Opos,Adja,Hypo):
	A = Angl
	a = Opos
	b = Adja
	c = Hypo

	if c == True:
		Opos=sin(A)*c
		Adja=cos(A)*c
		return Opos,Adja
	if b == True:
		Hypo=b/cos(A)
		Opos=b*tan(A)
		return Hypo,Opos 
	if a == True:
		Adja=a/tan(A)
		Hypo = a/sin(A)
		return Adja,Hypo
	else:
		return "Error","Error"

#Find the angle of a right-triangle
def f-angl(Angle,Opos,Adja,Hypo):
	A = Angle
	a = Opos
	b = Adja
	c = Hypo

	if a == True and c == True:
		A = asin(a/c)
		return A
	if b == True and c == True:
		A = acos(b/c)
		return A
	if a == True and c == True:
		A = atan(a/c)
		return A
	else:
		return "Error","Error"
