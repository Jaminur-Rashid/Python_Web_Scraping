#######################
# This is a test script
#######################
import  re
print(re.findall("\d+", "33 sss 777 . 88u88"))
print(type(re.findall("\d+", "33 sss 777 . 88u88")))
l=re.findall("\d+", "33 sss 777 . 88u88")
print(type(l[0]))