from src.schemas import Vendas, Categoria
import pytest
from datetime import datetime
from pydantic import ValidationError


def test_vendas_dados_validos():
    from datetime import datetime


    # Criando um exemplo de dados válidos para o teste    
    dados_validos = {
        "email": "comprador@exemplo.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto Exemplo",
        "quantidade": 2,
        "categoria": "Categoria 1",
    }
    venda = Vendas(**dados_validos)

    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]