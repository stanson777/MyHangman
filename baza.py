class Engine:
    def __init__(self):
        self.words=[
            "Drzewo", "Zegar", "Książka", "Ławka", "Ogórek", "Światło", "Wiatr", "Piasek", "Chleb", "Kot",
            "Samochód", "Okno", "Zamek", "Rzeka", "Słowo", "Telefon", "Góry", "Las", "Most", "Rower",
            "Mysz", "Stół", "Kawa", "Róża", "Jabłko", "Drzwi", "Zegarek", "Krzesło", "Balon", "Deszcz",
            "Dom", "Liść", "Księżyc", "Ziemia", "Lampa", "Słońce", "Zupa", "Ściana", "Koń", "Pies",
            "Herbata", "Ołówek", "Chmura", "Pomarańcza", "Drzewo", "Fotografia", "Muzyka", "Talerz", "Jajko", "Mleko",
            "Pióro", "Motyl", "Plecak", "Rzeka", "Łódka", "Ptak", "Woda", "Lód", "Kwiat", "Papier",
            "Kubek", "Miasto", "Wazon", "Mapa", "Wieża", "Buty", "Pociąg", "Zeszyt", "Obraz", "Klucz",
            "Pszczoła", "Zamek", "Czekolada", "Miś", "Świeca", "Okulary", "Skrzynka", "Trawa", "Drabina", "Zegarek",
            "Truskawka", "Lampa", "Komputer", "Łańcuch", "Gwiazda", "Płyta", "Szklanka", "Kamień", "Miłość", "Rybka",
            "Chusteczka", "Plecak", "Wiatrak", "Słoik", "Flaga", "Perfumy", "Poduszka", "Mapa", "Skarpetka", "Podłoga",
            "Śrubka", "Serce", "Wieża", "Park", "Grzyb", "Ogród", "Most", "Długopis", "Rower", "Rękawiczka",
            "Królik", "Noc", "Dzbanek", "Cukier", "Siatka", "Szalik", "Pączek", "Strona", "Brama", "Drzwi",
            "Ślimak", "Poduszka", "Przycisk", "Telefon", "Pomidor", "Ziemniak", "Wiosna", "Zima", "Orzeł", "Liść",
            "Kwiat", "Woda", "Latarnia", "Butelka", "Latarka", "Stolik", "Deska", "Zegar", "Owoc", "Zamek",
            "Książka", "Kalendarz", "Pióro", "Krowa", "Klawiatura", "Zeszyt", "Krzesło", "Pająk", "Światło", "Wąż"
        ]
        self.polish_letters={"ó":"o","ł":"l","ą":"a","ż":"z","ś":"s","ć":"c","ń":"n","ź":"z","ę":"e"}




    def get_words(self):
        self.list_modifier(self.words)
        return self.deleted_duplicates(self.words)

    def add_word(self,word):
        self.words.append(word)


    def word_modifier(self,word):
        new_word=[]
        for i in range(len(word)):
            if word[i].lower() in self.polish_letters:
                if i==0:
                    new_word.append(self.polish_letters[word[i].lower()].upper())
                else:
                    new_word.append(self.polish_letters[word[i].lower()])
            else:
                new_word.append(word[i])

        return "".join(new_word)

    def list_modifier(self,list):
        for i in range(len(list)):
            list[i]=self.word_modifier(list[i])

    def counter(self,list):
        counter=0
        for i in list:
            counter+=1

        return counter

    def which_word_has_duplicates(self,words):
        words2=[]
        repeated_words=[]
        for word in words:
            if word in words2:
                repeated_words.append(word)
            else:
                words2.append(word)

        return repeated_words



    def deleted_duplicates(self,list2):
        return list(set(list2))









