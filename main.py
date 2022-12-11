with open('input.txt', mode='r', encoding='UTF-8') as code:
    lining = code.readline()

answer = 0
pointer = []
for char in lining:
    pointer.append(char)
    answer += 1
    if len(pointer) > 13:
        if len(set(pointer)) == 14:
            print(answer)
            break
        pointer.pop(0)
