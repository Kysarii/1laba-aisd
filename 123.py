f = open('7.txt')
a = [x.strip() for x in f]
if len(a)==0:
    print("Файл пустой")

for num_str in a:
    if all(c in '01' for c in num_str):
        num = int(num_str, 2)
    else:
        num = int(num_str)

    if (num <=8192 and num %2==0):
        b = str(bin(abs(num))[2:])
        b = b.replace("000", "*")
        k = b.count("*")
        if k ==1:
            pos = b.find('*') + 1
            b = b.replace("*", "")
            print(b, pos)