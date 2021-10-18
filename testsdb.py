import os
import unittest
from dbconnector import Conexao


class TestCaseDB(unittest.TestCase):
    def setUp(self) -> None:
        os.environ['senhadb'] = 'Digo1660!'
        novaconexao = Conexao()
        self.conn = novaconexao.conectar()
    def test_something(self):
        self.assertTrue(self.conn, "São iguais. Deu certo")  # add assertion here


if __name__ == '__main__':
    unittest.main()
