class Noticia:

    def __init__(self, video: str, imagem_show: str, titulo: str, conteudo: str, data: int):
        self.__video = video
        self.__imagem_show = imagem_show
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__data = data

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

    