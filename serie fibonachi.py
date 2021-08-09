def fibonacci(n):
    if n == 0:
        serie_fibonacci = []
    elif n == 1:
        serie_fibonacci = [1]
    elif n == 2:
        serie_fibonacci = [0, 1]
    elif n > 2:
        serie_fibonacci = [0, 1]
        i = 1

        while i < n - 1:
            serie_fibonacci.append(serie_fibonacci[i] + serie_fibonacci[i - 1])
            i += 1
    
    return serie_fibonacci

def main():
  print("Lab7 Ejercicio3")
  xx= int(input("cuantos numeros de la serie quiere: "))
  resultado = fibonacci(xx)
  print(resultado)

main()
