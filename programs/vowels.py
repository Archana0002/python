count=0
a="mar Athanasis colege of engineering"
s=a.lower()
vowels=['a','e','i','o','u']
out={}
for letter in vowels:
    out[letter]=a.count(letter)
print(out)
