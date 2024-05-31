def sum_even_numbers(my_list):
    Sum=0
    for a in my_list:
       if a%2==0:
        Sum=Sum+a
    return Sum

my_list=[]
z=int(input("enter number of elements : "))
for i in range (1, z +1):
    y=int(input("enter integers in the list: "))
    my_list.append(y)

print(sum_even_numbers(my_list))