"""
class Pessoa:
    __init__
        nome: str
        sobrenome: str
        dados_obtidos: bool

    API
        obter_todos_os_dados -> method
            OK
            404
"""

import unittest
from unittest.mock import patch
from pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Bruno', 'Volpe')

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'bruno')

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'bruno')

    def test_pessoa_attr_dados_obtidos_deve_ter_false(self):
        self.assertFalse(self.p1.dados_obtidos, 'bruno')

    def test_pessoa_attr_nome_eh_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_eh_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.asserEqual(self.p1.obter_todos_os_dados(), 'conectado')
            SELF.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.asserEqual(self.p1.obter_todos_os_dados(), 'erro 404')


if __name__ == '__main__':
    unittest.main(verbosity=2)
