import sys
input = sys.stdin.readline

while True:
    s = list(input())
    s.remove(s[-1])
    if len(s) == 1 and s[0] == '.':
        break
    flag = 0
    stack_arr = []
    for i in s:
        if i == '(' or i == '[':
            stack_arr.append(i)
        elif i == ')':
            if not stack_arr or stack_arr[-1] == '[':
                flag = 1
                break
            elif stack_arr[-1] == '(':
                stack_arr.pop()
        elif i == ']':
            if not stack_arr or stack_arr[-1] == '(':
                flag = 1
                break
            elif stack_arr[-1] == '[':
                stack_arr.pop()
        
    if flag == 0 and not stack_arr:
        print("YES")
    else:
        print("NO")