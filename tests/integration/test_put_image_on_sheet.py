from src.Imagem import Imagem
from src.FolhaImagem import FolhaImagem
from src.Folha import Folha
from src.Pdf import Pdf
from PIL import Image
from pathlib import Path
from src.Diretorio import Diretorio
import logging
from reportlab.pdfgen import canvas
from dotenv import load_dotenv
import os

def test_as_imagens_de_cada_lote_de_imagens_deve_ser_inseridas_no_pdf(criar_lotes_imagens,caplog):

    load_dotenv()

    caplog.set_level(logging.INFO)
    
    folha = Folha(tipo_folha='A4',comprimento=210,largura=297,margem_em_cada_lado=10)
    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=4)
    imagens = Imagem(Image,folha_imagem)

    folha_imagem.calcular_comprimento_largura_maxima_imagem()
    lotes_redimensionados = imagens.redimensionar_imagem()

    model_pdf = Pdf(canvas,folha_imagem)
    pdfs_por_lote = model_pdf.criar_pdf_com_imagens()

    for pdf in pdfs_por_lote:

        assert pdf.suffix == '.pdf'
