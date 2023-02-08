#Fibonacci numbers
'''
import math              
 
def fibo(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))
       
if __name__ == '__main__':
     
    n = int(input("Enter the no. of terms : "))
     
    print(fibo(n))

OR 

'''

no_of_terms = (int(input ("Enter no of terms : ")))
  
n1 = 0  
n2 = 1  
count = 0  
  
if no_of_terms <= 0:  
    print (f"Enter a positive integer. ")  

elif no_of_terms == 1:  
    print (f"The Fibonacci sequence up to {no_of_terms} is : ")  
    print(n1)  

else:  
    print (f"The fibonacci sequence of the numbers up to {no_of_terms} is : ")  
    while count < no_of_terms:  
        print(n1)  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count += 1  
        
        
