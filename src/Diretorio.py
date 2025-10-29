from pathlib import Path
from dotenv import load_dotenv

class Diretorio:

    def limpar_diretorio(nome):

        load_dotenv()

        BASE_DIR = Path(__file__).resolve().parent.parent
        pasta_processado = BASE_DIR / nome

        pastas = [x for x in pasta_processado.iterdir()]

        for pasta in pastas:

            imagens = [x for x in pasta.iterdir()]
            
            for imagem in imagens:

                imagem.unlink()

            pasta.rmdir()
