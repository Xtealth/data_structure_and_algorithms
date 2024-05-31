def is_prime(y):
    if y==2 or y==3 or y==5 or y==7:
       return True
    elif  a%2!=0 and a%3!=0 and a%5!=0 and  a%7!=0:
        return True
    else:
        return False
    

a=int(input("enter a number: "))
print(is_prime(a))     