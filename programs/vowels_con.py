a="hdvfbDSAIjeiowaaaao"
a=a.lower()
count = 0
count1 = 0
print(a)
vowels=['a','e','i','o','u']
# if vowels in a:
#     count = count + 1
print(count)
if('a' in a):
    print("afound")

for i in range(len(a)):
    if a[i] in vowels:
        count = count + 1
    else:
        count1 = count1 + 1
print(count)
print(count1)