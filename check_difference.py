# Check for difference
# Use case:
# 1. Check for hash file sums
from time import sleep
from difflib import ndiff

target_sum = str(input("Input file checksum here: "))
base_sum = str(input("Input calculated checksum here: "))

if target_sum == base_sum:
  print("No Difference")
else:
  print('{} => {}'.format(base_sum,target_sum))  
  for i,s in enumerate(ndiff(base_sum, target_sum)):
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))  
  
input("Press enter to exit...")