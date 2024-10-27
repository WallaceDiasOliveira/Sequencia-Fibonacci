n = int(input('Digite quantos números deseja visualizar na sequência: '))
a = 1
b = k = 0
while k <= n:
    k += 1
    c = a + b
    a = b
    b = c
    print(c, end=' ')