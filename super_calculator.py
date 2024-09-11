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

    elif user_input == 2:
        
        num1_resta = int(input("ingresa el primer numero "))
        num2_resta = int(input("ingresa el segundo numero "))

        def resta(num1_resta, num2_resta):
            return num1_resta - num2_resta
            
        resultado_resta = resta(num1_resta, num2_resta)

        print("")    
        print(resultado_resta)
        print("")

    elif user_input == 3:
        
        print("========================================")
        print("")
        num1_multiplicar = int(input("Ingrese el primer numero "))
        num2_multiplicar = int(input("Ingrese el segundo numero "))

        def multiplicar(num1_multiplicar, num2_multiplicar):
            return num1_multiplicar * num2_multiplicar
        
        resultado_multiplicar = multiplicar(num1_multiplicar, num2_multiplicar)

        print("")
        print(resultado_multiplicar)
        print("")
