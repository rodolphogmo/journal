from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia
from application.model.dao.estado_dao import EstadoDAO
from datetime import date
from typing import List



class NoticiaDAO:

    def __init__(self):


        estado1 = Estado(1, "São Paulo", "img/sao_paulo_bandeira.jpg", "SP")
        estado2 = Estado(2, "Rio de Janeiro", "img/rio_de_janeiro_bandeira.jpg", "RJ")
        estado3 = Estado(3, "Minas Gerais", "img/minas_gerais_bandeira.jpg", "MG")
        estado4 = Estado(4, "Espírito Santo", "img/espirito_santo_bandeira.jpg", "ES")

        noticia1 = Noticia("video/covideo1.mp4", "img/covid1.jpg", "corona virus", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", date.today(), estado1, 10, 100, 11)
        noticia2 = Noticia("video/covideo2.mp4", "img/covid2.jpg", "os perigos do corona virus", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", date.today(), estado2, 15, 50, 22)
        noticia3 = Noticia("video/covideo3.mp4", "img/covid3.jpg", "Aumento de contaminados", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", date.today(), estado3, 2, 30, 33)
        noticia4 = Noticia("video/covideo4.mp4", "img/covid4.jpg", "Um quarto da população do estado vacinada!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", date.today(), estado4, 500, 1000, 44)

        

        self.lista_noticia = []
        self.lista_noticia.append(noticia1)
        self.lista_noticia.append(noticia2)
        self.lista_noticia.append(noticia3)
        self.lista_noticia.append(noticia4)
        






    def noticia_mais_curtida(self, listar_tudo):
        n = len(listar_tudo)
        for j in range(n-1):
            min_index = j
            for i in range(j, n):
                if listar_tudo[i].get_likes() > listar_tudo[min_index].get_likes():
                    min_index = i
                j = 0
                if listar_tudo[j].get_likes() < listar_tudo[min_index].get_likes():
                    vetor = listar_tudo[j]
                    listar_tudo[j] = listar_tudo[min_index]
                    listar_tudo[min_index] = vetor
        return listar_tudo    




    def show_noticia(self, id, lista_noticia):
            for noticia in lista_noticia:
                if noticia.get_id() == int(id):
                    return noticia
            return None    

       