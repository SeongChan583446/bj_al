arr_x = []
arr_y = []
for i in range(3):
    x,y = map(int, input().split(' '))
    arr_x.append(x)
    arr_y.append(y)

answer_x = 0
answer_y = 0
if arr_x[0] == arr_x[1]:
    answer_x = arr_x[2]
elif arr_x[0] == arr_x[2]:
    answer_x = arr_x[1]
else:
    answer_x = arr_x[0]

if arr_y[0] == arr_y[1]:
    answer_y = arr_y[2]
elif arr_y[0] == arr_y[2]:
    answer_y = arr_y[1]
else:
    answer_y = arr_y[0]

print(answer_x,answer_y)