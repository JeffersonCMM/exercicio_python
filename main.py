num = float(input("Qual é a sua idade? "))

if num < 12:
    print("Você é uma criança")
elif 12 <= num < 18:
    print("Você é um adolescente")
elif 18 <= num < 60:
    print("Você é um adulto")
else:
    print("Você é um idoso")


