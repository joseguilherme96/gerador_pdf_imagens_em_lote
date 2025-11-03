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
from dynaconf import settings
import logging
from src.Flags import flags


@fixture(scope="session")
def redimensionar_imagens_inserir_no_pdf(criar_lotes_imagens,request):

    load_dotenv()
    
    quantidade_imagens_por_folha = request.config.getoption('--qtd-imagens-por-folha')
    ajuste_width = request.config.getoption('--ajuste-width')
    ajuste_height = request.config.getoption('--ajuste-height')

    folha = Folha(tipo_folha='A4',comprimento=210,largura=297,margem_em_cada_lado=10)
    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=int(quantidade_imagens_por_folha))
    imagens = Imagem(Image,folha_imagem)

    folha_imagem.calcular_comprimento_largura_maxima_imagem()
    lotes_redimensionados = imagens.redimensionar_imagem(ajuste_width,ajuste_height)

    model_pdf = Pdf(canvas,folha_imagem)
    pdfs_por_lote = model_pdf.criar_pdf_com_imagens()

    yield pdfs_por_lote


@fixture(scope="session")
def criar_lotes_imagens(request):

    yield True

    teardown = request.config.getoption('--teardown')

    load_dotenv()

    if teardown == "True":

        Diretorio.limpar_diretorio(settings.IMAGE_PATH_PROCESSED)

@fixture(scope="session",autouse=True)
def set_test_settings():
    
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
    logging.info("Sendo executado em ambiente de teste.........")


def pytest_addoption(parser):
    
    for flag in flags:

        parser.addoption(f"-{flag['flag_name']}",action="store", default=flag['default'], help=flag['help'])



