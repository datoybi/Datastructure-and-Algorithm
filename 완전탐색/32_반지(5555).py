'''
    

'''
# str, N = input(), int(input())
# str_lst = list()

# for i in range(3):
#     str_lst.append([input()])

str, N = 'ABCD', 3
flag = False 
str_lst = [['ABCDXXXXXX'], ['YYYYABCDXX'], ['DCBAZZZZZZ']]

# print(str_lst[0])
for i in range(0,11):
    tmp = str_lst[0][0]
    j = i+len(str)
    print('i : ' , i , ' j : ' , j)

    if j <= len(str_lst[0][0]):
        print(tmp[i:j])

    elif j > len(str_lst[0][0]):
        s = j-len(str_lst[0][0])
        print('s : ' , s)
        print('hap : ' , tmp[i:j] , ' , ' ,  tmp[0:s])
        # if s == len(str):
        #     break

        if tmp[0:s] == str:
            break

    # print(tmp[i:j])
    # print(tmp)