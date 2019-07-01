# print(int(netaddr.IPAddress('1.2.3.4')))
# print(str(netaddr.IPAddress(16909060)))

#Sample Input: 
# 2^2  129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25 || 129.0.0.1-129.0.0.5,12.0.0.5 || 12.0.0.2,11.0.0.1-11.0.0.5 || 1.0.0.54,0.0.0.43

# Combo2 Part1 1.0.0.54,0.0.0.43,12.0.56.34 || 12.0.0.2,11.0.0.1-11.0.0.5,1.0.0.3 || 12.0.0.2,11.0.0.1-11.0.0.5,1.0.0.3-1.0.0.7
# Combo2 Part2 1.0.0.54,0.0.0.43,0.0.0.1-0.0.0.20 || 129.0.0.1-129.0.0.5,12.0.0.5,192.0.0.1-192.0.0.45 || 129.0.0.1-129.0.0.5,12.0.0.5,192.0.0.1
# Combo2 Part3 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1 || 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1-192.0.0.45

# Combo3 Part1 1.0.0.54,0.0.0.43,12.0.56.34,192.0.0.33 || 1.0.0.54,0.0.0.43,12.0.56.34,192.0.0.33-192.0.0.36 || 0.0.0.43,12.0.56.34,192.0.0.33-192.0.0.36,1.0.0.54
# Combo3 Part2 12.0.56.34,192.0.0.33-192.0.0.36,1.0.0.54,0.0.0.43 || 1.0.0.54,0.0.0.43,129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25 || 1.0.0.54,129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,0.0.0.43
# Combo3 Part3 1.0.0.54,129.0.0.1-129.0.0.5,0.0.0.43,11.0.0.1-11.0.0.5 || 255.255.255.255,129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1-192.0.0.45 || 192.0.0.33-192.0.0.36,129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1-192.0.0.4
# Combo3 Part4 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1-192.0.0.45,0.0.0.4 || 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,192.0.0.1,192.0.0.45-192.0.0.48 || 200.0.0.1-200.0.0.4,192.0.0.1,192.0.0.45-192.0.0.48,11.0.0.1-11.0.0.5 
# Combo3 Part5 129.0.0.1-129.0.0.5,12.0.0.23-12.0.0.25,1.0.0.54,0.0.0.43 || 129.0.0.1-129.0.0.5,1.0.0.54,0.0.0.43,12.0.0.23-12.0.0.25 || 12.0.0.23-12.0.0.25,0.0.0.43,11.0.0.1-11.0.0.5,1.0.0.54
# Combo3 Part6 129.0.0.1-129.0.0.5,1.0.0.54,0.0.0.43,12.0.56.34


# Validation Sample Input
# 12.0.0.5,129.0.0.1-129.0.0.5,129.0.0.4,192.0.0.1-192.0.0.45
# 12.0.0.5,129.0.0.1-129.0.0.5,129.0.0.2-129.0.0.3,192.0.0.1-192.0.0.45
# 12.0.0.5,129.0.0.1-129.0.0.2,129.0.0.3-129.0.0.5,192.0.0.1-192.0.0.45


#UPDATE 0 and 255x CHECK 0.0.0.0-34.0.0.0,192.0.0.4

import netaddr
import re

from datetime import datetime
start_time = datetime.now()

#Taking Input
inp_string = input()		


def blocked_ip(inp):
	
	#PHASE 1: Parse the String

	listt = []
	syn = []

	syntax = re.sub("[^-|,]", "", inp)

	if not syntax:
		syn.append(0)


	for c in syntax:
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


	listt = re.split(',|-',inp)

	length = len(listt)

	for i in range(length):
	        listt[i] = int(netaddr.IPAddress(listt[i]))

	# PHASE 2: Merging and Sorting

	yx = list(map(list,zip(listt,syn)))

	yx.sort()


	# PHASE 3: Validation

	flag_stack = []

	for sub_list in yx:	
		flag_stack.append(sub_list[1])

	count = 0

	index_s = None
	index_e = None
	prev_flag = flag_stack[0]

	length = len(flag_stack)
	for i in range(1,length):
		if ((flag_stack[i] == 0 or flag_stack[i] == 1) and (prev_flag == 1)):
			count += 1
			if index_s is None:
				index_s = i-1
		elif (flag_stack[i] == 2 and (prev_flag == 0 or prev_flag == 2)) :
			count -= 1
			if count == 0:
				if index_e is None:
					index_e = i
		prev_flag = flag_stack[i]
		

	if (index_s is not None and index_e is not None):
		del yx[index_s+1:index_e]


	last_seen = yx[0][1]
	last_notused = yx[0][0]

	for not_used, value in yx[1:]:
		if last_seen == 0 and value == 2:
			print("Error with Single IP")  
			exit()
		last_seen = value
		last_notused = not_used




	# PHASE 4: Modification 

	for sub_list in yx:
		if sub_list[0] == 0 or sub_list[0] == 4294967295:
			continue

		elif sub_list[1] == 0:
			index = yx.index(sub_list) 
			sub_list[0] = sub_list[0] - 1
			new_list = [sub_list[0] + 2, 3]
			yx.insert(index + 1, new_list)

		elif sub_list[1] == 1:
			sub_list[0] = sub_list[0] - 1

		elif sub_list[1] == 2:
			sub_list[0] = sub_list[0] + 1


	if yx[0][0] != 0:
		new_list = [0,3]
		yx.insert(0,new_list)
	if yx[-1][0] != 4294967295:
		new_list = [4294967295,1]
		yx.append(new_list)

	prev_ip = yx[0][0]
	for sub_list in yx[1:]:
		if sub_list[0] == prev_ip:
			index = yx.index(sub_list)
			del yx[index]
		prev_ip = sub_list[0]	


	# PHASE 5: String Generation
	op_string = ""
	for sub_list in yx:
		if sub_list[1] == 3: 
			ip_add = str(netaddr.IPAddress(sub_list[0]))
			op_string = op_string + ip_add + "-"
		if sub_list[1] == 0 or sub_list[1] == 1:
			ip_add = str(netaddr.IPAddress(sub_list[0]))
			op_string = op_string + ip_add + ","
		if sub_list[1] == 2:
			ip_add = str(netaddr.IPAddress(sub_list[0]))
			op_string = op_string + ip_add + "-"		

	op_string = op_string[:-1]


	end_time = datetime.now()
	print('\nDuration: {}'.format(end_time - start_time))

	return op_string

final = blocked_ip(inp_string)
print("Output String: \n", final)
