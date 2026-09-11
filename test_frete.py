import pytest
from frete import calcular_frete

# >_Conecta com: Atende RF-01 e RB-01
def test_frete_gratis_padrao():
    assert calcular_frete(valor_carrinho=250.0, regiao="Sudeste") == 0.0

# >_ Conecta com: Atende RF-01 e RB-01
def test_frete_gratis_regiao_norte():
    assert calcular_frete(valor_carrinho=300.0, regiao="Norte") == 0.0

# >_ Conecta com: Atende RB-02
def test_cobrar_taxa_abaixo_limite():
    assert calcular_frete(valor_carrinho=150.0, regiao="Sudeste") == 20.0

# >_ Conecta com: Atende RB-03
def test_valor_carrinho_invalido():
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_frete(valor_carrinho=0.0, regiao="Sudeste")