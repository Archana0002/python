a = ["apple","orange","apple","mango","mango"]
out = {}
for i in a:
    out[i]=out.get(i,0)+1
print(out)