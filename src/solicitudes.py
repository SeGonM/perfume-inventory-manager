def solicitar_entero(prompt, min_val=None):
    while True:
        valor = input(prompt)
        try:
            numero = int(valor)
            if min_val is not None and numero < min_val:
                raise ValueError
            return numero
        except ValueError:
            if min_val is not None:
                print(f"Entrada inválida. Ingrese un número entero mayor o igual a {min_val}.")
            else:
                print("Entrada inválida. Ingrese un número entero válido.")


def solicitar_flotante(prompt, min_val=None):
    while True:
        valor = input(prompt)
        try:
            numero = float(valor)
            if min_val is not None and numero < min_val:
                raise ValueError
            return numero
        except ValueError:
            if min_val is not None:
                print(f"Entrada inválida. Ingrese un número válido mayor o igual a {min_val}.")
            else:
                print("Entrada inválida. Ingrese un número válido.")


def solicitar_texto(prompt):
    while True:
        texto = input(prompt).strip()
        if texto:
            return texto
        print("Entrada inválida. Por favor, ingrese un texto no vacío.")