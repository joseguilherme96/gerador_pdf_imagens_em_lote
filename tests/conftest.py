from pytest import fixture
import os
from src.Diretorio import Diretorio
from dotenv import load_dotenv
from src.Imagem import Imagem
from src.FolhaImagem import FolhaImagem
from src.Folha import Folha
from src.Pdf import Pdf
from PIL import Image
import logging
from reportlab.pdfgen import canvas


@fixture(scope="session")
def redimensionar_imagens_inserir_no_pdf(criar_lotes_imagens):

    load_dotenv()
    
    folha = Folha(tipo_folha='A4',comprimento=210,largura=297,margem_em_cada_lado=10)
    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=4)
    imagens = Imagem(Image,folha_imagem)

    folha_imagem.calcular_comprimento_largura_maxima_imagem()
    lotes_redimensionados = imagens.redimensionar_imagem()

    model_pdf = Pdf(canvas,folha_imagem)
    pdfs_por_lote = model_pdf.criar_pdf_com_imagens()

    yield pdfs_por_lote


@fixture(scope="session")
def criar_lotes_imagens():

    yield True

    load_dotenv()

    Diretorio.limpar_diretorio(os.getenv('IMAGE_PATH_PROCESSED'))