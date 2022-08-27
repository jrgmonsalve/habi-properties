from src.shared.utilities import extrac_params_from_path


def test_extrac_params_from_path_ok():
    # Arrange
    path = "/property?key1=value1&key2=123"
    expected = [{
        "key": "key1",
        "value": "value1"
    }, {
        "key": "key2",
        "value": "123"
    }]

    # Act
    obtained = extrac_params_from_path(path)

    # Assert
    assert obtained == expected


def test_extrac_param_from_path_ok():
    # Arrange
    path = "/property?key1=value1"
    expected = [{
        "key": "key1",
        "value": "value1"
    }]

    # Act
    obtained = extrac_params_from_path(path)

    # Assert
    assert obtained == expected


def test_extrac_none_params_from_path_empty_result():
    # Arrange
    path = "/property"
    expected = []

    # Act
    obtained = extrac_params_from_path(path)

    # Assert
    assert obtained == expected
