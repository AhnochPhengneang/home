# Ex1 - String 
# Enter text and display it one by one
# text = input("Enter text: ")
# for cha in text :
#     print(cha)


# Ex2 - String
# Enter text and display number of letter

# text = input("Enter your text: ")
# for i in range(len(text)):
#     print(i)

# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter


# text = input("Enter Text : ")
# result = "No"
# for i in range(len(text)):
#     if text[i] == text[i].upper():
#         result = "Yes"
# print(result)
    

# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)

# text = input("Enter text: ")
# total = 0
# nospace = ""
# for i in range (len(text)) :
#     if text[i] == " " :
#         nospace += ""
#     else:
#         nospace += text[i]
#         total += int(text[i])
# print(int(nospace))
# print("Total:", total)


# text = "3 4 5 6"
# total = 0
# for char in text.replace(" ", ""):   function replace pi mean space mk ot space
#     print(char)
#     total += int(char)
# print(total)
 


# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 


# text = "454639"
# count_odd = 0
# count_even = 0
# for i in range(len(text)):
#     total = int(text[i])
#     if total % 2 == 0:
#         count_odd += 1
#     if total % 2 == 1:
#         count_even += 1
# print("Count of even :", count_even)
# print("Count of odd :", count_odd)
# print("sum all number:",count_even+count_odd)
# print("Reverse",text[::-1])


# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"

# input = int(input("enter number: "))
# if input % 2 == 1 :
#     print("Odd Number")
# else:
#     print("Even Number")  

# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20


# isfound = False
# while not isfound :
#     num = int(input("enter number: "))
#     if num >= 10 and num <= 20 :
#         print("Continue")
#     else:
#         isfound = True
# print("Out of range")
    

# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string

# input = "9394884039"
# count_8 = 0
# for cha in input :
#     if cha == "8" :
#         count_8 += 1
# print(count_8)

# Q2 - What is first index of letter 8

# input = "9394884039"
# isfound = False
# index = 0
# while not isfound :
#     if input[index] == "8" :
#         isfound = True
#         print(index)
#     index += 1


# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"

# text = input("Enter text: ")
# nospace = ""
# for cha in text :
#     if cha == " " :
#          nospace += ""
#     else:
#          nospace += cha
# print(nospace)

# Q2 - Multiple each letter by 2 result = "6 8 10 12"
# text = "3 4 5 6"
# total = ""
# for i in range(len(text)) :
#     if text[i] != " ":
#          total += str(int(text[i]) * 2) + " "
# print(total)

# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0

Max = 0
Min = 0
for i in range (5) :
    num = int(input("enter num: "))
    if num > Max:
        Max = num
    else:
        if num < Min :
            Min = num
print("Max", Max, "Min", Min)




