# Pastas para armazenamento das imagens

Estas pastas `received, process e processed` fazem parte do fluxo do RPA para salvar o recebimento das imagens do cliente, imagens que entraram em processamento e as imagens que foram redimensionadas e inseridas no pdf.

## Pasta `received`

É uma pasta que salva todas as imagens recebidas do cliente, é uma forma bruta de salvar as imagens mantendo o histórico das imagens originais envidadas pelo cliente.

## Pasta `process`

É a pasta que salva todas as imagens em lote(pastas) que serão processadas para inserção automática no pdf após seu redimensionamento.

Ao salvar as imagens em grupo de pastas dentro da pasta `process`, automaticamente o script irá entender que são lotes de imagens para processamento.

## Pasta `processed`

Armazena todos os lotes de imagens que foram processadas e inseridas no pdf. Cada pasta contém as imagens e o pdf gerado.

Após a execução do RPA na pasta root pelo comando :

```sh
    python processar.py
```

Você terá a seguinte estrutura :

```sh

gerador_pdf_imagens_em_lote/
│
├── resize/                     # Diretório principal responsável pelo fluxo completo do processamento
│
│   ├── received/               # Onde as imagens originais são recebidas para iniciar o processo
│   │   ├── lote0/              # Cada lote representa um grupo de imagens a serem processadas
│   │   │   ├── imagem_exemplo.png
│   │   │   └── imagem_exemplo - Copia.png
│   │   └── lote1/
│   │       ├── imagem_exemplo.png
│   │       └── imagem_exemplo - Copia.png
│   │
│   ├── process/                # Onde as imagens são guardadas para serem processadas(redimensionamento e inserção no pdf)
│   │   ├── lote0/
│   │   │   ├── imagem_exemplo.png
│   │   │   └── imagem_exemplo - Copia.png
│   │   └── lote1/
│   │       ├── imagem_exemplo.png
│   │       └── imagem_exemplo - Copia.png
│   │
│   └── processed/              # Onde ficam os resultados finais (PDFs e imagens geradas)
│       ├── lote0/
│       │   ├── lote0.pdf       # PDF final gerado com as imagens do lote
│       │   ├── ss_0.jpg        # Capturas de tela ou imagens intermediárias de verificação
│       │   └── ss_1.jpg
│       └── lote1/
│           ├── lote1.pdf
│           ├── ss_0.jpg
│           └── ss_1.jpg


```

