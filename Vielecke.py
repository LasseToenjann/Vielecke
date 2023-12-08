from turtle import *
shape("turtle")

m = int(numinput("Ecken","Wie viele Ecken soll ihr Vieleck haben?"))
for i in range (m):
	fd(10)
	rt(360/m)
