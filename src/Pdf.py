from pathlib import Path
from dotenv import load_dotenv
from PIL import Image
import logging
from dynaconf import settings

class MockPdf:

    pass

class Pdf:

    def __init__(self,pdf,folha_imagem):

        self.pdf = pdf
        self.folha_imagem = folha_imagem

    def criar_pdf_com_imagens(self):

        logging.info("Inicio de criação de pdfs .........")

        load_dotenv()

        BASE_DIR = Path(__file__).resolve().parent.parent
        caminhos_imagens_processadas = BASE_DIR / settings.IMAGE_PATH_PROCESSED
        caminhos_imagens_processadas.mkdir(exist_ok=True)

        pastas_lotes_imagens = [x for x in caminhos_imagens_processadas.iterdir()]

        pdfs_por_lote = []

        for (x,path_lote_images) in enumerate(pastas_lotes_imagens):

            logging.info(f"Lote de imagens {x} .........")

            paths_images = [x for x in path_lote_images.iterdir()]

            caminho_pdf = f"{str(path_lote_images)}/{str(path_lote_images.name)}.pdf"

            pdf = Path(caminho_pdf)
            
            if pdf.exists():

                pdf.unlink()
                paths_images.pop()

            c = self.pdf.Canvas(caminho_pdf, pagesize=(595.27, 841.89))
        
            start = 0 
            end = len(paths_images) + 1
            passo = self.folha_imagem.quantidade_imagens_por_folha

            for page in range(start,end,passo):

                path_images_to_current_page = paths_images[page:page+passo]
                coordinates = self.folha_imagem.get_coordenadas_imagens()
                self.folha_imagem.desenhar_imagens_na_folha(c,path_images_to_current_page,coordinates)

                c.showPage()

            c.save()
            pdfs_por_lote.append(pdf)
            logging.info(pdf)
            logging.info(f"Gerado pdf {pdf.name}")

        logging.info("Fim de criação de pdfs .........")

        return pdfs_por_lote