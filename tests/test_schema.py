from schemas.vendas import VendasSchema

def test_vendas_dados_validos():
    from datetime import datetime
    

    # Criando um exemplo de dados válidos para o teste    
dados_validos = {
    "email": "comprador@exemplo.com",
    "data": datetime.now(),
    "valor": 100.50,
    "produto": "Produto Exemplo",
    "quantidade": 2,
    "categoria": "Categoria Exemplo",
}