# Task 01.
# Working with memory variables.

# string memvar
print( "String MemVar" )

name = input("Enter your name: ")
place = input("Enter your place: ")

print("name: ", name)
print(type(name))
print("place: ", place)
print(type(place))

print("\n---------------------------------------------------\n")
# integer memvar
print( "Integer MemVar" )

int_num_1 = int(input("Enter first integer number: "))
int_num_2 = int(input("Enter second integer number: "))

print("first integer number: ", int_num_1)
print(type(int_num_1))
print("second integer number: ", int_num_2)
print(type(int_num_2))

print("\n---------------------------------------------------\n")
# float memvar
print( "Float MemVar" )

flt_num_1 = float(input("Enter first float number: "))
flt_num_2 = float(input("Enter second float number: "))

print("first float number: ", flt_num_1)
print(type(flt_num_1))
print("second float number: ", flt_num_2)
print(type(flt_num_2))

print("\n---------------------------------------------------\n")
# bulean memvar
print( "Boolean MemVar" )

vb_True = bool(input("Enter True: "))
vb_False = bool(input("Enter False: "))

print("Boolean True: ", vb_True)
print(type(vb_True))
print("Booleam False: ", vb_False)
print(type(vb_False))