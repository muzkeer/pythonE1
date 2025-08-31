###slicing 
# x = "hello"
# print(x[0:4])


###reversing 
# x = "hello"
# print(x[::-1])


###Reverse a String
# x = str(input("enter a string"))
# empty = ""
# for a in x:
#     empty = a + empty
# print(empty)


###Count Vowels in a String
# a = str(input("enter a string :"))
# b = a.lower()
# count = 0
# for i in b:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         count = count+1
# print(count)
       

###Check for Palindrome
# x = str(input("enter a string"))
# empty = ""
# for a in x:
#     empty = a + empty
# if empty == x:
#     print("palindrome")
# else:
#     print("not")


###Replace All Spaces with Hyphens
# x = str(input("enter a string"))
# a = x.replace(" " ,"-")
# print(a)


###Count Occurrence of Each Character
x = str(input("enter a string:"))
empty = ""
for i in x:
    if i not in empty:
        count = 0
        for a in x:
            if a == i:
                count = count + 1 
                print(f"{a}:{count}")
            empty = empty + i



    