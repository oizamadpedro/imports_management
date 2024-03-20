import requests, json
import pytest
ENDPOINT = "http://localhost:8000/v1/products/"

@pytest.fixture
def payload():
    return {
        "product": "Produto Teste Pytest",
        "quantity": 3,
        "description": "produto testando descrição..."
    }

@pytest.fixture
def created_product(payload):
    create_product_response = requests.post(ENDPOINT, json=payload)
    data = json.loads(create_product_response.json())
    created_product = data['data'][0]
    assert created_product['product'] == payload['product']
    assert create_product_response.status_code == 201
    yield created_product  # A fixture retorna o produto criado
    # O código abaixo será executado após o teste, removendo o produto criado
    print(created_product['id'])
    delete_product_response = requests.delete(ENDPOINT + str(created_product['id']))
    print(delete_product_response.json())
    assert delete_product_response.status_code == 200

def test_getById(created_product):
    # Utiliza o produto criado para realizar verificações de get
    print(created_product['id'])
    response = requests.get(ENDPOINT + str(created_product['id']))
    assert response.status_code == 200
    data = json.loads(response.json())
    assert data['data'][0]['product'] == created_product['product']

def test_falha_em_pegar_produto_nao_existente():
    response = requests.get(ENDPOINT + "99999")
    data = json.loads(response.json())
    assert response.status_code == 404
    assert "error" in data
    assert data['status'] == 404
    assert data['error']['message'] == "product not found"

def test_get_all_products(created_product):
    response = requests.get(ENDPOINT)
    data = json.loads(response.json())
    assert data['data'][-1]['product'] == created_product['product']
    assert data['status'] == 200
    assert response.status_code == 200

def test_fail_delete_product_not_exist():
    response = requests.delete(ENDPOINT + "9128319082")
    data = json.loads(response.json())
    assert response.status_code == 404
    assert "error" in data
    assert data['status'] == 404
    assert data['error']['message'] == "product not found"

def test_get_products():
    response = requests.get(ENDPOINT, verify=False)
    data = json.loads(response.json())
    assert response.status_code == 200
    assert "data" in data
    assert len(data['data']) > 0
