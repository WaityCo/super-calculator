while True:
    print("========================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("========================")

    print("")
    user_input = int(input("Ingresa tu opción aqui => "))

    if user_input == 1:
        print("========================================")
        print("")
        num1_suma = int(input("Ingresa el primero numero: "))
        num2_suma = int(input("Ingrese el segundo numero: "))
        print("========================================")

        def suma(num1_suma, num2_suma):
            return num1_suma + num2_suma

        resultado_suma = suma(num1_suma, num2_suma)
        print("")
        print(resultado_suma)
        print("")

    elif user_input == 3:
        print("========================================")
        print("")
        num1_multiplicar = int(input("Ingrese el primer numero "))
        num2_multiplicar = int(input("Ingrese el segundo numero "))

        def multiplicar(num1_multiplicar, )
