import requests
import random

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from tests import schemas


def test_get_all_todos_status_code():
    response = requests.get("http://localhost:8000/todos")
    assert response.status_code == 200


def test_get_all_todos_content_type_header_response_value():
    response = requests.get("http://localhost:8000/todos")

    assert response.headers["Content-Type"] == 'application/json'


def test_get_all_todos_response_data_validation():
    response = requests.get("http://localhost:8000/todos")
    response_data = response.json()[1]

    assert response_data["id"] == 2
    assert response_data["description"] == "fastapi project"
    assert response_data["complete"] is False
    assert response_data["priority"] == 1
    assert response_data["title"] == "learn python"


def test_get_all_todos_json_schema():
    response = requests.get("http://localhost:8000/todos")
    try:
        validate(instance=response.json()[0], schema=schemas.GET_ALL_TODOS_SCHEMA)
    except ValidationError as e:
        assert False, e
    except Exception as err:
        raise Exception(err.__str__())


def test_get_todo_by_id_status_code():
    response = requests.get("http://localhost:8000/todo/1")

    assert response.status_code == 200


def test_get_todo_by_id_content_type_header_response_value():
    response = requests.get("http://localhost:8000/todo/1")

    assert response.headers["Content-Type"] == 'application/json'


def test_get_todo_by_id_data_validation():
    response = requests.get("http://localhost:8000/todo/3")
    response_data = response.json()

    assert response_data["id"] == 3
    assert response_data["description"] == "code and sport"
    assert response_data["complete"] is False
    assert response_data["priority"] == 2
    assert response_data["title"] == "train everyday"


def test_get_todo_by_id_json_schema():
    response = requests.get("http://localhost:8000/todo/1")
    try:
        validate(instance=response.json(), schema=schemas.GET_TODO_BY_ID_SCHEMA)
    except ValidationError as e:
        assert False, e
    except Exception as err:
        raise Exception(err.__str__())


def test_get_todo_by_id_not_existing_id():
    response = requests.get(f"http://localhost:8000/todo/{random.randint(1000,2000)}")

    assert response.status_code == 404
    assert response.text == '{"detail":"Todo not found"}'


def test_get_todo_by_id_use_wrong_type():
    response = requests.get("http://localhost:8000/todo/string")

    assert response.status_code == 422
    assert response.text == '{"detail":[{"loc":["path","todo_id"],"msg":"value is not a valid integer","type":"type_error.integer"}]}'
