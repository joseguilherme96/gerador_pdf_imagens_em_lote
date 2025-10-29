from src.Folha import Folha
from src.FolhaImagem import FolhaImagem
from src.Pdf import Pdf
from src.Imagem import Imagem
from PIL import Image as PillowImage
from reportlab.pdfgen import canvas
import logging  
from dynaconf import settings


def main():

    logging.info("Processando imagens.......")
    logging.info(f"Ambiente : {settings.current_env}")

    folha = Folha(tipo_folha='A4',comprimento=210,largura=297,margem_em_cada_lado=10)
    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=4)
    imagens = Imagem(PillowImage,folha_imagem)
    pdf = Pdf(canvas,folha_imagem)

    folha_imagem.calcular_comprimento_largura_maxima_imagem()
    imagens = imagens.redimensionar_imagem()
    criar_pdf_com_imagens = pdf.criar_pdf_com_imagens()

    logging.info("Finalizado processamento......")

if __name__ == 'main':

    main()
