class Szkola():
    nauczyciele=[]
    kursy=[]
    studenci=[]



    def __init__(self):
        self.nazwa=input("Podaj nazwę Szkoły")
        self.adres=input("Podaj adres")

        P=input("Podaj liczbę nauczycieli")
        for p in range(int(P)):
            self.nauczyciele.append(Nauczyciel())

        H=input("Podaj liczbę kursów")
        for h in range(int(H)):
            self.kursy.append(Kurs(self.nauczyciele))


        S=input("Podaj liczbę studentów")
        for s in range(int(S)):
            self.studenci.append(Student(self.kursy))

    def wypisanie_studentów_email(self):
        self.studenci.sort(key=lambda x: x.email)
        for s in self.studenci:
            self.stu=s
            print(self.stu.__dict__)
        #print(self.studenci)

    def wypisanie_nauczycieli(self):
        self.nauczyciele.sort(key=lambda x: x.email)
        for n in self.nauczyciele:
            self.nau=n
            print(self.nau.__dict__)
        #print(self.nauczyciele)

    def wypisanie_kursow(self,sem):
        for s in self.kursy:
            if(s.semestr==sem):
                print(s.__dict__)




    def dodaj_ucznia(self):
        self.studenci.append(Student(self.kursy))

    def dodaj_nauczyciela(self):
         self.nauczyciele.append(Nauczyciel())

    def dodaj_kurs(self):
        self.kursy.append(Kurs(self.nauczyciele))

    def srednia_szkoly(self):
        print("")





class Nauczyciel(Szkola):
    def __init__(self):
        self.pesel=input("Podaj pesel")
        self.email=input("Podaj email")
        self.stopien=input("podaj stopien")
        self.kursy_nauczyciela=[]


class Kurs(Szkola):
    #self.studenci = []
    def __init__(self,nauczyciele):
        self.nazwa = input("Podaj nazwę")
        self.semestr = input("podaj semestr")
        pomoc = 1
        while (pomoc==1):
            self.pesel=input("Podaj pesel nauczyciela prowadząego kurs")
            for N in nauczyciele:
                if (self.pesel == N.pesel):
                     self.nauczyciel = N
                     self.nauczyciel.kursy_nauczyciela=self
                     pomoc = 0
            if(pomoc==1):
                print("Nie znaleziono nauczyciela. Wpisz jeszcze raz")
                     #print(self.nauczyciel.__dict__)    #pokazuje nam objekt nauczyciel z utworzonym właśnie kursem

        self.studenci = []




class Student(Szkola):
    kursy_studenta=[]
    def __init__(self,kursy):
        self.pesel=input("Podaj pesel studenta")
        self.email=input("Podaj email")
        self.semestr=input("podaj semestr")
        for kur in kursy:                         #wyświetla wszystkie dostępne kursy w celu spr czy jakiekolwiek kursy istnieją
            self.ku=kur
            print(self.ku.__dict__)
        K=input("Podaj liczbę kursów")
        for k in range(int(K)):
            pomoc=1
            while(pomoc==1):
                self.nazwa = input("Podaj nazwę kursu")
                for C in kursy:
                    if (self.nazwa == C.nazwa and self.semestr==C.semestr):
                        self.kursy_studenta = C
                        C.studenci = self
                        pomoc=0
                if(pomoc==1):
                    print("Niepoprawny semestr albo nie ma takiego kursu. Wpisz jeszcze raz")



objekt_szkola = Szkola()

print("Klasa szkoła:")      #wyświetlenie aktualnej struktury szkoly
for s in Szkola.studenci:
    print(s.__dict__)
for s in Szkola.nauczyciele:
    print(s.__dict__)
for s in Szkola.kursy:
    print(s.__dict__)

value=input(" Podaj semestr z jakiego mają zostać wypisane kursy ")
print("Kursy z dnego semestru")
objekt_szkola.wypisanie_kursow(value)

print("Teraz dodajemy pojedyncze objekty: kurs,ucznia,nauczyciela")
objekt_szkola.dodaj_kurs()
objekt_szkola.dodaj_ucznia()
objekt_szkola.dodaj_nauczyciela()





