from flask import render_template
from application.model.dao.noticia_dao import NoticiaDAO
from application.model.dao.estado_dao import EstadoDAO
from application import app

@app.route("/estado/<int:estado_id>")
def state(estado_id: int):
    lista_estados = EstadoDAO().lista_estados
    estado = EstadoDAO().buscar_estado(estado_id, lista_estados)
    lista_noticia = NoticiaDAO().lista_noticia
    lista_noticias = EstadoDAO().buscar_noticias_estado(estado_id, lista_noticia)
    return render_template("estado.html", estado=estado, lista_noticias=lista_noticias)