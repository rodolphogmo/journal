from flask import render_template
from application.model.dao.noticia_dao import NoticiaDAO
from application import app


@app.route("/show/<int:noticia_id>")
def show(noticia_id):
    lista_noticia = NoticiaDAO().lista_noticia
    noticia = NoticiaDAO().show_noticia(noticia_id, lista_noticia)
    
    return render_template("show.html", noticia=noticia)