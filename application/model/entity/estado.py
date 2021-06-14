class Estado:

    def __init__(self, id: int, nome: str, imagem_path: str, sigla: str):
        self.__id = id
        self.__nome = nome
        self.__imagem_path = imagem_path
        self.__sigla = sigla

    
    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_imagem_path(self) -> str:
        return self.__imagem_path

    def get_sigla(self):
        return self.__sigla