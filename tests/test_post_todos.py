import json
import requests


def test_post_todo_status_code():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "description": "continuous learning",
        "priority": 1,
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 201
    assert response.text == '{"status":201,"transaction":"Successful"}'


def test_post_todo_by_id_content_type_header_response_value():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "description": "continuous learning",
        "priority": 1,
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo", data=payload)

    assert response.headers["Content-Type"] == 'application/json'


def test_post_todo_missing_optional_field_description():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "priority": "1",
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 201
    assert response.text == '{"status":201,"transaction":"Successful"}'


def test_post_todo_missing_required_field_title():
    payload = json.dumps({
        "description": "continuous learning",
        "priority": 1,
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 422


def test_post_todo_missing_required_field_priority():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "description": "continuous learning",
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 422


def test_post_todo_missing_required_field_complete():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "description": "continuous learning",
        "priority": 1,
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 422


def test_post_todo_autoconvert_to_the_expected_type_priority_string():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "description": "continuous learning",
        "priority": "1",
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 201
    assert response.text == '{"status":201,"transaction":"Successful"}'


def test_post_todo_autoconvert_to_the_expected_type_complete_string():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "description": "continuous learning",
        "priority": 1,
        "complete": "False"
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 201
    assert response.text == '{"status":201,"transaction":"Successful"}'


def test_post_todo_autoconvert_to_the_expected_type_title_int():
    payload = json.dumps({
        "title": 213,
        "description": "continuous learning",
        "priority": 1,
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 201
    assert response.text == '{"status":201,"transaction":"Successful"}'


def test_post_todo_special_special_chars():
    payload = json.dumps({
        "title": '!@#$%^&*(*)_+',
        "description": "±§/.']}{[-=",
        "priority": 1,
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 201
    assert response.text == '{"status":201,"transaction":"Successful"}'


def test_post_todo_special_spaces():
    payload = json.dumps({
        "title": ' ',
        "description": " ",
        "priority": 1,
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 201
    assert response.text == '{"status":201,"transaction":"Successful"}'


def test_post_todo_priority_less_than_1():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "description": "continuous learning",
        "priority": 0,
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 422
    assert response.reason == 'Unprocessable Entity'


def test_post_todo_priority_greater_than_5():
    payload = json.dumps({
        "title": "Focus on backend & automation testing",
        "description": "continuous learning",
        "priority": 6,
        "complete": False
    })
    response = requests.post(url="http://localhost:8000/todo",
                             data=payload)

    assert response.status_code == 422
    assert response.reason == 'Unprocessable Entity'