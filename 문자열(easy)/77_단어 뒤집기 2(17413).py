# 다시 천천히 해보기
import sys

sentence = list(map(str, sys.stdin.readline().rstrip()))
# ['baekjoon', 'online', 'judge']
# ['<open>tag<close>']
print(sentence)

result = list()
arrow = False
tword = list()

for i in range(len(sentence)):
    # print(sentence[i])
    print('result : ' , result)
    print('sentence : ' , sentence[i])
    if sentence[i] == '<':
        if len(result) != 0:
            print('ues')
            word = ''
            new = list()            
            tmp = list()
            for z in range(len(tword)):
                if tword[z] == ' ':
                    # new.append(tmp[::-1])
                    for i in tmp:
                        new.append(i)
                    new.append(' ')
                    tmp = []
                else:
                    tmp.insert(0, tword[z])
                # new.insert(0, tword[z])
                # result.append(tword[z])
            if tmp:
                for i in tmp:
                    new.append(i)
            print('new!! ' ,new)
            for k in new :
                result.append(k)
        arrow = True
    elif sentence[i] == '>':
        result.append(sentence[i])
        arrow = False
        continue

    if arrow == True:
        result.append(sentence[i])
        # if sentence[i] != ' ': 
        #     tword.insert(0, sentence[i])
        # elif sentence[i] == ' ':
        #     print(tword)
        #     for z in range(len(tword)):
        #         result.append(tword[z])
        #     result.append(' ')
        #     tword = list()
            
                # tword = list()

    # print(tword)
    print(result)

for i in result:
    print(i, end='')