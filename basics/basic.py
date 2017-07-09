
#Print
# in Python 3 print is a function, so this code will miserabily fail
print 1
print "Hello"
print 'Hello'
print "\n"
print "\"Alan Parson's Project\" \\"
print "\n"

#variable
name="Jorge"

#Basic Operators
print "Hello" + name
print "Hello" , name
print 1+1
print 2.3-1.2
print 2*3
print 6/2
print 5/4
print 5//4
print 5.0/4
print 5/4.0
print 5.0/4.0
print 5.0//4.0
print 100%33
print 2**2
print "\n"

print 1 is 1

a = 3
print -a
print +a
print ~a
print +4.896586478467814367861383826572623844239
print ~4
print ~-5
print ~-1
print "\n"
print "\n"


#Functions
def addOne(number):
    temp = number + 1
    return temp
print addOne(4)
print "\n"
print "\n"


# Control Structures

for i in range(5):
    print i

print "\n"

for letter in "Python":
    print letter

print "\n"

for fruit in ['apple', 'banana', 'mango']:
    print fruit

print "\n"

dictionary = {"fruta1": 'apple', "fruta2": 'banana', "fruta3": 'mango'}
for (key, value) in dictionary.items():
    print key
    print value

array = ['apple', 'banana', 'mango']
for (i,j) in enumerate(array):
    print i , j

print "\n"
print "\n"




