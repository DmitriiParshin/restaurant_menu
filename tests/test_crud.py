from tests import test_hendlers
from tests.test_hendlers import test_client, get_test_db


def test_menu():
    test_hendlers.test_empty_menus(test_client, get_test_db)
    test_hendlers.test_create_menu(test_client, get_test_db)
    test_hendlers.test_get_menu(test_client, get_test_db)
    test_hendlers.test_update_menu(test_client, get_test_db)
    test_hendlers.test_delete_menu(test_client, get_test_db)


def test_submenu():
    test_hendlers.test_empty_menus(test_client, get_test_db)
    test_hendlers.test_create_menu(test_client, get_test_db)
    test_hendlers.test_get_menu(test_client, get_test_db)
    test_hendlers.test_update_menu(test_client, get_test_db)
    test_hendlers.test_empty_submenus(test_client, get_test_db)
    test_hendlers.test_create_submenu(test_client, get_test_db)
    test_hendlers.test_get_submenu(test_client, get_test_db)
    test_hendlers.test_update_submenu(test_client, get_test_db)
    test_hendlers.test_delete_submenu(test_client, get_test_db)
    test_hendlers.test_delete_menu(test_client, get_test_db)


def test_dish():
    test_hendlers.test_empty_menus(test_client, get_test_db)
    test_hendlers.test_create_menu(test_client, get_test_db)
    test_hendlers.test_get_menu(test_client, get_test_db)
    test_hendlers.test_update_menu(test_client, get_test_db)
    test_hendlers.test_empty_submenus(test_client, get_test_db)
    test_hendlers.test_create_submenu(test_client, get_test_db)
    test_hendlers.test_get_submenu(test_client, get_test_db)
    test_hendlers.test_update_submenu(test_client, get_test_db)
    test_hendlers.test_empty_dishes(test_client, get_test_db)
    test_hendlers.test_create_dish(test_client, get_test_db)
    test_hendlers.test_get_dish(test_client, get_test_db)
    test_hendlers.test_update_dish(test_client, get_test_db)
    test_hendlers.test_delete_dish(test_client, get_test_db)
    test_hendlers.test_delete_submenu(test_client, get_test_db)
    test_hendlers.test_delete_menu(test_client, get_test_db)
