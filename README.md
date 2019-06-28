# ip

### Phases
- [x] Phase 1: Parse The string

Maintaining a separate List for all ',' and '-' in the input string and setting a flag value according to it. Single IP will have 0, starting Range of IP will have 1 and 2 is for ending range of IP.
Another List is maintained for storing all the IP in the string. It is then converted into its numeric value using the package netaddr. For example, we have IP as '1.2.3.4', its numeric vale is 16909060. The package netaddr provides a Function IPAddress() which can take in string input for Dot Notation IP and generate an integer value for the same IP and vice versa.

- [x] Phase 2: Merge and Sort the List of Lists

Now, we have 2 independent lists and they can be mapped to each other and can be stored in a List of Lists.
Once merged, the list of lists is sorted according to the IP values.

- [x] Phase 3: Validation 

We have a list of lists containing IPs which could be either clashing with each other. For example, A range of IP can be given and at the same time a single IP could be given which resides in between the range. Such validation on the string is done and error message will be printed out and the program will be exited.

- [x] Phase 4: Modification

Now, we have IP in the list of lists. But they are the IPs which are allowed and we have to generate an output which consists of the blocked IPs. So, we modify the list of lists accordingly. For each O flag, we have to decrease the IP by 1 and insert anorther list after the current index which contains an IP value +1 than the old IP, also a flag of 3 is stored for the corresponding new IP.

For Flag 1, it is the same as 0 but we are not going to be inserting a new list as we know it has some ending range whereas in case of 0, we don't have an ending range so we manually have to insert an IP.

For Flag 2, we know that is the ending range of IP, hence we increase the value of IP by 1.  

Once the above modifications are finished, we are checking if the input string contains the first IP i.e. 0.0.0.0 or the last IP i.e. 255.255.255.255. If they are not present, we insert or append them into our list of lists respectively. 

- [x] Phase 5: Generate output String  

Finally, we can generate the output string with the help of the flag variables which we have set. For 1 and 0 we append the ip address and a ','. For flag 2 and 3, we append the ip address and '-'. 

The final output string is generated. Although, the last element of the string will be a '-'. So, we just remove it, and then output the string. 