import json
import uuid

from sqlalchemy import true


menu_id: uuid.UUID


def test_get_all(test_app):
    response = test_app.get("http://127.0.0.1:8000/api/v1/menus/")
    assert response.status_code == 200
    assert response.json() == []


def test_create(test_app):
    request_test_menu = {
        "title": "My menu 1",
        "description": "My menu description 1"
    }
    response = test_app.post(
        "http://127.0.0.1:8000/api/v1/menus/",
        content=json.dumps(request_test_menu)
    )
    global menu_id
    menu_id = response.json()["id"]
    assert response.status_code == 201
    assert response.json()["title"] == "My menu 1"
    assert response.json()["description"] == "My menu description 1"
    assert response.json()["submenus_count"] == 0
    assert response.json()["dishes_count"] == 0


def test_get_by_id(test_app):
    response = test_app.get(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "My menu 1"
    assert response.json()["description"] == "My menu description 1"
    assert response.json()["submenus_count"] == 0
    assert response.json()["dishes_count"] == 0


def test_update(test_app):
    request_test_menu = {
        "title": "My menu 1",
        "description": "My menu description 1"
    }
    response = test_app.patch(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}",
        content=json.dumps(request_test_menu)
    )
    assert response.status_code == 200
    assert response.json()["title"] == "My menu 1"
    assert response.json()["description"] == "My menu description 1"
    assert response.json()["submenus_count"] == 0
    assert response.json()["dishes_count"] == 0


def test_delete(test_app):
    response = test_app.delete(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}")
    assert response.status_code == 200
    assert response.json() == {
        "status": True,
        "message": "The menu has been deleted"
    }
