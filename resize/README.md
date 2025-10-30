# Pastas para armazenamento das imagens

Estas pastas `received, process e processed` fazem parte do fluxo do RPA para salvar o recebimento das imagens do cliente, imagens que entraram em processamento e as imagens que foram redimensionadas e inseridas no pdf.

## Pasta `received`

É uma pasta que salva todas as imagens recebidas do cliente, é uma forma bruta de salvar as imagens mantendo o histórico das imagens originais envidadas pelo cliente.

## Pasta `process`

É a pasta que salva todas as imagens em lote(pastas) que serão processadas para inserção automática no pdf após seu redimensionamento.

Ao salvar as imagens em grupo de pastas dentro da pasta `process`, automaticamente o script irá entender que são lotes de imagens para processamento.

## Pasta `production/processed`

Armazena todos os lotes de imagens que foram processadas e inseridas no pdf. Cada pasta contém as imagens e o pdf gerado.

Crie uma pasta chamada `production/process`e salve suas imagens em lote(pastas) dentro da pasta `production/process` confome hierarquia abaixo.

```sh

gerador_pdf_imagens_em_lote/
├── resize/ 
    ├── production
        ├── process/                # Onde as imagens são guardadas para serem processadas(redimensionamento e inserção no pdf)
        │   ├── lote0/
        │   │   ├── imagem_exemplo.png
        │   │   └── imagem_exemplo - Copia.png
        │   └── lote1/
        │       ├── imagem_exemplo.png
        │       └── imagem_exemplo - Copia.png
        ├── process/                # Onde as imagens são guardadas para serem processadas(redimensionamento e inserção no pdf) que podem ser organizadas.
        │   ├── lote0/
        │   │   ├── imagem_exemplo.png
        │   │   └── imagem_exemplo - Copia.png
        │   └── lote1/
        │       ├── imagem_exemplo.png
        │       └── imagem_exemplo - Copia.png
        ├── processed/              # Onde ficam os resultados finais (PDFs e imagens geradas)
        │   ├── lote0/
        │   │   ├── lote0.pdf       # PDF final gerado com as imagens do lote
        │   │   ├── imagem_exemplo.jpg        # Capturas de tela ou imagens intermediárias de verificação
        │   │   └── imagem_exemplo - Copia.jpg
        │   └── lote1/
        │       ├── lote1.pdf
        │       ├── imagem_exemplo.jpg
        │       └── imagem_exemplo - Copia.jpg

```

Execute o RPA na pasta root com o comando :

```sh

    set ENV_FOR_DYNACONF=production && python processar.py

```

