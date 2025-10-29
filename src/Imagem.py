
from pathlib import Path
from src.Conversao import Conversao
from dotenv import load_dotenv
import logging
from dynaconf import settings

class MockImagem:

    pass

class Imagem:

    def __init__(self,imagem,folha_imagem):

        self.imagem = imagem
        self.folha_imagem = folha_imagem

        load_dotenv()

    def gerar_imagem():

        return True

    def redimensionar_imagem(self):

        logging.info("Inicio de redimensionando de imagens .........")

        redimensionamento = []

        BASE_DIR = Path(__file__).resolve().parent.parent

        caminhos_lotes_a_processar = BASE_DIR / settings.IMAGE_PATH_PENDING
        caminhos_lotes_a_processar.mkdir(exist_ok=True)
        
        paths_lotes = [x for x in caminhos_lotes_a_processar.iterdir()]
        
        for (x,path_lote) in enumerate(paths_lotes):

            lote_imagens = []
            path_lote = Path(path_lote)
            paths_images = [x for x in path_lote.iterdir()]

            nova_pasta_lote = BASE_DIR / settings.IMAGE_PATH_PROCESSED / f"lote{x}"
            nova_pasta_lote.mkdir(exist_ok=True)

            paths_images.sort()

            for (x,path_image) in enumerate(paths_images):

                imagem = self.imagem.open(str(path_image))
                nova_imagem = imagem.resize((Conversao.convert_mm_to_pixel(int(self.folha_imagem.comprimento_maximo_imagem_na_folha)), Conversao.convert_mm_to_pixel(int(self.folha_imagem.largura_maxima_imagem_na_folha))))
                
                novo_caminho_imagem = nova_pasta_lote / f"{path_image.name}"
                nova_imagem.save(novo_caminho_imagem)

                nova_imagem = {
                
                'caminho': novo_caminho_imagem,
                'imagem':nova_imagem

                }

                lote_imagens.append(nova_imagem)

            redimensionamento.append(lote_imagens)

        logging.info("Fim do redimensionando de imagens.........")

        return redimensionamento  