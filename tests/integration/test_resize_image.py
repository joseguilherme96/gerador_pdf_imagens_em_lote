from src.Imagem import Imagem
from src.FolhaImagem import FolhaImagem
from src.Folha import Folha
from src.Conversao import Conversao
from PIL import Image
from pathlib import Path
from src.Diretorio import Diretorio
import logging
from dotenv import load_dotenv
import os


def test_cada_imagem_de_cada_lote_devem_ser_redimensionadas(criar_lotes_imagens,caplog):

    caplog.set_level(logging.INFO)
    
    folha = Folha(tipo_folha='A4',comprimento=210,largura=297,margem_em_cada_lado=10)
    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=4)
    imagens = Imagem(Image,folha_imagem)

    folha_imagem.calcular_comprimento_largura_maxima_imagem()
    lotes_redimensionados = imagens.redimensionar_imagem()

    for lote_imagem in lotes_redimensionados:

        for imagem in lote_imagem:

            assert imagem['imagem'].width <= Conversao.convert_mm_to_pixel(folha_imagem.comprimento_maximo_imagem_na_folha)
            assert imagem['imagem'].height <=  Conversao.convert_mm_to_pixel(folha_imagem.largura_maxima_imagem_na_folha)

    
    

