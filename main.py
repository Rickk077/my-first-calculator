num1 = float(input("digite um numero\n"))
num2 = float(input("digite outro numero\n"))
act = str(input("digite a acão Adiçao(a) Subtraçao(s) Multiplicação(m) Divisão(d)\n")).lower()

if act == "a":
    print(num1+num2)
elif act == "s":
    print(num1-num2)
elif act == "m":
    print(num1*num2)
elif act == "d":
    if num2 == 0:
        print ("divisao por zero e impossivel")
    else:
        print(num1/num2)
else:
    print("ação invalida")