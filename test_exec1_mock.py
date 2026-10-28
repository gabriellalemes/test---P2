from unittest.mock import patch

from exe1_mock import obter_nome


def test_obter_nome():
    with patch("exe1_mock.buscar_nome", return_value={"id": 1, "nome": "Gabriel Rafael"}) as mock_buscar_nome:
        nome = obter_nome(1)
        assert nome["nome"] == "Gabriel Rafael"
        mock_buscar_nome.assert_called_once_with(1)