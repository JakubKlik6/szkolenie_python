import numpy as np

# 1. Stwórz tablicę 4x6 z liczbami 1-24
arr = np.arange(24).reshape(4,6)

# 2. Wyświetl atrybuty
print(f"Kształt: {arr.ndim}")
print(f"Wymiary: {arr.shape}")
print(f"Typ: {arr.dtype}")

# 3. Trzeci wiersz (indeks 2)
trzeci_wiersz = arr[2]# TODO
print(f"Trzeci wiersz: {trzeci_wiersz}")

# 4. Druga kolumna (indeks 1)
druga_kolumna = arr[:,1]# TODO
print(f"Druga kolumna: {druga_kolumna}")

# 5. Wycinek 2x2 ze środka
srodek = arr[0:2,1:3]# TODO
print(f"Środek:\n{srodek}")

# 6. Elementy > 12
mask = arr > 12
wieksze = arr[mask]# TODO
print(f"Elementy > 12: {wieksze}")