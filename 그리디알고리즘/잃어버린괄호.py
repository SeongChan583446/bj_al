import sys
input = sys.stdin.readline

input_txt = input()
res_arr = []
exp_arith = input_txt[:-1]
exp = exp_arith.split('-')


for i in exp:
    tmp_res = 0
    tmp_arr = i.split('+')
    for j in tmp_arr:
        tmp_res += int(j)
    res_arr.append(tmp_res)

res = res_arr[0]
for i in range(1,len(res_arr)):
    res -= res_arr[i]

print(res)