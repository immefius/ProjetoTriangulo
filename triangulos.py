lado1=float (input("Informe o primeiro lado: "))
lado2=float (input("Informe o segundo lado: "))
lado3=float (input("Informe o terceiro lado: "))

if (lado1 + lado2) < lado3 or (lado1 + lado3) < lado2 or (lado2 + lado3) < lado1:
  print ("Não é um triângulo")
elif lado1 == lado2 and lado1 == lado3:
  print("Este triângulo é Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print("Este triângulo é Isósceles")
else:
  print("Este triângulo é Escaleno")