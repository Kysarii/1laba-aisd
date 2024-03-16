#Вариант 16. Четные двоичные числа, не превышающие 819210, в которых встречается не более одной серии из трех подряд идущих нуля. Выводит на экран цифры числа, исключая нули. 
#Отдельно выводится прописью номер позиции, с которой начинается эта серия.
file = open('7.txt')
while True:
    a = file.readline().split()
    if not a:
        print('Файл закончился')
        break
    for num in a:
        if all('0'<= num_str <= '1' for num_str in num):
            if int(num) <= 8192 and int(num) % 2 == 0:
                b = str(bin(abs(int(num)))[2:])
                b = b.replace("000", "*")
                k = b.count("*")
                if k == 1:
                    pos = b.find('*') + 1
                    b = b.replace("*", "")
                    print("Число исключая серию 000:", b)
                    print("Номер позиции ", pos)
        else:
            print('Неверный формат числа')
