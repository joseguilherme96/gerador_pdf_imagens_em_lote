from src.Folha import Folha
from src.FolhaImagem import FolhaImagem
from src.Pdf import Pdf
from src.Imagem import Imagem
from PIL import Image as PillowImage
from reportlab.pdfgen import canvas
import logging  
from dynaconf import settings
from src.main_opcoes import flags 

def main():

    logging.info("Processando imagens.......")

    folha = Folha(tipo_folha='A4',comprimento=210,largura=297,margem_em_cada_lado=10)

    logging.debug(f"Folha criada: {folha}")

    quantidade_imagens_por_folha = flags[0]['value'] if flags[0]['value'] else 4
    ajuste_width = flags[1]['value'] if flags[1]['value'] else 1.0
    ajuste_height = flags[1]['value'] if flags[2]['value'] else 1.0

    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=int(quantidade_imagens_por_folha))
    logging.debug(f"FolhaImagem configurada: {folha_imagem}")

    comprimento_largura_maxima_imagem = folha_imagem.calcular_comprimento_largura_maxima_imagem()
    logging.debug(f"Dimensão máxima de imagem: {comprimento_largura_maxima_imagem}")

    imagens = Imagem(PillowImage,folha_imagem)
    logging.debug(f"Classe PillowImage inicializada: {imagens}")

    imagens = imagens.redimensionar_imagem(ajuste_width,ajuste_height)

    logging.debug(f"Imagens redimensionadas: {imagens}")

    pdf = Pdf(canvas,folha_imagem)
    logging.debug(f"Classe canvas inicializado : {pdf}")

    criar_pdf_com_imagens = pdf.criar_pdf_com_imagens()
    logging.debug(f"Pdf criado com as imagens: {criar_pdf_com_imagens}")

    logging.info("Finalizado processamento......")

if __name__ == 'main':

    main()
