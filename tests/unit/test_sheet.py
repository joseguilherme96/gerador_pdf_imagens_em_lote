from src.Folha import Folha
from pytest import fixture,mark

def test_calcular_area_livre():

    quantidade_de_imagens_por_folha = 6
    
    folha = Folha(tipo_folha="A4",comprimento=210,largura=297,margem_em_cada_lado=30)

    assert 35550 == folha.calcular_area_livre()

