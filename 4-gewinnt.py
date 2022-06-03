#Erster Versuch von 4-Gewinnt in Python
#Das ganze wurde ohne guide oder vorwissen Erstellt also sicherlich grausamer Code
#Freue mich schon das später mit mehr wissen zu verschlimmbessern


# spielfeld um 90° gedreht
# rechts also bei [Spalten1-7] ist oben und links is boden bei postion "0" in der liste
# beim nächsten rewrite könnte man die selbe methode wie für "Wagrecht1-6" nutzen und das ganzen von vorherein richtig zu machen
Spalte7 = [0,0,0,0,0,0]
Spalte6 = [0,0,0,0,0,0]
Spalte5 = [0,0,0,0,0,0]
Spalte4 = [0,0,0,0,0,0]
Spalte3 = [0,0,0,0,0,0]
Spalte2 = [0,0,0,0,0,0]
Spalte1 = [0,0,0,0,0,0]
Player= "Spieler 1 mit X"
Spielerfarbe=1
#wiederholung bis p oder p2 gewinnt
Sieg=0
while Sieg ==0:

      #druckt spielfeld
    print("Aktuelles Spielfeld")
    Wagerecht1 = [Spalte1[0], Spalte2[0], Spalte3[0], Spalte4[0], Spalte5[0], Spalte6[0], Spalte7[0],]
    Wagerecht2 = [Spalte1[1], Spalte2[1], Spalte3[1], Spalte4[1], Spalte5[1], Spalte6[1], Spalte7[1],] 
    Wagerecht3 = [Spalte1[2], Spalte2[2], Spalte3[2], Spalte4[2], Spalte5[2], Spalte6[2], Spalte7[2],]
    Wagerecht4 = [Spalte1[3], Spalte2[3], Spalte3[3], Spalte4[3], Spalte5[3], Spalte6[3], Spalte7[3],] 
    Wagerecht5 = [Spalte1[4], Spalte2[4], Spalte3[4], Spalte4[4], Spalte5[4], Spalte6[4], Spalte7[4],]
    Wagerecht6 = [Spalte1[5], Spalte2[5], Spalte3[5], Spalte4[5], Spalte5[5], Spalte6[5], Spalte7[5],] 

#speudographishe darstellung
    act=1
    i = 0
    while act <7:
        i = 0
        if act ==1:
            Zeichenmacher=Wagerecht6 
        if act ==2:
            Zeichenmacher=Wagerecht5 
        if act ==3:
            Zeichenmacher=Wagerecht4
        if act ==4:
            Zeichenmacher=Wagerecht3 
        if act ==5:
            Zeichenmacher=Wagerecht2 
        if act ==6:
            Zeichenmacher=Wagerecht1  
        while i < len(Zeichenmacher):
#ersätzt die "datensätze von spieler mit symbolen"
            if Zeichenmacher[i] == 0:
                Zeichenmacher[i] = ' '

            if Zeichenmacher[i] == 1:
                Zeichenmacher[i] = 'X'

            if Zeichenmacher[i] == 2:
                Zeichenmacher[i] = 'O'
            i+=1

# mit stern "*" wird beim print die '' entfernt damit das spielfeld "leer ist"
        print(*Zeichenmacher)
        act=act+1
    print("1 2 3 4 5 6 7")
#initialiesierung der leeren variable bzw reset
    Spaltencheck=0
    Spalte=0
    n=0
    SpaltenV = 0    
   
#abfrage der spieler züge und falsche eingabe
    print(Player)
    items = { '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',}
    Auswahl = input("Wähle deine Spalte per Zahl von 1-7 aus: ")
    if Auswahl in items:
        Augewähltespalte = items[Auswahl]
        print (Augewähltespalte + " wurde ausgewählt")
        print("  ")
        Spaltencheck = int(Augewähltespalte)
    else:
        print("huh? falsche Eingabe, gegner darf also :D")

#spieler wechsler  
    if Player=="Spieler 2 mit O":
        Player="Spieler 1 mit X"
        Spielerfarbe=2
    else:
        Player="Spieler 2 mit O"
        Spielerfarbe=1

    #Auswahl der Liste in die der Chip "fällt" 
    #check bis zum ersten leeren platz leere plätze = 0 volle haben 1 oder 2
    if Spaltencheck == 1:
        while Spalte1[n]>0:
            n+=1
        if Spalte1[n]==0:
            Spalte1[n]=Spielerfarbe
    if Spaltencheck == 2:
        while Spalte2[n]>0:
            n+=1
        if Spalte2[n]==0:
            Spalte2[n]=Spielerfarbe

    if Spaltencheck == 3:
        while Spalte3[n]>0:
            n+=1
        if Spalte3[n]==0:
            Spalte3[n]=Spielerfarbe

    if Spaltencheck == 4:
        while Spalte4[n]>0:
            n+=1
        if Spalte4[n]==0:
            Spalte4[n]=Spielerfarbe
    if Spaltencheck == 5:
        while Spalte5[n]>0:
            n+=1
        if Spalte5[n]==0:
            Spalte5[n]=Spielerfarbe

    if Spaltencheck == 6:
        while Spalte6[n]>0:
            n+=1
        if Spalte6[n]==0:
            Spalte6[n]=Spielerfarbe

    if Spaltencheck == 7:
        while Spalte7[n]>0:
            n+=1
        if Spalte7[n]==0:
            Spalte7[n]=Spielerfarbe
    
    
    # DiagSpielerfarbenalisten L links nach rechts
    # Daten kommen aus den "Line" listen
    Diag6L = [Spalte4[0], Spalte3[1], Spalte2[2], Spalte1[3]]
    Diag5L = [Spalte5[0], Spalte4[1], Spalte3[2], Spalte2[3], Spalte1[4]]
    Diag4L = [Spalte6[0], Spalte5[1], Spalte4[2], Spalte3[3], Spalte2[4], Spalte1[5]]
    Diag3L = [Spalte7[0], Spalte6[1], Spalte5[2], Spalte4[3], Spalte3[4], Spalte2[5]]
    Diag2L = [Spalte7[1], Spalte6[2], Spalte5[3], Spalte4[4], Spalte3[5]]
    Diag1L = [Spalte7[2], Spalte6[3], Spalte5[4], Spalte4[5]]

    # Diagonalisten von R rchts nach links
    Diag6R = [Spalte4[5], Spalte3[4], Spalte2[3], Spalte1[2]]
    Diag5R = [Spalte5[5], Spalte4[4], Spalte3[3], Spalte2[2], Spalte1[1]]
    Diag4R = [Spalte6[5], Spalte5[4], Spalte4[3], Spalte3[2], Spalte2[1], Spalte1[0]]
    Diag3R = [Spalte7[5], Spalte6[4], Spalte5[3], Spalte4[2], Spalte3[1], Spalte2[0]]
    Diag2R = [Spalte7[4], Spalte6[3], Spalte5[2], Spalte4[1], Spalte3[0]]
    Diag1R = [Spalte7[3], Spalte6[2], Spalte5[1], Spalte4[0]]

    #Wagerechtcheck 
    Wagerecht1 = [Spalte1[0], Spalte2[0], Spalte3[0], Spalte4[0], Spalte5[0], Spalte6[0], Spalte7[0],]
    Wagerecht2 = [Spalte1[1], Spalte2[1], Spalte3[1], Spalte4[1], Spalte5[1], Spalte6[1], Spalte7[1],] 
    Wagerecht3 = [Spalte1[2], Spalte2[2], Spalte3[2], Spalte4[2], Spalte5[2], Spalte6[2], Spalte7[2],]
    Wagerecht4 = [Spalte1[3], Spalte2[3], Spalte3[3], Spalte4[3], Spalte5[3], Spalte6[3], Spalte7[3],] 
    Wagerecht5 = [Spalte1[4], Spalte2[4], Spalte3[4], Spalte4[4], Spalte5[4], Spalte6[4], Spalte7[4],]
    Wagerecht6 = [Spalte1[5], Spalte2[5], Spalte3[5], Spalte4[5], Spalte5[5], Spalte6[5], Spalte7[5],] 

    #Fast alles listen zusammen in eine gesamt liste und wertet aus ob es eine 4er serie gibt
    ListenListe =[Spalte7,Spalte6, Spalte5,Spalte4,Spalte3, Spalte2, Spalte1, Diag6R, Diag5R, Diag4R, Diag3R, Diag2R, Diag1R, Diag6L, Diag5L, Diag4L, Diag3L, Diag2L, Diag1L, Wagerecht1, Wagerecht2, Wagerecht3, Wagerecht4, Wagerecht5, Wagerecht6,]

    for x in ListenListe:
        ReihenCheck = (x)
        for idx, a in enumerate(ReihenCheck):
            if ReihenCheck[idx:idx+4] == [a,a,a,a]:
                if a == 1:
                    print ("Spieler 1 Gewinnt")
                    Sieg=1
                if a == 2:
                    print("Spieler 2 gewinnt")
                    Sieg=2

#Ausgabe vom letzten Spielfeld
        if Sieg!=0:
            Wagerecht1 = [Spalte1[0], Spalte2[0], Spalte3[0], Spalte4[0], Spalte5[0], Spalte6[0], Spalte7[0],]
            Wagerecht2 = [Spalte1[1], Spalte2[1], Spalte3[1], Spalte4[1], Spalte5[1], Spalte6[1], Spalte7[1],] 
            Wagerecht3 = [Spalte1[2], Spalte2[2], Spalte3[2], Spalte4[2], Spalte5[2], Spalte6[2], Spalte7[2],]
            Wagerecht4 = [Spalte1[3], Spalte2[3], Spalte3[3], Spalte4[3], Spalte5[3], Spalte6[3], Spalte7[3],] 
            Wagerecht5 = [Spalte1[4], Spalte2[4], Spalte3[4], Spalte4[4], Spalte5[4], Spalte6[4], Spalte7[4],]
            Wagerecht6 = [Spalte1[5], Spalte2[5], Spalte3[5], Spalte4[5], Spalte5[5], Spalte6[5], Spalte7[5],] 
            print ("Spiel vorbei, enstand")
            act=1
            i = 0
            while act <7:
                i = 0
                if act ==1:
                    Zeichenmacher=Wagerecht6 
                if act ==2:
                    Zeichenmacher=Wagerecht5 
                if act ==3:
                    Zeichenmacher=Wagerecht4
                if act ==4:
                    Zeichenmacher=Wagerecht3 
                if act ==5:
                    Zeichenmacher=Wagerecht2 
                if act ==6:
                    Zeichenmacher=Wagerecht1  
                while i < len(Zeichenmacher):
                    if Zeichenmacher[i] == 0:
                        Zeichenmacher[i] = ' '

                    if Zeichenmacher[i] == 1:
                        Zeichenmacher[i] = 'X'

                    if Zeichenmacher[i] == 2:
                        Zeichenmacher[i] = 'O'
                    i+=1

                print(*Zeichenmacher)
                act=act+1
            print("1 2 3 4 5 6 7")
            break









