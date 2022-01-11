import sys
input = sys.stdin.readline

n = int(input())
input_arr = []
stack_arr = []
res_arr = []
for i in range(n):
    input_arr.append(int(input()))

i = 1
index = 0
flag = True
while index != n:
    if i == 9 and len(stack_arr) == 0:
        flag = True
        break
    if len(stack_arr) == 0:
        stack_arr.append(i)
        res_arr.append('+')
        i += 1
    elif stack_arr[-1] < input_arr[index]:
        stack_arr.append(i)
        res_arr.append('+')
        i += 1
    elif stack_arr[-1] == input_arr[index]:
        stack_arr.pop()
        res_arr.append('-')
        index += 1
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for i in res_arr:
        print(i)