# 02. Cikli un algoritmiskā domāšana

**14 stundas (10-015 – 10-028)** · Standarta 1. un 3. temats

**Bloka mērķis:** izvēlēties un uzrakstīt uzdevumam atbilstošu ciklu, pierakstīt algoritmu
blokshēmā vai pseidokodā un realizēt to kodā.

**Teorija un piemēri:** [`teorija.py`](teorija.py) · **Darba fails:** [`uzdevumi.py`](uzdevumi.py)
**Pārbaudes darbi:** privātajā `sv-fv` repozitorijā
**Noslēgums:** pārbaudes darbs 10-028

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 02-cikli/README.md && python3 bin/darbafails.py 02-cikli -->

| Nr. | Tēma | Sasniedzamais rezultāts |
| --- | --- | --- |
| 10-015 | Cikla jēdziens. Cikls `for` un funkcija `range()`. | Uzraksta `for` ciklu, kas atkārto darbību noteiktu reižu skaitu. |
| 10-016 | Funkcijas `range()` parametri: sākums, beigas, solis. | Izmanto `range()` ar norādītām robežām un soli, lai iegūtu vajadzīgo skaitļu virkni. |
| 10-017 | Uzkrājēja mainīgais. Summas, reizinājuma un skaita aprēķināšana ciklā. | Lieto uzkrājēja mainīgo, lai ciklā aprēķinātu summu, reizinājumu vai elementu skaitu. |
| 10-018 | Praktikums: aprēķini ar `for` ciklu. | Patstāvīgi uzraksta programmu, kas ciklā apstrādā skaitļu virkni un izvada rezultātu. |
| 10-019 | Cikls `while`. Cikla nosacījums un tā pārbaude. | Uzraksta `while` ciklu un pamato, kāpēc konkrētam uzdevumam tas ir piemērotāks par `for`. |
| 10-020 | Cikls ar lietotāja ievadi. Ievades atkārtošana līdz derīgai vērtībai. | Uzraksta ciklu, kas atkārto ievades pieprasījumu, līdz lietotājs ievada derīgus datus. |
| 10-021 | Cikla pārtraukšana ar `break` un soļa izlaišana ar `continue`. | Lieto `break` un `continue`, lai vadītu cikla izpildi. |
| 10-022 | Datu validācija. Ievades pārbaude ciklā. | Uzraksta programmu, kas pārbauda ievades derīgumu un neļauj turpināt ar nederīgiem datiem. |
| 10-023 | Ligzdoti cikli. Divdimensiju rakstu un tabulu izvade. | Uzraksta ligzdotu ciklu, kas izvada dotu rakstu vai tabulu. |
| 10-024 | Algoritma shematiskais pieraksts: blokshēma un pseidokods. | Pieraksta algoritmu blokshēmā vai pseidokodā un realizē to kodā. |
| 10-025 | Minimuma, maksimuma un skaita meklēšana ciklā. | Realizē pamatalgoritmus — atrod lielāko, mazāko un saskaita elementus pēc pazīmes. |
| 10-026 | Praktikums: algoritmi ar cikliem. | Izvēlas uzdevumam piemērotu cikla veidu un realizē algoritmu patstāvīgi. |
| 10-027 | Cikli: atkārtojums. Biežākās kļūdas un to novēršana. | Atpazīst un izlabo tipiskās cikla kļūdas svešā kodā. |
| 10-028 | Pārbaudes darbs: cikli, uzkrājēji, ligzdoti cikli, algoritmi. | Demonstrē bloka sasniedzamos rezultātus patstāvīgā darbā. |

<!-- TABULA:BEIGAS -->

---

## 10-015 · Kāpēc vajadzīgi cikli
`prakse` · `teorija.py` §1

**Tēma:** Cikla jēdziens. Cikls `for` un funkcija `range()`.
**SR:** Uzraksta `for` ciklu, kas atkārto darbību noteiktu reižu skaitu.
**Standarts:** T.O.2.4.13. · T.Li.2.

**Gaita**
- 5' — uzraksti programmu, kas izvada skaitļus no 1 līdz 100. Cik ilgi tas prasīs?
- 10' — demo §1: `for i in range(10)`, cikla mainīgais, atkāpe
- 20' — uzdevumi
- 5' — kāpēc koda dublēšana ir problēma, arī ja tā strādā

**Uzdevumi**
1. Izvadi skaitļus no 1 līdz 20, katru jaunā rindā.
2. Izvadi tekstu `Sveiks!` piecas reizes.
3. Izvadi skaitļus no 1 līdz 10 un blakus katram tā kvadrātu, formātā `3 -> 9`.
4. Izvadi visus pāra skaitļus no 1 līdz 30.
5. ★ Izvadi skaitļus no 1 līdz 50, bet tos, kas dalās ar 7, izvadi ar piezīmi
   `50 -> dalās ar 7`.

**Mājasdarbs:** 3. uzdevums

## 10-016 · range() ar robežām un soli
`prakse` · `teorija.py` §2

**Tēma:** Funkcijas `range()` parametri: sākums, beigas, solis.
**SR:** Izmanto `range()` ar norādītām robežām un soli, lai iegūtu vajadzīgo skaitļu virkni.
**Standarts:** T.O.2.4.13.

**Gaita**
- 5' — atkārtojums: kāpēc `range(5)` beidzas ar 4
- 10' — demo §2: trīs `range()` formas, arī negatīvs solis
- 20' — uzdevumi
- 5' — biežākā kļūda: robeža par vienu par daudz vai par maz

**Uzdevumi**
6. Izvadi skaitļus no 10 līdz 20 ieskaitot.
7. Izvadi skaitļus no 20 līdz 1 dilstošā secībā.
8. Izvadi katru trešo skaitli no 0 līdz 30.
9. Izvadi reizināšanas tabulu skaitlim 7 formātā `7 x 3 = 21`.
10. Programma prasa skaitli `n` un izvada visus skaitļus no 1 līdz `n`.
11. ★ Programma prasa divus skaitļus un izvada visus starp tiem — neatkarīgi no tā, kurš
   ievadīts pirmais.

**Mājasdarbs:** 9. uzdevums

## 10-017 · Uzkrājējs: summa, reizinājums, skaitītājs
`prakse` · `teorija.py` §3

**Tēma:** Uzkrājēja mainīgais. Summas, reizinājuma un skaita aprēķināšana ciklā.
**SR:** Lieto uzkrājēja mainīgo, lai ciklā aprēķinātu summu, reizinājumu vai elementu skaitu.
**Standarts:** T.O.2.4.13.

**Gaita**
- 5' — kā saskaitīt 100 skaitļus, ja atmiņā drīkst turēt tikai vienu
- 10' — demo §3: uzkrājēja sākumvērtība (0 summai, 1 reizinājumam) un kāpēc
- 20' — uzdevumi
- 5' — kas notiek, ja uzkrājēju inicializē cikla iekšpusē

**Uzdevumi**
12. Aprēķini un izvadi skaitļu summu no 1 līdz 100.
13. Programma prasa `n` un izvada `n` faktoriālu (visu skaitļu reizinājumu no 1 līdz `n`).
14. Programma prasa 5 skaitļus pēc kārtas un izvada to summu un vidējo aritmētisko.
15. Programma prasa skaitli un saskaita, cik tajā ir ciparu.
16. ★ Programma prasa skaitli un izvada tā ciparu summu (izmantojot `%` un `//` ciklā).
17. ★ Aprēķini summu `1/1 + 1/2 + 1/3 + … + 1/n` un izvadi ar četriem cipariem aiz komata.

**Mājasdarbs:** 14. uzdevums

## 10-018 · Praktikums: aprēķini ar for ciklu
`prakse` · FV3 (papīrs)

**Tēma:** Praktikums: aprēķini ar `for` ciklu.
**SR:** Patstāvīgi uzraksta programmu, kas ciklā apstrādā skaitļu virkni un izvada rezultātu.
**Standarts:** T.O.2.4.13. · T.O.2.4.8.

**Gaita**
- 15' — **FV3** uz papīra, datori vēl aizvērti
- 5' — uzdevumu nolasīšana
- 20' — patstāvīgs darbs, skolotājs konsultē individuāli

**Uzdevumi**
18. **Krājkonts.** Sākumā kontā ir 500 EUR, katru gadu pieaug par 3 %. Izvadi atlikumu pēc
   katra gada 10 gadu garumā, ar diviem cipariem aiz komata.
19. **Temperatūru vidējais.** Programma prasa 7 dienu temperatūras un izvada vidējo, kā arī
   cik dienās bija virs vidējā.
20. ★ **Procentu tabula.** Izvadi tabulu, kas rāda, cik gadu vajag, lai 1000 EUR dubultotos
   pie 1 %, 3 % un 5 % likmes.

**Mājasdarbs:** pabeigt 19. uzdevumu

## 10-019 · while cikls
`prakse` · `teorija.py` §4

**Tēma:** Cikls `while`. Cikla nosacījums un tā pārbaude.
**SR:** Uzraksta `while` ciklu un pamato, kāpēc konkrētam uzdevumam tas ir piemērotāks par `for`.
**Standarts:** T.O.2.4.13. · T.Li.2.

**Gaita**
- 5' — kad nezinām, cik reižu jāatkārto
- 10' — demo §4: nosacījums, mainīgā izmaiņa ciklā, bezgalīgs cikls
- 20' — uzdevumi
- 5' — kā apturēt programmu, kas iestrēgusi (Ctrl+C)

**Uzdevumi**
21. Izvadi skaitļus no 1 līdz 10, izmantojot `while`.
22. Programma sāk ar skaitli 100 un katrā solī dala to uz pusēm, līdz rezultāts ir mazāks
   par 1. Izvadi katru soli.
23. Programma prasa skaitli un izvada, cik reizes to var izdalīt ar 2 bez atlikuma.
24. Programma skaita no 1 uz augšu, līdz summa pārsniedz 1000, un izvada, pie kura skaitļa
   tas notika.
25. ★ Programma prasa skaitli un pārbauda, vai tas ir pirmskaitlis.

**Mājasdarbs:** 23. uzdevums

## 10-020 · while ar lietotāja ievadi
`prakse` · `teorija.py` §5

**Tēma:** Cikls ar lietotāja ievadi. Ievades atkārtošana līdz derīgai vērtībai.
**SR:** Uzraksta ciklu, kas atkārto ievades pieprasījumu, līdz lietotājs ievada derīgus datus.
**Standarts:** T.O.2.4.13. · T.V.2.3.5.

**Gaita**
- 5' — kas notiek, ja lietotājs ievada muļķības
- 10' — demo §5: ievades cikls, izejas nosacījums, sentinel vērtība
- 20' — uzdevumi
- 5' — laba kļūdas ziņa lietotājam

**Uzdevumi**
26. Programma prasa skaitli no 1 līdz 10 un atkārto pieprasījumu, līdz ievade ir derīga.
27. Programma prasa paroli, līdz tā ir pareiza, un skaita mēģinājumus.
28. Programma pieņem skaitļus, līdz lietotājs ievada 0, un tad izvada to summu.
29. Programma prasa vārdus, līdz ievadīts tukšs teksts, un izvada, cik vārdu ievadīti.
30. ★ Mini spēle: programma izdomā skaitli no 1 līdz 100 (`random`), lietotājs min, programma
   saka `par lielu` vai `par mazu` un beigās izvada mēģinājumu skaitu.

**Mājasdarbs:** 28. uzdevums

## 10-021 · break un continue
`prakse` · `teorija.py` §6

**Tēma:** Cikla pārtraukšana ar `break` un soļa izlaišana ar `continue`.
**SR:** Lieto `break` un `continue`, lai vadītu cikla izpildi.
**Standarts:** T.O.2.4.13.

**Gaita**
- 5' — meklēšana: kāpēc turpināt, ja jau esam atraduši
- 10' — demo §6: `break` pret `continue`, un kāpēc ar tiem nevajag pārspīlēt
- 20' — uzdevumi
- 5' — vai to pašu var uzrakstīt bez `break`

**Uzdevumi**
31. Programma prasa 10 skaitļus, bet apstājas uzreiz, ja ievadīts negatīvs skaitlis.
32. Izvadi skaitļus no 1 līdz 50, izlaižot visus, kas dalās ar 3.
33. Programma meklē pirmo skaitli no 100 uz augšu, kas dalās gan ar 7, gan ar 11.
34. Programma prasa skaitļus, līdz ievadīts `0`, un izvada lielāko no tiem.
35. ★ Pārraksti 33. uzdevumu bez `break` un salīdzini, kurš variants ir saprotamāks.

**Mājasdarbs:** 32. uzdevums

## 10-022 · Ievades validācija ar ciklu
`prakse`

**Tēma:** Datu validācija. Ievades pārbaude ciklā.
**SR:** Uzraksta programmu, kas pārbauda ievades derīgumu un neļauj turpināt ar nederīgiem datiem.
**Standarts:** T.V.2.3.5. · T.O.2.4.13.

**Gaita**
- 5' — atkārtojums no 01. bloka: kāpēc `int(input())` avarē
- 10' — derīguma nosacījumi: diapazons, formāts, tukša ievade
- 20' — uzdevumi
- 5' — ko programma dara, ja lietotājs kļūdās desmit reizes pēc kārtas

**Uzdevumi**
36. Programma prasa vecumu un pieņem tikai skaitli no 1 līdz 120.
37. Programma prasa mēneša numuru un pieņem tikai 1–12, katrā kļūdas gadījumā paskaidrojot,
   kas nav kārtībā.
38. Programma prasa atzīmi un pieņem tikai veselu skaitli no 1 līdz 10.
39. Papildini 10-018 18. uzdevumu (krājkonts) ar ievades validāciju: procentu likmei jābūt
   no 0 līdz 20.
40. ★ Programma prasa datumu formātā `DD.MM` un pārbauda, vai diena un mēnesis ir iespējami.

**Mājasdarbs:** 38. uzdevums

## 10-023 · Ligzdoti cikli
`prakse` · `teorija.py` §7

**Tēma:** Ligzdoti cikli. Divdimensiju rakstu un tabulu izvade.
**SR:** Uzraksta ligzdotu ciklu, kas izvada dotu rakstu vai tabulu.
**Standarts:** T.O.2.4.13. · T.O.2.4.16.

**Gaita**
- 5' — cik reižu izpildīsies iekšējais cikls, ja ārējais iet 5 reizes?
- 10' — demo §7: `print(..., end="")` un rindas beigas
- 20' — uzdevumi
- 5' — cik darbību veic programma ar diviem ligzdotiem cikliem līdz `n`?

**Uzdevumi**
41. Izvadi taisnstūri no zvaigznītēm 5 rindās un 8 kolonnās.
42. Izvadi trijstūri, kur pirmajā rindā ir viena zvaigznīte, otrajā divas utt. līdz 7.
43. Izvadi visu reizināšanas tabulu no 1 līdz 10 taisnā tabulā.
44. Izvadi apgrieztu trijstūri (pirmajā rindā 7 zvaigznītes, pēdējā — viena).
45. ★ Izvadi Paskāla trijstūra pirmās 6 rindas.
46. ★ Izvadi kvadrātu, kas iekšpusē ir tukšs — tikai maliņas no zvaigznītēm.

**Mājasdarbs:** 42. uzdevums

## 10-024 · Blokshēmas un pseidokods
`jaukta`

**Tēma:** Algoritma shematiskais pieraksts: blokshēma un pseidokods.
**SR:** Pieraksta algoritmu blokshēmā vai pseidokodā un realizē to kodā.
**Standarts:** T.O.2.4.13. · T.Li.2.

**Gaita**
- 10' — blokshēmas elementi: sākums/beigas, darbība, lēmums, ievade/izvade
- 10' — viens algoritms trijos pierakstos: vārdiem, blokshēmā, kodā
- 15' — uzdevumi
- 5' — kāpēc programmētāji zīmē, pirms raksta

**Uzdevumi**
47. Uzzīmē blokshēmu algoritmam, kas nosaka lielāko no trim skaitļiem.
48. Pieraksti pseidokodā algoritmu, kas saskaita, cik sarakstā ir pāra skaitļu.
49. Dota blokshēma (uz tāfeles). Uzraksti tai atbilstošu programmu.
50. Savai 10-020 30. uzdevuma spēlei uzzīmē blokshēmu.
51. ★ Uzzīmē blokshēmu algoritmam, kas pārbauda, vai skaitlis ir pirmskaitlis, un pieraksti,
   kurā vietā tajā var pārtraukt meklēšanu ātrāk.

**Mājasdarbs:** 48. uzdevums

## 10-025 · Klasiskie cikla algoritmi
`prakse` · `teorija.py` §8

**Tēma:** Minimuma, maksimuma un skaita meklēšana ciklā.
**SR:** Realizē pamatalgoritmus — atrod lielāko, mazāko un saskaita elementus pēc pazīmes.
**Standarts:** T.O.2.4.16. · T.O.2.4.19.

**Gaita**
- 5' — kā atrast lielāko, ja visus skaitļus vienlaikus neredz
- 10' — demo §8: sākumvērtības izvēle min/max meklēšanā un kāpēc tā ir bīstamā vieta
- 20' — uzdevumi
- 5' — cik salīdzinājumu veic algoritms ar `n` skaitļiem?

**Uzdevumi**
52. Programma prasa 8 skaitļus un izvada lielāko.
53. Programma prasa 8 skaitļus un izvada mazāko un tā kārtas numuru.
54. Programma prasa 10 atzīmes un saskaita, cik ir zemākas par 4.
55. Programma prasa skaitļus, līdz ievadīts 0, un izvada lielāko, mazāko un vidējo.
56. ★ Programma atrod lielāko un otro lielāko skaitli **vienā** ciklā.
57. ★ Fibonači virkne: izvadi pirmos 15 locekļus.

**Mājasdarbs:** 54. uzdevums

## 10-026 · Praktikums: algoritmi ar cikliem
`prakse` · FV4 (dators)

**Tēma:** Praktikums: algoritmi ar cikliem.
**SR:** Izvēlas uzdevumam piemērotu cikla veidu un realizē algoritmu patstāvīgi.
**Standarts:** T.O.2.4.13. · T.O.2.4.16.

**Gaita**
- 5' — uzdevumu nolasīšana
- 20' — patstāvīgs darbs
- 15' — **FV4** pie datora

**Uzdevumi**
58. **Skaitļa apgriešana.** Programma prasa skaitli un izvada to ar cipariem pretējā secībā
   (piemēram, 1234 -> 4321).
59. **Palindroms.** Programma pārbauda, vai skaitlis lasās vienādi abos virzienos.
60. ★ **Dalītāji.** Programma prasa skaitli un izvada visus tā dalītājus, kā arī pasaka,
   vai skaitlis ir pilnīgs (dalītāju summa bez paša skaitļa ir vienāda ar to).

**Mājasdarbs:** pabeigt 59. uzdevumu

## 10-027 · Atkārtojums pirms pārbaudes darba
`jaukta`

**Tēma:** Cikli: atkārtojums. Biežākās kļūdas un to novēršana.
**SR:** Atpazīst un izlabo tipiskās cikla kļūdas svešā kodā.
**Standarts:** viss bloks

**Gaita**
- 10' — kopīgi: kad `for`, kad `while`; robežu kļūdas; uzkrājēja vieta
- 20' — uzdevumi ar kļūdainām programmām
- 10' — jautājumi, individuālas konsultācijas

**Uzdevumi**
61. Katrā programmā ir viena kļūda. Atrodi to, nepalaižot kodu:
   ```python
   summa = 0
   for i in range(1, 10):
       summa = i
   print(summa)
   ```
   ```python
   n = 5
   while n > 0:
       print(n)
   ```
   ```python
   for i in range(1, 5):
       for j in range(1, 5):
           print("*")
       print()
   ```
62. Pieraksti, ko izvadīs katra no trim programmām pēc izlabošanas.
63. ★ Uzraksti programmu, kas izvada to pašu, ko dotā programma, bet ar `while` `for` vietā.

**Mājasdarbs:** atkārtot bloka jēdzienus

## 10-028 · Pārbaudes darbs
`pārbaudes darbs`

**Tēma:** Pārbaudes darbs: cikli, uzkrājēji, ligzdoti cikli, algoritmi.
**SR:** Demonstrē bloka sasniedzamos rezultātus patstāvīgā darbā.
**Standarts:** viss bloks

**Gaita**
- 40' — darbs uz papīra, datori aizvērti; kods jāraksta ar roku

**Materiāli:** SV2 — divi varianti, papīra darbs (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **`range(n)` beidzas ar `n-1`.** Šī ir bloka biežākā kļūda un tā atkārtosies visu gadu.
  10-016 tam jāvelta atsevišķs brīdis, un pārbaudes darbā tas ir apzināti pārbaudīts.
- **Uzkrājēja inicializācija.** Ja `summa = 0` ir cikla iekšpusē, programma strādā, bet dod
  nepareizu rezultātu — tā ir loģiskā kļūda, kas nemet nekādu paziņojumu. Rādi to apzināti.
- **`while` bez izmaiņas.** Pirms pirmā `while` uzdevuma parādi bezgalīgu ciklu un Ctrl+C,
  lai skolēni nebaidās, kad tas notiek viņiem.
- **Ligzdotie cikli un ātrdarbība.** 10-023 un 10-025 beigās uzdotais jautājums par darbību
  skaitu ir pirmais pieskāriens algoritma sarežģītībai. Atbilde nav jāformalizē — pietiek,
  ka skolēns pamana: viens cikls `n` soļi, divi ligzdoti — `n × n`.
- **Kods ar roku.** SV2 ir papīra darbs, kurā jāuzraksta divas programmas ar roku. Tāpēc
  vismaz 10-021 un 10-027 daļa uzdevumu jāatrisina burtnīcā, pirms tos raksta datorā —
  citādi pārbaudes darbā formāts pats par sevi būs pārsteigums.
- **★ uzdevumi šajā blokā** (pirmskaitlis, Fibonači, palindroms, ciparu summa) ir tiešā veidā
  olimpiādes pirmās kārtas materiāls. Skat. `kurss/zvaigznu-trase.md`.
