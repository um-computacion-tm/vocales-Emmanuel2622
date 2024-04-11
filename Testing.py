import unittest
from Vocales import cont_vocales

class TestVocales(unittest.TestCase):

    def test_1(self):
        result = cont_vocales("aloA")
        self.assertEqual(result, {'o':1, 'a':2})

    def test_2(self):
        result = cont_vocales("esdrújula")
        self.assertEqual(result,{'e':1, 'u':2, 'a':1})
unittest.main()
