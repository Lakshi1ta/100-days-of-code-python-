#-------------------------------------------------------------------------------
# Name:        project2
# Purpose:
#
# Author:      kandp
#
# Created:     21-05-2024
# Copyright:   (c) kandp 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Welcome to the Tip Calculator!");
a=float(input("What was total bill? "));
b=int(input("How much tip would you like to give? 10,12 or 15?"));
c=int(input("How many people to split the bill?"));
totaltip=a*(b/100);
bill=a+totaltip;
billperperson=bill/c;
##bill=(float(a) + int(b)) / int(c);
print("Each person should pay:",round(billperperson,2));