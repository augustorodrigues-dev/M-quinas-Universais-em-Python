import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../implementacoes')))
from automato_pilha import AutomatoDePilha  

class TestAutomatoPilha(unittest.TestCase):
    def setUp(self):
        self.ap = AutomatoDePilha()

    def test_cadeias_aceitas(self):
        """Testa strings que DEVEM ser aceitas pelo autômato"""
        self.assertTrue(self.ap.processar("{[()]}"))
        self.assertTrue(self.ap.processar("()[]{}"))
        self.assertTrue(self.ap.processar("{[()[]{}()]}"))
        self.assertTrue(self.ap.processar("()"))

    def test_cadeias_rejeitadas_por_ordem(self):
        """Testa strings com erro de fechamento/ordem"""
        self.assertFalse(self.ap.processar("{(})"))
        self.assertFalse(self.ap.processar("{[(])}"))
        self.assertFalse(self.ap.processar(")(]"))

    def test_cadeias_rejeitadas_por_escopo_aberto(self):
        """Testa strings que terminam sem fechar tudo"""
        self.assertFalse(self.ap.processar("([]"))
        self.assertFalse(self.ap.processar("{[()}"))
        self.assertFalse(self.ap.processar("("))

if __name__ == '__main__':
    unittest.main()