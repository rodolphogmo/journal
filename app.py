from flask import Flask, render_template
from estado import Estado
from noticia import Noticia
from datetime import date

app = Flask(__name__)

lista_noticias = []
lista_estados = []

estado1 = Estado(1, "São Paulo", "img/sao_paulo_bandeira.jpg", "SP")
estado2 = Estado(2, "Rio de Janeiro", "img/rio_de_janeiro_bandeira.jpg", "RJ")
estado3 = Estado(3, "Minas Gerais", "img/minas_gerais_bandeira.jpg", "MG")
estado4 = Estado(4, "Espírito Santo", "img/espirito_santo_bandeira.jpg", "ES")

lista_estados.append(estado1)
lista_estados.append(estado2)
lista_estados.append(estado3)
lista_estados.append(estado4)

noticia1 = Noticia("video/covideo1.mp4", "img/covid1.jpg", "corona virus", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", date.today(), estado1, 10, 100, 11)
noticia2 = Noticia("video/covideo2.mp4", "img/covid2.jpg", "os perigos do corona virus", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", date.today(), estado2, 15, 50, 22)
noticia3 = Noticia("video/covideo3.mp4", "img/covid3.jpg", "Aumento de contaminados", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", date.today(), estado3, 2, 30, 33)
noticia4 = Noticia("video/covideo4.mp4", "img/covid4.jpg", "Um quarto da população do estado vacinada!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", date.today(), estado4, 500, 1000, 44)

lista_noticias.append(noticia1)
lista_noticias.append(noticia2)
lista_noticias.append(noticia3)
lista_noticias.append(noticia4)

def noticia_mais_curtida(self):
        n = len(lista_noticias)
        for j in range(n-1):
            min_index = j
            for i in range(j, n):
                if lista_noticias[i].get_likes() > lista_noticias[min_index].get_likes():
                    min_index = i
                j = 0
                if lista_noticias[j].get_likes() < lista_noticias[min_index].get_likes():
                    vetor = lista_noticias[j]
                    lista_noticias[j] = lista_noticias[min_index]
                    lista_noticias[min_index] = vetor
        return lista_noticias


noticia = noticia_mais_curtida(lista_noticias)

def buscar_estado(id):
    for estado in lista_estados:
        if estado.get_id() == int(id):
            return estado
    return None

def buscar_noticias_estado(id):
    lista_noticias_do_estado = []
    for noticia in lista_noticias:
        if noticia.get_estado() == buscar_estado(id):
            lista_noticias_do_estado.append(noticia)
    return lista_noticias_do_estado

def show_noticia(id):
        for noticia in lista_noticias:
            if noticia.get_id() == int(id):
                return noticia
        return None

@app.route("/")
def home():
    return render_template("home.html", lista_noticias=lista_noticias, noticia=noticia)

@app.route("/estado/<int:estado_id>")
def state(estado_id: int):
    estado = buscar_estado(estado_id)
    lista_noticias = buscar_noticias_estado(estado_id)
    return render_template("estado.html", estado= estado, lista_noticias=lista_noticias)

@app.route("/show/<int:noticia_id>")
def show(noticia_id):
    noticia = show_noticia(noticia_id)
    
    return render_template("show.html", noticia=noticia)
