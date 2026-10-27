# I valori hanno un tipo. Le variabili no: una stessa variabile può cambiare tipo.

intero = 42
decimale = 3.5
testo = "ciao"
vero_o_falso = True

print(type(intero))
print(type(decimale))
print(type(testo))
print(type(vero_o_falso))

x = 10
print("x vale", x, "ed è di tipo", type(x))
x = "dieci"
print("ora x vale", x, "ed è di tipo", type(x))
