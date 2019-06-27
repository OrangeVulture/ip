# print(int(netaddr.IPAddress('1.2.3.4')))
# print(str(netaddr.IPAddress(16909060)))

#Sample Input: 
# 2^2  129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25 || 129.0.0.1-129.0.0.5,12.0.0.5 || 12.0.0.2,11.0.0.1-11.0.0.5 || 1.0.0.54,0.0.0.43

# Combo2 Part1 1.0.0.54,0.0.0.43,12.0.56.34 || 12.0.0.2,11.0.0.1-11.0.0.5,1.0.0.3 || 12.0.0.2,11.0.0.1-11.0.0.5,1.0.0.3-1.0.0.7
# Combo2 Part2 1.0.0.54,0.0.0.43,0.0.0.1-0.0.0.20 || 129.0.0.1-129.0.0.5,12.0.0.5,192.0.0.1-192.0.0.45 || 129.0.0.1-129.0.0.5,12.0.0.5,192.0.0.1
# Combo2 Part3 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1 || 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1-192.0.0.45

#Combo3 Part1 1.0.0.54,0.0.0.43,12.0.56.34,192.0.0.33 || 1.0.0.54,0.0.0.43,12.0.56.34,192.0.0.33-192.0.0.36 || 0.0.0.43,12.0.56.34,192.0.0.33-192.0.0.36,1.0.0.54
#Combo3 Part2 12.0.56.34,192.0.0.33-192.0.0.36,1.0.0.54,0.0.0.43 || 1.0.0.54,0.0.0.43,129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25 || 1.0.0.54,129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,0.0.0.43
#Combo3 Part3 1.0.0.54,129.0.0.1-129.0.0.5,0.0.0.43,11.0.0.1-11.0.0.5 || 255.255.255.255,129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1-192.0.0.45 || 192.0.0.33-192.0.0.36,129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1-192.0.0.4
#Combo3 Part4 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1-192.0.0.45,0.0.0.4 || 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1,192.0.0.45-192.0.0.48 || 200.0.0.1-200.0.0.4,192.0.0.1,192.0.0.45-192.0.0.48,11.0.0.1-11.0.0.5 
#Combo3 Part5 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,1.0.0.54,0.0.0.43 || 129.0.0.1-129.0.0.5,1.0.0.54,0.0.0.43,12.0.0.23-12.0.0.25 || 12.0.0.23-12.0.0.25,0.0.0.43,11.0.0.1-11.0.0.5,1.0.0.54
#Combo3 Part6 129.0.0.1-129.0.0.5,1.0.0.54,0.0.0.43,12.0.56.34



# Validation Sample Input
# 12.0.0.5,129.0.0.1-129.0.0.5,129.0.0.4,192.0.0.1-192.0.0.45


import netaddr
import re


#Taking Input
inp = input()		


#Parse the String

listt = []
syn = []

syntax = re.sub("[^-|,]", "", inp)

if not syntax:
	syn.append(0)

print(syntax)
for c in syntax:
	print(c)
	if c == ',':
		if not syn:
			syn.append(0)
		syn.append(0)

	if c == '-':
		if not syn:
			syn.append(1)
			syn.append(2)
		if syn[-1] == 0:
			del syn[-1]
			syn.append(1)
			syn.append(2)		

print("Printing - , List")
print(syn)

listt = re.split(',|-',inp)
print("Printing after re.split")
print(listt)

length = len(listt)

for i in range(length):
        listt[i] = int(netaddr.IPAddress(listt[i]))
print("Printing after conversion")
print(listt)

# Merging and Sorting

yx = list(map(list,zip(listt,syn)))

print("Before Merging and Sorting: ")
print(yx)

yx.sort()

print("After Mergng and Sorting: ")
print(yx)


# Validation

last_seen = yx[0][1]
for not_used, value in yx[1:]:
	if last_seen == 1 and value != 2:
		print("Error with Range of IP")
	if last_seen == 0 and value == 2:
		print("Error with Single IP") 
	last_seen = value

# Modification 

for sub_list in yx:
	if sub_list[1] == 0:
		index = yx.index(sub_list) 
		sub_list[0] = sub_list[0] - 1
		new_list = [sub_list[0] + 2, 3]
		yx.insert(index + 1, new_list)

	if sub_list[1] == 1:
		sub_list[0] = sub_list[0] - 1

	if sub_list[1] == 2:
		sub_list[0] = sub_list[0] + 1

print("After Mod: ")
print(yx)

# String Generation

