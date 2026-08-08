# Slicing is basecally like between 
name = "BA-234-36"
#  B  A  -  2  3  4  -  3  6
#  0  1  2  3  4  5  6  7  8
# -9 -8 -7 -6 -5 -4 -3 -2 -0
print(name[0:2])
print(name[2:-1]) # the same as total number minus the number 9-1 = 8 the same 2:8
print(name[2:8])

name = "Harky01234456789"
# print(name[0:10:n]) # Skip n -1  characters
print(name[0:10:1]) # Skip 0 character nothing will happen when 0

print(name[0:10:2]) # sKIP 2 Characters n-1 2-1 is 1 characters only 

print(name[:4]) # Replcae the fist empty number with 0 # number [0:4]
print(name[0:]) # Replcae the second empty number with length [0:15]

print(name[1:]) # Replcae the second empty number with length [1:15]