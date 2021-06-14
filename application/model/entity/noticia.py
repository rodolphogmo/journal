from application.model.entity.estado import Estado

class Noticia:

    def __init__(self, video: str, imagem_show: str, titulo: str, conteudo: str, data: int, estado, likes: int, views: int, id: int):
        self.__video = video
        self.__imagem_show = imagem_show
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__data = data
        self.__estado = estado
        self.__likes = likes
        self.__views = views
        self.__id = id

    def get_video(self) -> str:
        return self.__video

    def get_imagem_show(self) -> str:
        return self.__imagem_show

    def get_titulo(self) -> str:
        return self.__titulo

    def get_conteudo(self) -> str:
        return self.__conteudo

    def get_data(self) -> int:
        return self.__data

    def get_estado(self):
        return self.__estado

    def get_likes(self) -> int:
        return self.__likes

    def get_views(self) -> int:
        return self.__views

    def get_id(self) -> int:
        return self.__id