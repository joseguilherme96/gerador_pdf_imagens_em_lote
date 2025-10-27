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

def test_as_imagens_de_cada_lote_de_imagens_deve_ser_inseridas_no_pdf(criar_lotes_imagens,caplog,redimensionar_imagens_inserir_no_pdf):

    load_dotenv()

    caplog.set_level(logging.INFO)
    
    pdfs_por_lote = redimensionar_imagens_inserir_no_pdf

    for pdf in pdfs_por_lote:

        assert pdf.suffix == '.pdf'
