import math
import logging

class FolhaImagem:

    def __init__(self,folha,quantidade_imagens_por_folha):

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

        return [self.quantidade_linhas,self.quantidade_colunas]

        
