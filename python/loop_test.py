x=0

for x in range(5,10):
	print(x)

days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
	print(d)

for x in range(5,10):
	#if (x==7): break
	if (x % 2 == 0): 
		print(str(x) + " is even number")
		continue
	print(x)

days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i,d in enumerate(days):
	print(i, d)
