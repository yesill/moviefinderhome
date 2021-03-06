from Film import Film
import pickle
from random import randint

#search_text = ""
class Arama():
    film_list = []

    def __init__(self):
        with open('imdb.pkl','rb') as input:
            self.film_list = pickle.load(input)
    
    def searchParametresiz(self):
        """
            Butun filmler arasindan random bir film secilir...
        """
        rnd = randint(0,len(self.film_list)-1)
        return self.film_list[rnd]


    def search(self,search_text):
        """
            Parametre olarak String alir.
            Aranan film ismi filmler listesinde aynen varsa(tami tamina ayni olmali) aranan filmi obje olarak returnler.
            Aranan film ismi filmler listesinde yoksa 'False' returnler.
        """
        search_text = search_text.lower()
        for film in self.film_list:
            if search_text in film.name.lower():
                return film
        return False
    
    def searchGenre(self,genre):
        film_list = []
        for film in self.film_list:
            if genre in film.genre.lower():
                film_list.append(film)

        rnd = randint(0,len(film_list)-1)
        return film_list[rnd] 

    def oneri(self,searched_film):
        """
            Parametre olarak bir adet film nesnesi alir.
            Aranan filmle ayni veya benzer kategoride film varsa bu filmlerden bir tanesini rastgele secer ve film objesi olarak returnler.
            Aranan filmle ayni veya benzer kategoride film yoksa 'False' returnler.
        """
        if searched_film == False:
            return False

        searched_film_genres = searched_film.genre.replace(' ','').split(',')
        film_list = []
        film_list_same_genre = []
        for film in self.film_list:
            #ayni filmi onerme
            if film.name != searched_film.name:
                if film.genre == searched_film.genre:
                    film_list_same_genre.append(film)
                else:
                    film_genres = film.genre.replace(' ','').split(',')  
                    for genre in film_genres:
                        if genre in searched_film_genres:
                            film_list.append(film)
        
        if len(film_list_same_genre) > 0:
            rnd = randint(0,len(film_list_same_genre)-1)
            return film_list_same_genre[rnd]
        elif len(film_list) > 0:
            rnd = randint(0,len(film_list)-1)
            return film_list[rnd]
        else:
            return False
                

            


