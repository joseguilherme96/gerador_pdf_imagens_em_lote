from dotenv import load_dotenv
import os
from pathlib import Path
from pytest import fixture
import logging
from dynaconf import settings


def get_quantidade_imagens(caminho_pasta):

    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    path_client_image = BASE_DIR / caminho_pasta

    path_lotes = [x for x in path_client_image.iterdir()]
    
    quantidade_imagens_enviadas = 0
    for path_lote in path_lotes:

        paths_images = [path_imagem for path_imagem in path_lote.iterdir() if path_imagem.suffix not in ".pdf"]

        quantidade_imagens_enviadas += len(paths_images)

    return quantidade_imagens_enviadas


def test_a_quantidade_de_imagens_enviadas_pelo_cliente_deve_ser_igual_a_quantidade_imagens_em_processo(redimensionar_imagens_inserir_no_pdf,caplog):

    load_dotenv()

    caplog.set_level(logging.INFO)

    quantidade_imagens_enviadas = get_quantidade_imagens(settings.IMAGE_PATH_RECEIVED)
    quantidade_imagens_processo = get_quantidade_imagens(settings.IMAGE_PATH_PENDING)
    
    assert quantidade_imagens_processo == quantidade_imagens_enviadas

def test_a_quantidade_de_imagens_enviadas_pelo_cliente_deve_ser_igual_a_quantidade_imagens_processadas(redimensionar_imagens_inserir_no_pdf,caplog):

    load_dotenv()

    caplog.set_level(logging.INFO)

    quantidade_imagens_enviadas = get_quantidade_imagens(settings.IMAGE_PATH_RECEIVED)
    quantidade_imagens_processadas = get_quantidade_imagens(settings.IMAGE_PATH_PROCESSED)

    assert quantidade_imagens_processadas == quantidade_imagens_enviadas