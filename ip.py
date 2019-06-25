import netaddr
import re

# print(int(netaddr.IPAddress('1.2.3.4')))
# print(str(netaddr.IPAddress(16909060)))

#Sample: 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25 || 129.0.0.1-129.0.0.5,12.0.0.5 || 12.0.0.2,11.0.0.1-11.0.0.5 || 1.0.0.54,0.0.0.43
# 
# || 12.0.0.2-12.0.0.5,10.0.0.86,13.0.0.42,11.0.0.3-11.0.0.5

inp = input()		#Taking Input

#Parse the String

listt = []
syn = []

syntax = re.sub("[^-|,]", "", inp)

for i, c in enumerate(syntax):
	if c == ',':
		if not syn:
			syn.append(0)
		elif syn[-1] == 0:
			syn.append(0)
		
			syn.append(0)

	if c == '-':
		if not syn:
			syn.append(1)
			syn.append(2)
		elif syntax[i-1] == ',' and syntax[i-2] == '-':
			syn.append(1)
			syn.append(2)
		else:
			del syn[-1]			
			syn.append(1)
			syn.append(2)			

# if ',' in inp or '-' in inp:

# 	for c in inp:

# 		if c == ',':
# 			if not syn:
# 				syn.append(0)

# 			elif syn[-1] != 2:
# 				syn.append(0)
# 			else:
# 				syn.append(0)

# 		if c == '-':
# 			if not syn:
# 				syn.append(1)
# 				syn.append(2)
# 			elif syn[-1] != 0:
# 				syn.append(1)
# 				syn.append(2)
# 			else:
# 				del syn[-1]

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
yx = list(zip(listt,syn))
yx.sort()
print("After Sorting: ")
print(yx)




# yx = list(map(list, yx))
# print("Printing after Mapping:")
# print(yx)

# yx.sort()
      
# print("Printing after sort:")
# print(yx)

