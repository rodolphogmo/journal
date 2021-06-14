from application.model.entity.estado import Estado
from typing import List


class EstadoDAO:

    def __init__(self):


        

        estado1 = Estado(1, "São Paulo", "img/sao_paulo_bandeira.jpg", "SP")
        estado2 = Estado(2, "Rio de Janeiro", "img/rio_de_janeiro_bandeira.jpg", "RJ")
        estado3 = Estado(3, "Minas Gerais", "img/minas_gerais_bandeira.jpg", "MG")
        estado4 = Estado(4, "Espírito Santo", "img/espirito_santo_bandeira.jpg", "ES")

        self.lista_estados = []
        self.lista_estados.append(estado1)
        self.lista_estados.append(estado2)
        self.lista_estados.append(estado3)
        self.lista_estados.append(estado4)

    def buscar_estado(self, id, lista_estados):
        for estado in lista_estados:
            if estado.get_id() == int(id):
                return estado
        return None


    def buscar_noticias_estado(self, id, lista_noticia):
            lista_noticias_do_estado = []
            lista_estados = self.lista_estados
            for noticia in lista_noticia:
                if noticia.get_estado() == EstadoDAO.buscar_estado(self, id, lista_estados):
                    lista_noticias_do_estado.append(noticia)
            return lista_noticias_do_estado 