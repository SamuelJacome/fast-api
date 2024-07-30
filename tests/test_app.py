from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_create_user(client):
    #act
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    #assert
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def read_user():
    # act
    response = client.get('/users/')
    # assert
    assert response.status_code == HTTPStatus.Ok
    assert response.json() == {
            "users": [
                {
                    'id': 1,
                    'username': 'alice',
                    'email': 'alice@example.com'
                }
            ]
    }


def test_update_user(client):
    #act
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    #assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    #act
    response = client.delete('/users/1')
    #assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}

def test_dado_um_id_de_usuario_que_nao_existe_o_response_deve_ser_not_found(client):
    #act
    response = client.put(
        '/users/10000',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        })
    #assert
    assert response.status_code == HTTPStatus.NOT_FOUND