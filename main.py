# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#leap_year = year % 4 == 0
if year % 4 !=0:
  print("Not a leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
  print("Not a leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
  print("Leap year.")
elif year % 4 == 0 and year % 100 == 0:
  print("Not leap year.")
else:
  print("Leap year.")

# realizing I did some wild shit here but it seems to work....
# this is cleaner --> -> -->

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")






