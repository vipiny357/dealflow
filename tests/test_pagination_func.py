from app.main import get_page_size

def test_get_page_size():
    # Test case 1 Page number 1, page size 10
    initial_value, last_value = get_page_size(1, 10)
    assert initial_value == 0
    assert last_value == 10

    # Test case 2 Page number 2, page size 20
    initial_value, last_value = get_page_size(2, 20)
    assert initial_value == 20
    assert last_value == 40
