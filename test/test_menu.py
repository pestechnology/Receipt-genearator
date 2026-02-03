from menu import show_menu

def test_menu_items():
    menu = show_menu()
    assert len(menu) == 4
