#2
#Write a program that gets a string from the user containing a potential telephone number. The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise. A phone number is considered valid as long as it is written in the form abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain only numbers and dashes, and the number of digits in each group must be correct.
#PhoneNumber = input("Enter the phone number: ")
#length = len(PhoneNumber)
#if length == 12 \
 #   and PhoneNumber[3] == PhoneNumber[7] == "-" \
  #  and PhoneNumber[:3].isdigit() \
   # and PhoneNumber[4:7].isdigit() \
    #and PhoneNumber[8:].isdigit() :
     #   print("Valid")
#elif length == 14 \
 #   and PhoneNumber[2:5].isdigit() \
  #  and PhoneNumber[6:9].isdigit() \
   # and PhoneNumber[10:14].isdigit() :
    #    print("Valid") 
#else :
 #   print("Invalid")

#3
#- Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000.
palindrome=[]
a=[x for x in range(100,1000) if str(x)==str(x)[::-1]]
print("The palindromic numbers are: ",a)


#4
#- Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]. Use a list comprehension to produce a list of the gaps between consecutive entries in L. Then find the maximum gap size and the percentage of gaps that have size 2.

