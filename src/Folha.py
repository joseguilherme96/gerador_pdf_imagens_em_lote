class Folha:

    def __init__(self,tipo_folha: str,comprimento:int,largura:int,margem_em_cada_lado:int):

        self.tipo_folha = tipo_folha
        self.comprimento = comprimento
        self.largura = largura
        self.margem_em_cada_lado = margem_em_cada_lado
        self.area_livre = None
        self.comprimento_livre = None
        self.largura_livre = None

    def calcular_area_livre(self):

        somatoria_margin_dois_lados = self.margem_em_cada_lado * 2
        self.area_livre = ((self.comprimento - somatoria_margin_dois_lados) * ( self.largura - somatoria_margin_dois_lados))

        return self.area_livre
    
    def calcular_largura_livre(self):

        somatoria_margin_dois_lados = self.margem_em_cada_lado * 2
        self.largura_livre = self.largura - somatoria_margin_dois_lados

        return self.largura_livre
    
    def calcular_comprimento_livre(self):

        somatoria_margin_dois_lados = self.margem_em_cada_lado * 2
        self.comprimento_livre = self.comprimento - somatoria_margin_dois_lados

        return self.comprimento_livre
