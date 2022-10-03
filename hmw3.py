#1

string = ""
for i in range(4):
    num = str(input("Please input number: "))
    string+=num+"+"
num5 = str(input("Please input number: "))
print(string+num5)

#2

PhoneNumber = input("Enter the phone number: ")
length = len(str(PhoneNumber))
if length == 12 and PhoneNumber[3] == PhoneNumber[7] == "-" and PhoneNumber[:3].isdigit() and PhoneNumber[4:7].isdigit() and PhoneNumber[8:].isdigit() :
        print("Valid")
elif length == 14 and PhoneNumber[1] == PhoneNumber[5] == PhoneNumber[9] == "-" and PhoneNumber[0] == '1' and PhoneNumber[2:5].isdigit() and PhoneNumber[6:9].isdigit() and PhoneNumber[10:14].isdigit() :
        print("Valid")
else :
   print("Invalid")

#3

palindrome=[]
a=[x for x in range(100,1000) if str(x)==str(x)[::-1]]
print("The palindromic numbers are: ",a)


#4
L = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
Gaps = []
for i in range (1,15):
    gap=[L[i]-L[i-1]]
    Gaps.append(gap)
print(Gaps)
print("Max gap is:", max(Gaps))
counter = 0
for m in Gaps:
    if m == [2]:
        counter+=1
percentage = counter / len(Gaps)*100
print("The percentage of 2 in Gaps is:" ,percentage ,"%")

#5
num = int(input("Enter the n6umber of products: "))
Products ={}

for i in range (num):
  name = input("Enter product name: ")
  Products [name]  = input("Product price: ")

name1 = input("Enter a product name you search: ")
if name1 in Products:
  print("The price of", name1, "is", Products[name])
else: 
  print("No such product")
  
#6
di = [{'name':'Todd', 'phone':'555-1414', 'email':'mailto:todd@mail.net'}, {'name':'Helga', 'phone':'555-1618', 'email':'mailto:helga@mail.net'}, {'name':'Princess', 'phone':'555-3141', 'email':''}, {'name':'LJ', 'phone':'555-2718', 'email':'mailto:lj@mail.net'}]
print('Users whose phone number ends in an 8 are:')
i=0
for a in di:
    n=di[i]['phone']
    if n[-1]=='8':
        print(di[i])
    i=i+1

print("Users who don't have email addresses are: ")
i=0
for a in di:
    n=di[i]['email']
    if len(n)==0:
        print(di[i])
    i=i+1
    
    
 #7
import random 
raw = 5 
matrix = [[random.randint(1, 5) for i in range(raw)] for j in range(raw)] 
  
myset = set() 
for i in range(raw): 
     for j in range(raw): 
         myset.add(matrix[i][j]) 
mydict = {} 
for mykey in myset: 
     count = 0 
     for i in range(raw): 
         for j in range(raw): 
             if mykey == matrix[i][j]: 
                 count += 1 
     mydict[mykey] = count 
print("This is how many times the numbers occur:") 
print(mydict) 
  
ls_values = list(mydict.values()) 
ls_values.sort() 
ls_values = ls_values[-3:] 
print("Most common numbers are:") 
for i in ls_values: 
     for j in mydict.keys(): 
         if mydict[j] == i: 
             print(str(j) + " : " + str(mydict[j]))

