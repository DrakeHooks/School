# Chapter 2 Practice Problem 1
# Program: cookies.py
# Author: Drake Hooks
# Date: 9/15/20
# Purpose: Write a program that calculates the amoung of ingredients needed to make
# the amount of cookies inputed by the user.
# Notes: Amounts of ingredients provided is relative to making 48 cookies.
#     Ex. 1.5 cups of sugar makes 48 cookies 1.5/48 makes one cookie.

# Input Section
numCookies = int(input("Please enter the number of cookies you want to make: ")
) 
print() # skip line in console after inputting
# Processing Section
sugarPerCookie = 1.5/48
butterPerCookie = 1/48
flourPerCookie = 2.75/48

sugarNeeded = numCookies * sugarPerCookie
butterNeeded = numCookies * butterPerCookie
flourNeeded = numCookies * flourPerCookie

# Output Section
#print("Cups of sugar needed:", sugarNeeded)
#print("Cups of butter needed:",sugarNeeded)
#print("Cups of flour needed:", flourNeeded)

print("Cups of sugar needed:", format(sugarNeeded, ".3f"))
print("Cups of butter needed:",format(butterNeeded, ".3F"))
print("Cups of flour needed:", format(flourNeeded, ".3F"))

# End