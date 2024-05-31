def find_first_occurence(my_list, num):
   if num in my_list:
       
       for i in range(len(my_list)):
           if my_list[i]==num:
               return i
           else:
               return None
           
my_list=[] 
z=int(input("Enter the number of elements: "))
for i in range(1,z+1):
    a=int(input("enter the integers: "))
    my_list.append(a) 
num=int(input("enter the num: "))
print(find_first_occurence(my_list,num))
    
         
               