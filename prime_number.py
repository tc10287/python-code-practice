def prime_number(num):
    if num==1:
        return(print("1 is not considered"))
    for i in range(2,num):                  #logic behind prime number, prime number is a number who can only be divided by the number itself
        if num%i==0:
            return(print("%d is not a prime number"%num))
    return(print("%d is a prime number"%num))

prime_number(2)
prime_number(23)
prime_number(235)

