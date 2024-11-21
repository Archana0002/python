
s="apple Orange Apple orange OrAnGe Lemon"
s=s.lower()
fruits=s.split()
output={}
for fruit in fruits:
    output[fruit]=output.get(fruit,0)+1
print(output)

# Sort the dictionary by value in ascending order and store as a list of tuples
sorted_fruits_asc = sorted(output.items(), key=lambda x: x[1])
print("Ascending Order:", sorted_fruits_asc)
temp=[k for k,v in sorted_fruits_asc]

print(temp)
# Sort the dictionary by value in descending order and store as a list of tuples
sorted_fruits_desc = sorted(output.items(), key=lambda x: x[1], reverse=True)
print("Descending Order:", sorted_fruits_desc)
