#create an array
myList=[]

#input the number of elements of the array from user
n = int(input("Enter number of elements: "))

#make the array
for i in range(0,n):
  a = int(input("Enter a number: "))
  myList.append(a)

#print original array
print(myList)

#bubble_sort starts
print("=============== start!! ===============")
for i in range(len(myList)):
    for j in range(len(myList)-1):
        if myList[j]>myList[j+1]:
            temp = myList[j+1]
            myList[j+1]=myList[j]
            myList[j]=temp
            print(myList)

#Print the result
print("=============== end!! =============== ")
print(myList)