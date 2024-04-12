import unittest
from Vocales import cont_vocales

class TestVocales(unittest.TestCase):

    def test_1(self):
        result = cont_vocales("aloA")
        self.assertEqual(result, {'o':1, 'a':2})

    def test_2(self):
        result = cont_vocales("esdrújula")
        self.assertEqual(result,{'e':1, 'u':2, 'a':1})
    

    def test_3(self):
        result = cont_vocales("josé come")
        self.assertEqual(result,{'e':2, 'o':2})
    

    def test_4(self):
        result = cont_vocales("hAblar")
        self.assertEqual(result,{'a':2})

    
    def test_5(self):
        result = cont_vocales("comEr")
        self.assertEqual(result,{'e':1, 'o':1,})
    

    def test_6(self):
        result = cont_vocales("binario")
        self.assertEqual(result,{'i':2, 'a':1, 'o':1})
    

    def test_7(self):
        result = cont_vocales("universidad")
        self.assertEqual(result,{'u':1, 'i':2, 'e':1, 'a':1})

    
    def test_8(self):
        result = cont_vocales("rEctOradO")
        self.assertEqual(result,{'e':1, 'o':2, 'a':1})

    
    def test_9(self):
        result = cont_vocales("Mendoza")
        self.assertEqual(result,{'e':1, 'o':1, 'a':1})
    

    def test_10(self):
        result = cont_vocales("CelulAr")
        self.assertEqual(result,{'e':1, 'u':1, 'a':1})
unittest.main()
