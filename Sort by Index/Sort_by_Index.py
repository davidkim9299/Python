#create an array
person=[]

#input the number of elements of the array from user
n = int(input("Enter number of elements: "))

#make the array
for i in range(0,n):
  a = (input("Enter information (First name, Last name, Phone #): ").split(","))
  person.append(a)

#print contact ordered by first name
list_Fname = sorted(person, key=lambda user:user[0])
print(list_Fname)
print("")

#Print contact ordered by last name
list_Lname = sorted(person, key=lambda user:user[1])
print(list_Lname)
print("")

#print contact ordered by phone number
list_phonenum = sorted(person, key=lambda user:user[2])
print(list_phonenum)
print("")



