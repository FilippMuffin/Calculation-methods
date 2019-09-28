x = []
v = 23.0
e = 0.000001
a = int(input("Input start: "))
h = int(input("Input step: "))

for i in range(a, (a + (5 * h))):
	x.append(i)
	i += h

print(*x)

for x_i in x:
	i = 3.0 
	s = 0.0
	f = v*x_i
	n = 0
	while abs(f) > e:
		f *= -(x_i * v * x_i * v)/(i * (i - 1))
		s += f
		i += 2
		n += 1
		# print("f({0})={1}".format(n, f))
	print("S({0})={1}".format(x_i, s))
	print("N({0})={1}".format(x_i, n))