# %% Ejercicio 122: Tokenizando una Cadena.
def tokenList(s):
    # remover todos los espacios en la cadena s
    s = s.replace(" ", "")
    # despues se elaborara un ciclo para identificar los tokens en la cadena y
    # añadirlos a la lista
    token = []
    i = 0
    while i < len(s):
        # Manejar los tokens que son siempre de un único caracter: *,/,^,( and )
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or s[i] == "(" or s[i] == ")":
            token.append(s[i])
            i = i+1
    # para el caso de + y -
        elif s[i] == "+" or s[i] == "-":
            # si hay un caracter previo que es un numero o un bracket
            # entonces el + o - is un token en si mismo
            if i > 0 and (s[i-1] >= "0" and s[i-1] <= "9" or s[i-1] == ")"):
                token.append(s[i])
                i = i+1
            else:
                # el + o - es parte de un numero
                num = s[i]
                i = i+1
                # estar añadiendo caracteres al token tanto como sean digitos
                while i < len(s) and s[i] >= "0" and s[i] <= "9":
                    num = num+s[i]
                    i = i+1
                token.append(num)
        # manejar numeros sin un lider + o -
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            # estar añadiendo caracteres al token tanto como sean digitos
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num+s[i]
                i = i+1
            token.append(num)
        else:
            return []
    return token


# leer la expresion ingresada por el usuario y tokenizarla
def tokenizar():
    exp = input("Ingrese una expresion matematica : ")
    token = tokenList(exp)
    print("Los tokens son: ", token)


# llamar la funcion unicamente si el archivo no ha sido importado
if __name__ == "__main__":
    tokenizar()
