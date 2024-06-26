def remove_p(s):
    res = ""
    j = 0
    for i in range(len(s)):
        if s[i] == '(':
            if j > 0:
                res += s[i]
            j += 1
        elif s[i] == ')':
            j -= 1
            if j > 0:
                res += s[i]
    return res

if __name__ == "__main__":
    s = "(()())(())"
    ans = remove_p(s)
    for char in ans:
        print(char, end="")
