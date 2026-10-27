# ============================================================
# 02. BLOKS — CIKLI UN ALGORITMISKĀ DOMĀŠANA
# ============================================================
# Cikls ļauj atkārtot darbības, nerakstot vienu un to pašu kodu
# vairākas reizes. Divi cikla veidi:
#
#   for   — zinām, cik reižu jāatkārto
#   while — atkārtojam, kamēr izpildās nosacījums
# ============================================================


# ============================================================
# 1. for CIKLS UN range()                              [10-015]
# ============================================================
# range(5) dod skaitļus 0, 1, 2, 3, 4 — PIECI skaitļi, bet
# pēdējais ir 4, nevis 5. Šī ir visbiežākā kļūda visā blokā.

# for i in range(5):
#     print(i)

# Cikla mainīgais i eksistē tikai cikla laikā un katrā solī maina vērtību.
# Ja pati vērtība nav vajadzīga, to var neizmantot:

# for i in range(3):
#     print("Sveiks!")


# ============================================================
# 2. range() AR ROBEŽĀM UN SOLI                        [10-016]
# ============================================================
#   range(beigas)                 0 .. beigas-1
#   range(sakums, beigas)         sakums .. beigas-1
#   range(sakums, beigas, solis)  ar soli

for i in range(1, 11):        # 1 .. 10
    print(i)

# for i in range(0, 21, 5):     # 0, 5, 10, 15, 20
#     print(i)

# for i in range(10, 0, -1):    # 10, 9, 8 ... 1  (atpakaļgaitā)
#     print(i)

# Ja gribam skaitļus LĪDZ n IESKAITOT, jāraksta range(1, n + 1):
# n = 7
# for i in range(1, n + 1):
#     print(i)


# ============================================================
# 3. UZKRĀJĒJS                                         [10-017]
# ============================================================
# Uzkrājējs ir mainīgais, kas krāj rezultātu pa daļām.
# Tas jāizveido PIRMS cikla — ja to izveido ciklā, tas katrā solī
# atgriežas sākumstāvoklī un rezultāts ir nepareizs.

# summa = 0                     # sākumvērtība summai ir 0
# for i in range(1, 101):
#     summa = summa + i         # var rakstīt arī:  summa += i
# print(summa)                  # 5050

# reizinajums = 1               # reizinājumam sākumvērtība ir 1, ne 0!
# for i in range(1, 6):
#     reizinajums *= i
# print(reizinajums)            # 120

# skaits = 0                    # skaitītājs — cik reižu kaut kas notika
# for i in range(1, 51):
#     if i % 7 == 0:
#         skaits += 1
# print(skaits)


# ============================================================
# 4. while CIKLS                                       [10-019]
# ============================================================
# while atkārto, KAMĒR nosacījums ir True.
# Ciklā OBLIGĀTI jābūt kaut kam, kas nosacījumu galu galā padara par False,
# citādi cikls nekad nebeidzas (bezgalīgs cikls, Ctrl+C to aptur).

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1          # <- bez šīs rindas cikls nekad nebeigtos
# print("Starts!")

# while der tur, kur iepriekš NEZINĀM soļu skaitu:
# skaitlis = 1000
# solis = 0
# while skaitlis > 1:
#     skaitlis = skaitlis / 2
#     solis += 1
# print(solis)


# ============================================================
# 5. while AR LIETOTĀJA IEVADI                         [10-020]
# ============================================================
# Tipisks veids, kā pieprasīt ievadi, līdz tā ir derīga:

# vecums = int(input("Ievadi vecumu (1-120): "))
# while vecums < 1 or vecums > 120:
#     print("Tāds vecums nav iespējams. Mēģini vēlreiz.")
#     vecums = int(input("Ievadi vecumu (1-120): "))
# print(f"Paldies! Tavs vecums: {vecums}")

# Sentinel vērtība — īpaša vērtība, kas nozīmē "beidz":
# summa = 0
# skaitlis = int(input("Ievadi skaitli (0 = beigt): "))
# while skaitlis != 0:
#     summa += skaitlis
#     skaitlis = int(input("Ievadi skaitli (0 = beigt): "))
# print(f"Summa: {summa}")


# ============================================================
# 6. break UN continue                                 [10-021]
# ============================================================
#   break     — pārtrauc ciklu pavisam
#   continue  — izlaiž atlikušo soli un iet uz nākamo

# for i in range(1, 101):
#     if i % 7 == 0 and i % 11 == 0:
#         print(f"Atradu: {i}")
#         break                  # atradām, nav jēgas meklēt tālāk

# for i in range(1, 21):
#     if i % 3 == 0:
#         continue               # trijniekus izlaižam
#     print(i)

# Piezīme: gandrīz vienmēr to pašu var uzrakstīt arī bez break un continue.
# Izvēlies to variantu, kurš ir vieglāk lasāms.


# ============================================================
# 7. LIGZDOTI CIKLI                                    [10-023]
# ============================================================
# Cikls cikla iekšpusē. Iekšējais cikls izpildās PILNĪBĀ katrā
# ārējā cikla solī. Ja ārējais iet 5 reizes un iekšējais 8, tad
# iekšējā cikla ķermenis izpildās 5 * 8 = 40 reizes.

# for rinda in range(5):
#     for kolonna in range(8):
#         print("*", end="")     # end="" nozīmē: neej jaunā rindā
#     print()                    # tukšs print() pāriet jaunā rindā

# Trijstūris — iekšējā cikla garums atkarīgs no ārējā mainīgā:
# for rinda in range(1, 8):
#     for kolonna in range(rinda):
#         print("*", end="")
#     print()

# Reizināšanas tabula:
# for a in range(1, 11):
#     for b in range(1, 11):
#         print(f"{a * b:4}", end="")   # :4 atvēl skaitlim 4 zīmes
#     print()


# ============================================================
# 8. KLASISKIE ALGORITMI                               [10-025]
# ============================================================
# Lielākā meklēšana: pieņemam, ka pirmais ir lielākais, un
# pārbaudām pārējos. Sākumvērtības izvēle ir bīstamā vieta —
# ja sāktu ar 0, tad negatīvu skaitļu virknē atbilde būtu nepareiza.

# skaitli = [4, 17, 3, 42, 8]
# lielakais = skaitli[0]
# for skaitlis in skaitli:
#     if skaitlis > lielakais:
#         lielakais = skaitlis
# print(lielakais)

# Skaitīšana pēc pazīmes:
# atzimes = [7, 3, 9, 2, 8, 5]
# vaji = 0
# for atzime in atzimes:
#     if atzime < 4:
#         vaji += 1
# print(vaji)

# Cik darbību veic šis algoritms, ja skaitļu ir n?
# Katrs skaitlis tiek apskatīts vienu reizi -> n darbību.
# Bet ligzdotā ciklā tas jau būtu n * n. Pie n = 1000 tā ir
# starpība starp 1000 un 1 000 000 darbībām.
