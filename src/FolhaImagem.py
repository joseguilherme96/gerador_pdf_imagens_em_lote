import math
import logging

class FolhaImagem:

    def __init__(self,folha,quantidade_imagens_por_folha = 4):

        logging.info("Iniciando FolhaImagem")

        self.folha = folha
        self.quantidade_imagens_por_folha = quantidade_imagens_por_folha
        self.quantidade_linhas = None
        self.quantidade_colunas = None
        self.comprimento_maximo_imagem_na_folha : None
        self.largura_maxima_imagem_na_folha : None

    def calcular_comprimento_largura_maxima_imagem(self):

        self.criar_linhas_colunas_para_inserir_imagens()

        largura_imagem = self.folha.calcular_largura_livre() / self.quantidade_linhas
        comprimento_imagem =  self.folha.calcular_comprimento_livre() / self.quantidade_colunas

        self.comprimento_maximo_imagem_na_folha = comprimento_imagem
        self.largura_maxima_imagem_na_folha = largura_imagem

        return [comprimento_imagem,largura_imagem]
    
    def criar_linhas_colunas_para_inserir_imagens(self):

        self.quantidade_linhas = math.ceil(math.sqrt(self.quantidade_imagens_por_folha))
        self.quantidade_colunas = math.ceil(self.quantidade_imagens_por_folha / self.quantidade_linhas)

        logging.debug(f"Quantidade de linhas : {self.quantidade_linhas}")
        logging.debug(f"Quantidade de colunas : {self.quantidade_colunas}")

        return [self.quantidade_linhas,self.quantidade_colunas]
    
    def get_coordenadas_imagens(self):
         
        coodernadas_por_quantidade_imagens_por_folha = {

            "2":[(100,500),(100,150)],
            "4":[(0,500),(250,500),(0,150),(250,150)],
            "6":[(-90,500),(100,500),(290,500),(-90,150),(100,150),(290,150)]
        }
         
        chave = self.quantidade_imagens_por_folha
        coordenadas = coodernadas_por_quantidade_imagens_por_folha[f"{chave}"]
    
        return coordenadas

    
    def desenhar_imagens_na_folha(self,canvas,path_images,coodernadas):
        
        for (key,coodernada) in enumerate(coodernadas):
                
                if key < len(path_images):

                    logging.info("Inserindo imagem no pdf.........")
                    canvas.drawImage(
                        path_images[key],    
                        x=coodernada[0],
                        y=coodernada[1],
                        width=400, 
                        height=300, 
                        preserveAspectRatio=True
                    )
                    logging.info(path_images[key])

        

        
