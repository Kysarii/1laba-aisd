#Вариант 16. Четные двоичные числа, не превышающие 819210, в которых встречается не более одной серии из трех подряд идущих нуля. Выводит на экран цифры числа, исключая нули. 
#Отдельно выводится прописью номер позиции, с которой начинается эта серия.
file = open('7.txt')
while True:
    a = file.readline().split()
    if not a:
        print('Файл закончился')
        break
    for num_str in a:
        if int(num_str) == int((bin(abs(int(num_str)))[2:])):
            num = int(num_str, 2)
        else:
            num = int(num_str)
        if num <= 8192 and num % 2 == 0:
            b = str(bin(abs(num))[2:])
            b = b.replace("000", "*")
            k = b.count("*")
            if k == 1:
                pos = b.find('*') + 1
                b = b.replace("*", "")
                print(b, pos)
