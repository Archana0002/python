'''a="aaaiieeouAEAIOUoiuii"
a=a.lower()
print(a)
out=dict()
vowels=['a','e','i','o','u']
for letter in a:
    if letter in vowels:
        out[letter]=out.get(letter,0)+1
    
print(out)
final=dict()
aj="ajmal"
for vowel in vowels:
    final[vowel]=aj.count(vowel)
print(final)

    
'''

a = "aaaeeeioiuuuiouIOUU"
a=a.lower()
out={}
vowels=["a","e","i","o","u"]
for letter in a:
    if letter in vowels:
        out[letter]=out.get(letter,0)+1
print(out)