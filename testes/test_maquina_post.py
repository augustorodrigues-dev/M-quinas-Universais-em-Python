import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../implementacoes')))
from maquina_post import MaquinaDePost  

class TestMaquinaPost(unittest.TestCase):
    def setUp(self):
        self.mp = MaquinaDePost()

    def test_cadeias_aceitas(self):
        """Testa strings que seguem estritamente a^n b^n c^n com n >= 1"""
        self.assertTrue(self.mp.processar("abc"))          
        self.assertTrue(self.mp.processar("aabbcc"))      
        self.assertTrue(self.mp.processar("aaabbbccc"))  

    def test_cadeias_rejeitadas_por_proporcao(self):
        """Testa strings com contagem desigual de elementos (n inválido)"""
        self.assertFalse(self.mp.processar("aabbc"))     
        self.assertFalse(self.mp.processar("abbcc"))     
        self.assertFalse(self.mp.processar("aabcc"))     
        self.assertFalse(self.mp.processar("aabbccc"))   

    def test_cadeias_rejeitadas_por_ordem(self):
        """Testa strings com as letras certas, mas fora de ordem estrutural"""
        self.assertFalse(self.mp.processar("abca"))     
        self.assertFalse(self.mp.processar("cbaf"))      
        self.assertFalse(self.mp.processar("bca"))       

    def test_cadeias_vazias_ou_invalidas(self):
        """Testa casos de borda como strings vazias ou caracteres fora do alfabeto"""
        self.assertFalse(self.mp.processar(""))          
        self.assertFalse(self.mp.processar("xyz"))        

if __name__ == '__main__':
    unittest.main()