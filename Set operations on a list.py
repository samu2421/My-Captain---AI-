#Set operations on a list

print("Enter no's in set E : ")       #Enter nos using space
E = list(input().split())

print("Enter no's in set N : ")       #Enter nos using space
N = list(input().split())
    
A = list (set(E) | set(N))
B = list (set(E) & set(N))
C = list (set(E) - set(N))
D = list (set(E) ^ set(N))


print ("Union of set E and N is : \n",A) 
print ("\nIntersection of set E and N is : \n",B)
print ("\nDifference of set E and N is : \n",C) 
print ("\nSymmetric difference of set E and N is : \n",D) 


 