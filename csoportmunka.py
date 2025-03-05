#Göröcs Máté, Ivády Barnabás, Kapitány Levente, Janovics Zombor
varosSebessegAtlag = 50 * 0.8
foutSebessegAtlag = 110 * 0.8
atlagsebessegAutoPalya = 130 * 0.9
ErdTavVarosban = 8.8
ErdTavFout = 0
ErdTavAutoPalyan = 13.2
ErdTavOssz = ErdTavVarosban + ErdTavFout + ErdTavAutoPalyan
t1 = 13
t2 = 0
t3 = 7
utazasiIdo = 2 * (t1 + t2 + t3 + 15)
matricaAr = 5320
benzinAr = 651
fogyasztasVar = 0.095 * ErdTavVarosban
fogyasztasFout = 0.07  * ErdTavFout
fogyasztasAut = 0.085 * ErdTavAutoPalyan
fogyasztasOssz = fogyasztasVar + fogyasztasFout + fogyasztasAut
fogyasztasAr = 2 * (fogyasztasOssz * benzinAr)

valaszto = input("Melyik útvonalat választod? (Érd, Miskolc): ")
if valaszto == "Érd":
    print("------------------------------------------")
    print("| Érdre fogunk menni                      |")
    print(f"|     -Az út hossza: {ErdTavOssz:.1f}km               |")
    print(f"|     -Az út időtartama: {utazasiIdo:.1f}perc         |")
    print(f"|     -Az autópálya matrica ára: {matricaAr:.1f}Ft |")
    print(f"|     -Az üzemanyagköltség: {fogyasztasAr:.1f}Ft      |")
    print(f"|     -Az út költsége:  {matricaAr + fogyasztasAr:.1f}Ft          |")
    print("------------------------------------------")
elif valaszto == "Miskolc":
    print("ez még nincs meg")
else:
    print("Nem megfelelő válasz")
