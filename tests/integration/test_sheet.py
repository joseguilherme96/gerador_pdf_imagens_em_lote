from src.Folha import Folha
from src.FolhaImagem import FolhaImagem
from pytest import mark

@mark.parametrize("quantidade_de_imagens_por_folha, comprimento_maximo_esperado_imagem,largura_maxima_esperada_imagem",
                  [
                      (3,75,118.5),
                      (5,75,79),
                      (6,75,79)
                  ],)
def test_deve_retornar_dimensoes_maximas_que_a_imagem_pode_ser_colocada_na_folha(quantidade_de_imagens_por_folha,comprimento_maximo_esperado_imagem,largura_maxima_esperada_imagem):

    folha = Folha(tipo_folha="A4",comprimento=210,largura=297,margem_em_cada_lado=30)

    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=quantidade_de_imagens_por_folha)

    comprimento,largura = folha_imagem.calcular_comprimento_largura_maxima_imagem()

    assert comprimento == comprimento_maximo_esperado_imagem
    assert largura == largura_maxima_esperada_imagem

@mark.parametrize("quantidade_de_imagens_por_folha, quantidade_linhas_esperado,quantidade_colunas_esperadas",
                  [
                      (3,2,2),
                      (5,3,2),
                      (6,3,2)
                  ],)
def test_deve_retornar_a_quantidade_de_linhas_colunas_que_a_folha_tera_para_inserir_as_imagens(quantidade_de_imagens_por_folha,quantidade_linhas_esperado,quantidade_colunas_esperadas):

    folha = Folha(tipo_folha="A4",comprimento=210,largura=297,margem_em_cada_lado=30)

    folha_imagem = FolhaImagem(folha,quantidade_imagens_por_folha=quantidade_de_imagens_por_folha)

    quantidade_linhas,quantidade_colunas = folha_imagem.criar_linhas_colunas_para_inserir_imagens()

    assert quantidade_linhas == quantidade_linhas_esperado
    assert quantidade_colunas == quantidade_colunas_esperadas

