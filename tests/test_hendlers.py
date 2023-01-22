import pytest
from typing import Generator

from fastapi.testclient import TestClient

from api.database import Session
from api.models import Menu
from main import app


@pytest.fixture
def get_test_db() -> Generator:
    session = Session()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def test_client() -> Generator:
    client = TestClient(app)
    yield client


HOST = "http://127.0.0.1:8000/api/v1/"


def test_empty_menus(test_client: TestClient):
    response = test_client.get(f"{HOST}menus/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_menu(test_client: TestClient, get_test_db):
    request_test_menu = {
        "title": "My menu 1",
        "description": "My menu description 1"
    }
    response = test_client.post(f"{HOST}menus/", json=request_test_menu)
    assert response.status_code == 201
    assert response.json()["title"] == "My menu 1"
    assert response.json()["description"] == "My menu description 1"
    assert isinstance(response.json()["id"], str)
    assert response.json()["submenus_count"] == 0
    assert response.json()["dishes_count"] == 0
    menu_id = response.json()["id"]
    _menu = get_test_db.query(Menu).first()
    assert str(_menu.id) == menu_id

# def test_get_menu(test_app):
#     response = test_app.get(f"{HOST}menus/{menu_id}/")
#     assert response.status_code == 200
#     assert response.json()["title"] == "My menu 1"
#     assert response.json()["description"] == "My menu description 1"
#     assert response.json()["submenus_count"] == 0
#     assert response.json()["dishes_count"] == 0
#
#
# def test_update_menu(test_app):
#     request_test_menu = {
#         "title": "My update_menu 1",
#         "description": "My menu update_description 1"
#     }
#     response = test_app.patch(
#         f"{HOST}menus/{menu_id}/",
#         content=json.dumps(request_test_menu)
#     )
#     assert response.status_code == 200
#     assert response.json()["title"] == "My updated menu 1"
#     assert response.json()["description"] == "My menu updated description 1"
#     assert response.json()["submenus_count"] == 0
#     assert response.json()["dishes_count"] == 0
#
#
# def test_delete_menu(test_app):
#     response = test_app.delete(f"{HOST}menus/{menu_id}/")
#     assert response.status_code == 200
#     assert response.json() == {
#         "status": True,
#         "message": "The menu has been deleted"
#     }
#
#
# def test_empty_submenus(test_app):
#     response = test_app.get(
#         f"{HOST}menus/{menu_id}/submenus/"
#     )
#     assert response.status_code == 200
#     assert response.json() == []
#
#
# def test_create_submenu(test_app):
#     request_test_menu = {
#         "title": "My submenu 1",
#         "description": "My submenu description 1"
#     }
#     response = test_app.post(
#         f"{HOST}menus/{menu_id}/submenus/",
#         content=json.dumps(request_test_menu)
#     )
#     global submenu_id
#     submenu_id = response.json()["id"]
#     assert response.status_code == 201
#     assert response.json()["title"] == "My submenu 1"
#     assert response.json()["description"] == "My submenu description 1"
#     assert response.json()["dishes_count"] == 0
#
#
# def test_get_submenu(test_app):
#     response = test_app.get(
#         f"{HOST}menus/{menu_id}/submenus/{submenu_id}/")
#     assert response.status_code == 200
#     assert response.json()["title"] == "My submenu 1"
#     assert response.json()["description"] == "My submenu description 1"
#     assert response.json()["dishes_count"] == 0
#
#
# def test_update_submenu(test_app):
#     request_test_menu = {
#         "title": "My updated submenu 1",
#         "description": "My updated submenu description 1"
#     }
#     response = test_app.patch(
#         f"{HOST}menus/{menu_id}/submenus/{submenu_id}/",
#         content=json.dumps(request_test_menu)
#     )
#     assert response.status_code == 200
#     assert response.json()["title"] == "My updated submenu 1"
#     assert response.json()["description"] == "My updated submenu description 1"
#     assert response.json()["dishes_count"] == 0
#
#
# def test_delete_submenu(test_app):
#     response = test_app.delete(
#         f"{HOST}menus/{menu_id}/submenus/{submenu_id}/")
#     assert response.status_code == 200
#     assert response.json() == {
#         "status": True,
#         "message": "The menu has been deleted"
#     }
#
#
# def test_empty_dishes(test_app):
#     response = test_app.get(
#         f"{HOST}menus/{menu_id}/submenus/{submenu_id}/dishes/"
#     )
#     assert response.status_code == 200
#     assert response.json() == []
#
#
# def test_create_dish(test_app):
#     request_test_menu = {
#         "title": "My dish 1",
#         "description": "My dish description 1",
#         "price": 12.5
#     }
#     response = test_app.post(
#         f"{HOST}menus/{menu_id}/submenus/{submenu_id}/dishes/",
#         content=json.dumps(request_test_menu)
#     )
#     global dish_id
#     dish_id = response.json()["id"]
#     assert response.status_code == 201
#     assert response.json()["title"] == "My dish 1"
#     assert response.json()["description"] == "My dish description 1"
#     assert response.json()["price"] == "12.5"
#
#
# def test_get_dish(test_app):
#     response = test_app.get(
#         f"{HOST}menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/"
#     )
#     assert response.status_code == 200
#     assert response.json()["title"] == "My dish 1"
#     assert response.json()["description"] == "My dish description 1"
#     assert response.json()["price"] == "12.5"
#
#
# def test_update_dish(test_app):
#     request_test_menu = {
#         "title": "My updated dish 1",
#         "description": "My updated dish description 1",
#         "price": 14.5
#     }
#     response = test_app.patch(
#         f"{HOST}menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/",
#         content=json.dumps(request_test_menu)
#     )
#     assert response.status_code == 200
#     assert response.json()["title"] == "My updated dish 1"
#     assert response.json()["description"] == "My updated dish description 1"
#     assert response.json()["price"] == "14.5"
#
#
# def test_delete_dish(test_app):
#     response = test_app.delete(
#         f"{HOST}menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/")
#     assert response.status_code == 200
#     assert response.json() == {
#         "status": True,
#         "message": "The menu has been deleted"
#     }
