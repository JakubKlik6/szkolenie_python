import numpy as np

# Ustal seed dla powtarzalności
np.random.seed(42)

# 1. Wygeneruj 10000 wartości polis (200-5000)
polisy = np.random.uniform(200,5000,10_000)

# 2. Statystyki
srednia = np.mean(polisy)# TODO
mediana = np.median(polisy)# TODO
std = np.std(polisy)# TODO
minimum = np.min(polisy)# TODO
maximum = np.max(polisy)# TODO

print(f"Średnia: {srednia:.2f} PLN")
print(f"Mediana: {mediana:.2f} PLN")
print(f"Odch. std: {std:.2f} PLN")
print(f"Min: {minimum:.2f} PLN")
print(f"Max: {maximum:.2f} PLN")

# 3. Polisy powyżej średniej
mask = polisy > np.mean(polisy)
powyzej_sredniej = polisy[mask]# TODO (liczba)
print(f"\nPolisy > średniej: {powyzej_sredniej}")

# 4. Przedziały (bez pętli!)
ponizej_1000 = polisy[polisy < 1000]# TODO
od_1000_do_2000 = polisy[(polisy > 1000) & (polisy < 2000)]# TODO
od_2000_do_3000 = polisy[(polisy > 2000) & (polisy < 3000)]# TODO
powyzej_3000 = polisy[polisy > 3000] # TODO

print(f"\n<1000: {ponizej_1000}")
print(f"1000-2000: {od_1000_do_2000}")
print(f"2000-3000: {od_2000_do_3000}")
print(f">3000: {powyzej_3000}")

# 5. Podwyżka 5%
polisy_podwyzszone = polisy * 1.05# TODO
print(f"\nNowa średnia po podwyżce: {np.mean(polisy_podwyzszone):.2f} PLN")