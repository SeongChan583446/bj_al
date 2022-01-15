import sys
input = sys.stdin.readline

n = int(input())
count = 1
stack_arr = []
res_arr = []
flag = True
for i in range(n):
    input_num = int(input())
    while count <= input_num:
        stack_arr.append(count)
        res_arr.append('+')
        count += 1
    if stack_arr[-1] == input_num:
        stack_arr.pop()
        res_arr.append('-')
    else:
        flag = False
      
if flag == False:
    print("NO")
else:
    for i in res_arr:
        print(i)