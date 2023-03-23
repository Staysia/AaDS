print("введите k:", end=" ")
k = int(input())
buffer = ''
num = ''
kol_1 = 0
kol_2 = 0
slovar = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь'}
with open("text.txt",'r') as f:
    buffer = f.readline(1)
    if not buffer:
        print("файл пустой")
        kol_1 += 1
    while buffer:
        while buffer:
            if buffer != ' ':
                num = num + buffer
            else:
                break
            buffer = f.readline(1)
        if (int(num,8) <= 4096) and (int(num,8) % 2 != 0) and (len(num) % 2 == 1) and (len(num) > k):
                print(num, end=' ')
                kol_2 += 1
        num = ''
        buffer = f.read(1)
    if kol_2 == 0:
        print("чисел не найдено")
print('')
