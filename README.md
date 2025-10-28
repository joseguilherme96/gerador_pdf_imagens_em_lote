# Processamento de Imagens em Lote para Redimensionamento e Inserção automática no PDF para Impressão
Está automação precisou ser desenvolvida para atender a necessidade de um cliente, devido ao grande numero de imagens que foram enviadas para inserção em folha A4, para geração de PDFs, e posteriormente a impressão realizada por conta do cliente, estes scripts se fez necessário para agilizar o trabalho onde este RPA cria todo fluxo desde o recebimento das imagens, passando pelo processo de redimensionamento e inserção em folha A4 de forma automática reduzindo o tempo que seria gasto se fosse realizado de forma manual.

## Funcionalidades
- O script redimensiona as imagens antes da inserção em folha `A4`
- O script gera automaticamente pdfs por lotes de imagens adicionadas na pasta `process`
- O script insere 4 imagens por folha

# Testes

Todo densenvolvimento do RPA foi realizado orientado a testes(TDD - Test-Driven Development), foi realizado diversos testes desde teste de simulação(mocks), passando por testes unitários até testes de integração que cobre todo o fluxo para geração dos pdfs da imagens adicionada para processamento em lote.

[![Testes](assets/testes.png "Testes")](assets/testes.png)

# Instale as dependências

Crie uma ambiente virtual na raiz do projeto adicionando a pasta `.venv`

Ative o ambiente virtual. E instale as dependências do projeto com o seguinte comando :

```sh

    pip install -r requirements.txt

```

# Execução do RPA

Salve suas imagens em lote(pastas) dentro da pasta `process`.

Na raiz do projeto execute :

```sh

    python processar.py

```

O script começará a processar as imagens fazendo o redimensionamento e inserção automática em folha A4 para impressão.

[![Processamento das imagens e geração de pdfs](assets/processamento_imagens_pdf.png "Processamento das imagens e geração de pdfs")](assets/processamento_imagens_pdf.png)

# PDF Gerado
[![Folha com as imagens inseridas](assets/folha_a4_com_imagens.png "Folha com as imagens inseridas")](assets/folha_a4_com_imagens.png)

# Principais conceitos aplicados

- Entendimento do problema e desenvolvimento de uma solução simples
- Desenvolvimento baseado em TDD(Test-Driven Development)
- Desenvolvimento baseado em um fluxo simples criado para o RPA, Recebimento das imagens enviadas pelo cliente->Processamento(Redimensionamento e Inserção no Pdf)->Geração de PDFs
- Implementação de logs
- Trabalhando com manipulação de arquivos
- Trabalhando com variaves de ambiente
- Trabalhando com a classe `os`
- Bibilotecas
- - Pillow
- - ReportLab
- Trabalhando com injeção de dependência
- Testes automatizados com Pytest
- - Testes com simulação(mocks)
- - Teste unitários
- - Testes de Integração
- Criação do arquivo de entrada processar.py para execução do RPA.



