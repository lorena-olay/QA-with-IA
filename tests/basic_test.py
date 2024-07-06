import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 2), 3)

    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -2), -3)

if __name__ == '__main__':
    unittest.main()
