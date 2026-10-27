# ==========================================================
# 02. CIKLI UN ALGORITMISKĀ DOMĀŠANA — DARBA FAILS
# ==========================================================
# Šeit raksti savus risinājumus.
# Teorija, piemēri un atgādne: teorija.py
# Uzdevumu numuri iet cauri visam blokam.
# ==========================================================


# ----------------------------------------------------------
# 10-015 · Kāpēc vajadzīgi cikli
# ----------------------------------------------------------

# 1. Izvadi skaitļus no 1 līdz 20, katru jaunā rindā.

# for i in range(1,21):
#     print(i)


# 2. Izvadi tekstu Sveiks! piecas reizes.

# for i in range(5):
#     print("Sveiki!")


# 3. Izvadi skaitļus no 1 līdz 10 un blakus katram tā kvadrātu, formātā 3 -> 9.

# for i in range(1, 11):
#     print(i, "->",  i**2)


# 4. Izvadi visus pāra skaitļus no 1 līdz 30.

# for i in range(1, 31):
#     if i % 2 == 0:
#         print(i)


# 5. ★ Izvadi skaitļus no 1 līdz 50, bet tos, kas dalās ar 7, izvadi ar piezīmi
#    50 -> dalās ar 7.

# for i in range(1, 50):
#      if i % 7 == 0:
#           print(i, "-> dalās ar 7"):
#      else:
#           print(i)



# ----------------------------------------------------------
# 10-016 · range() ar robežām un soli
# ----------------------------------------------------------

# 6. Izvadi skaitļus no 10 līdz 20 ieskaitot.

for i in range(10, 20 + 1):
    print(i)


# 7. Izvadi skaitļus no 20 līdz 1 dilstošā secībā.

for i in range(20, 0, -1):
    print(i)
    


# 8. Izvadi katru trešo skaitli no 0 līdz 30.

for i in range(0, 31, 3):
    print(i)



# 9. Izvadi reizināšanas tabulu skaitlim 7 formātā 7 x 3 = 21.

for i in range(1, 11):
    print("7 x", i, "=", 7 * i)


# 10. Programma prasa skaitli n un izvada visus skaitļus no 1 līdz n.

n = int(input("Ievadi skaitli n: "))
for i in range(1, n + 1):
    print(i)



# 11. ★ Programma prasa divus skaitļus un izvada visus starp tiem — neatkarīgi no tā, kurš
#    ievadīts pirmais.

input1 = int(input("Ievadi pirmo skaitli: "))
input2 = int(input("Ievadi otro skaitli: "))

if input1 > input2:
    input1, input2 = input2, input1

for i in range(input1, input2 + 1):
    print(i)


# ----------------------------------------------------------
# 10-017 · Uzkrājējs: summa, reizinājums, skaitītājs
# ----------------------------------------------------------

# 12. Aprēķini un izvadi skaitļu summu no 1 līdz 100.

for i in range(1, 101):
    summa = 0
    summa += i 
    print(summa)


# 13. Programma prasa n un izvada n faktoriālu (visu skaitļu reizinājumu no 1 līdz n).

n = int(input("Ievadi skaitli n: "))
faktorials = 1
for i in range(1, n + 1):
    faktorials *= i
print(faktorials)


# 14. Programma prasa 5 skaitļus pēc kārtas un izvada to summu un vidējo aritmētisko.




# 15. Programma prasa skaitli un saskaita, cik tajā ir ciparu.




# 16. ★ Programma prasa skaitli un izvada tā ciparu summu (izmantojot % un // ciklā).




# 17. ★ Aprēķini summu 1/1 + 1/2 + 1/3 + … + 1/n un izvadi ar četriem cipariem aiz komata.





# ----------------------------------------------------------
# 10-018 · Praktikums: aprēķini ar for ciklu
# ----------------------------------------------------------

# 18. Krājkonts. Sākumā kontā ir 500 EUR, katru gadu pieaug par 3 %. Izvadi atlikumu pēc
#    katra gada 10 gadu garumā, ar diviem cipariem aiz komata.




# 19. Temperatūru vidējais. Programma prasa 7 dienu temperatūras un izvada vidējo, kā arī
#    cik dienās bija virs vidējā.




# 20. ★ Procentu tabula. Izvadi tabulu, kas rāda, cik gadu vajag, lai 1000 EUR dubultotos
#    pie 1 %, 3 % un 5 % likmes.





# ----------------------------------------------------------
# 10-019 · while cikls
# ----------------------------------------------------------

# 21. Izvadi skaitļus no 1 līdz 10, izmantojot while.




# 22. Programma sāk ar skaitli 100 un katrā solī dala to uz pusēm, līdz rezultāts ir mazāks
#    par 1. Izvadi katru soli.




# 23. Programma prasa skaitli un izvada, cik reizes to var izdalīt ar 2 bez atlikuma.




# 24. Programma skaita no 1 uz augšu, līdz summa pārsniedz 1000, un izvada, pie kura skaitļa
#    tas notika.




# 25. ★ Programma prasa skaitli un pārbauda, vai tas ir pirmskaitlis.





# ----------------------------------------------------------
# 10-020 · while ar lietotāja ievadi
# ----------------------------------------------------------

# 26. Programma prasa skaitli no 1 līdz 10 un atkārto pieprasījumu, līdz ievade ir derīga.




# 27. Programma prasa paroli, līdz tā ir pareiza, un skaita mēģinājumus.




# 28. Programma pieņem skaitļus, līdz lietotājs ievada 0, un tad izvada to summu.




# 29. Programma prasa vārdus, līdz ievadīts tukšs teksts, un izvada, cik vārdu ievadīti.




# 30. ★ Mini spēle: programma izdomā skaitli no 1 līdz 100 (random), lietotājs min, programma
#    saka par lielu vai par mazu un beigās izvada mēģinājumu skaitu.





# ----------------------------------------------------------
# 10-021 · break un continue
# ----------------------------------------------------------

# 31. Programma prasa 10 skaitļus, bet apstājas uzreiz, ja ievadīts negatīvs skaitlis.




# 32. Izvadi skaitļus no 1 līdz 50, izlaižot visus, kas dalās ar 3.




# 33. Programma meklē pirmo skaitli no 100 uz augšu, kas dalās gan ar 7, gan ar 11.




# 34. Programma prasa skaitļus, līdz ievadīts 0, un izvada lielāko no tiem.




# 35. ★ Pārraksti 33. uzdevumu bez break un salīdzini, kurš variants ir saprotamāks.





# ----------------------------------------------------------
# 10-022 · Ievades validācija ar ciklu
# ----------------------------------------------------------

# 36. Programma prasa vecumu un pieņem tikai skaitli no 1 līdz 120.




# 37. Programma prasa mēneša numuru un pieņem tikai 1–12, katrā kļūdas gadījumā paskaidrojot,
#    kas nav kārtībā.




# 38. Programma prasa atzīmi un pieņem tikai veselu skaitli no 1 līdz 10.




# 39. Papildini 10-018 18. uzdevumu (krājkonts) ar ievades validāciju: procentu likmei jābūt
#    no 0 līdz 20.




# 40. ★ Programma prasa datumu formātā DD.MM un pārbauda, vai diena un mēnesis ir iespējami.





# ----------------------------------------------------------
# 10-023 · Ligzdoti cikli
# ----------------------------------------------------------

# 41. Izvadi taisnstūri no zvaigznītēm 5 rindās un 8 kolonnās.




# 42. Izvadi trijstūri, kur pirmajā rindā ir viena zvaigznīte, otrajā divas utt. līdz 7.




# 43. Izvadi visu reizināšanas tabulu no 1 līdz 10 taisnā tabulā.




# 44. Izvadi apgrieztu trijstūri (pirmajā rindā 7 zvaigznītes, pēdējā — viena).




# 45. ★ Izvadi Paskāla trijstūra pirmās 6 rindas.




# 46. ★ Izvadi kvadrātu, kas iekšpusē ir tukšs — tikai maliņas no zvaigznītēm.





# ----------------------------------------------------------
# 10-024 · Blokshēmas un pseidokods
# ----------------------------------------------------------

# 47. Uzzīmē blokshēmu algoritmam, kas nosaka lielāko no trim skaitļiem.




# 48. Pieraksti pseidokodā algoritmu, kas saskaita, cik sarakstā ir pāra skaitļu.




# 49. Dota blokshēma (uz tāfeles). Uzraksti tai atbilstošu programmu.




# 50. Savai 10-020 30. uzdevuma spēlei uzzīmē blokshēmu.




# 51. ★ Uzzīmē blokshēmu algoritmam, kas pārbauda, vai skaitlis ir pirmskaitlis, un pieraksti,
#    kurā vietā tajā var pārtraukt meklēšanu ātrāk.





# ----------------------------------------------------------
# 10-025 · Klasiskie cikla algoritmi
# ----------------------------------------------------------

# 52. Programma prasa 8 skaitļus un izvada lielāko.




# 53. Programma prasa 8 skaitļus un izvada mazāko un tā kārtas numuru.




# 54. Programma prasa 10 atzīmes un saskaita, cik ir zemākas par 4.




# 55. Programma prasa skaitļus, līdz ievadīts 0, un izvada lielāko, mazāko un vidējo.




# 56. ★ Programma atrod lielāko un otro lielāko skaitli vienā ciklā.




# 57. ★ Fibonači virkne: izvadi pirmos 15 locekļus.





# ----------------------------------------------------------
# 10-026 · Praktikums: algoritmi ar cikliem
# ----------------------------------------------------------

# 58. Skaitļa apgriešana. Programma prasa skaitli un izvada to ar cipariem pretējā secībā
#    (piemēram, 1234 -> 4321).




# 59. Palindroms. Programma pārbauda, vai skaitlis lasās vienādi abos virzienos.




# 60. ★ Dalītāji. Programma prasa skaitli un izvada visus tā dalītājus, kā arī pasaka,
#    vai skaitlis ir pilnīgs (dalītāju summa bez paša skaitļa ir vienāda ar to).





# ----------------------------------------------------------
# 10-027 · Atkārtojums pirms pārbaudes darba
# ----------------------------------------------------------

# 61. Katrā programmā ir viena kļūda. Atrodi to, nepalaižot kodu:
#    summa = 0
#    for i in range(1, 10):
#        summa = i
#    print(summa)
#    n = 5
#    while n > 0:
#        print(n)
#    for i in range(1, 5):
#        for j in range(1, 5):
#            print("*")
#        print()




# 62. Pieraksti, ko izvadīs katra no trim programmām pēc izlabošanas.




# 63. ★ Uzraksti programmu, kas izvada to pašu, ko dotā programma, bet ar while for vietā.
