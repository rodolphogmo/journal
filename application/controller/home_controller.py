from flask import render_template
from application.model.dao.noticia_dao import NoticiaDAO
from application.model.dao.estado_dao import EstadoDAO
from application import app



@app.route("/")
def home():
    if __name__=='__name__':
        instance = NoticiaDAO
    lista_noticias = NoticiaDAO().lista_noticia
    noticia = NoticiaDAO().noticia_mais_curtida(lista_noticias)
    
    return render_template("home.html", lista_noticias=lista_noticias, noticia=noticia)