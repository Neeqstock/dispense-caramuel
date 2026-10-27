# Crea il nostro eroe da tastiera e stampa una scheda semplice.

nome = input("Come si chiama l'eroe? ")
vita = int(input("Quanti punti vita ha? "))  # input restituisce sempre testo: int lo trasforma in numero
forza = 5

print(f"L'eroe {nome} entra nel dungeon.")
print(f"Vita: {vita}, forza: {forza}")

vita_dopo_trappola = vita - 3
print("Dopo la trappola la vita è", vita_dopo_trappola)
print("Metà della forza:", forza / 2)
print("Metà della forza, senza decimali:", forza // 2)
print("Resto della divisione:", forza % 2)
