from unittest.mock import Mock
from src.Imagem import Imagem
from src.Pdf import Pdf

def test_deve_converter_imagens_para_dimensoes_maxima_de_acordo_com_o_que_cabe_na_folha(mock_imagens_convertidas):

    assert len(mock_imagens_convertidas) == 30

def test_deve_inserir_imagens_convertidas_no_pdf(mock_imagens_convertidas,tmp_pdf):
    mock_pdf = Mock(spec=Pdf)

    mock_pdf.criar_pdf_com_imagens.return_value = tmp_pdf
    path_pdf = mock_pdf.criar_pdf_com_imagens()

    assert path_pdf.suffixes[0] == '.pdf'

