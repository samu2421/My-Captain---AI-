#printing positive numbers in the list

print("Enter the no's:")            #Enter numbers seperated by whitespace
n = list(input().split())
print("Entered list is : ", n)

output_list = []

for i in n:
    if int(i) > 0:
        output_list.append(int(i))
        
print("Positive numbers from given list are : ", output_list)

