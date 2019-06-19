from unittest.mock import MagicMock

from sample import read_file


def test_non_existing_file(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='hello')
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    c = read_file('foo.txt')
    assert c == 'hello'
    mock_open.assert_called_once()
    mock_file.readline.assert_called_once()
