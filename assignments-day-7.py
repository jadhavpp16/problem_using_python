


##definition: a number that can be divided exactly only by itself and 1.
##conditions: num>1 and 1 and 0 are not prime numbers.



###Problem 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - -
###Write a program for checking whether a number is a prime number or not


###----------------------------------------------------------------------------------
###Prime number using functions

#Code
##def prime(n):
##    for i in range(2,n):
##        if (n%i) == 0:
##            return False
##        else:
##            return True
##        
##n=int(input("Enter a Number: "))
##
##if prime(n):
##    print("Yes it is a Prime Number")
##else:
##    print("No it is not a Prime Number")


#----------------------------------------------------------------------------------
#prime number using recursive method!


#Code
    
##def prime(n,r):
##    if n==r:
##        return True
##    elif n%r==0:
##        return False
##    else:
##        return prime(n,r+1)
##    
##n=int(input("Enter a Number: "))
##r=2
##
##if prime(n,r):
##    print("Yes it is a Prime Number")
##else:
##    print("No it is not a Prime Number")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - -


###Problem 2

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - -
###Write a program to find maximum of three numbers using functions

def mx(n, m, o):
 
    if (n>= m) and (n >= o):
        return n
    elif (m >= n) and (m >= o):
        return m
    else:
        return o

n=int(input("Enter a First Number: "))
m=int(input("Enter a Second Number: "))
o=int(input("Enter a Third Number: "))

print("Largest Number of all is ", mx(n,m,o))




