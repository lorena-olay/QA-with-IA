import unittest
import torch
import torch.nn as nn

class Modelo(nn.Module):
    def __init__(self):
        super(Modelo, self).__init__()
        self.lineal = nn.Linear(1, 1)
    
    def forward(self, x):
        return self.lineal(x)

class TestModeloPyTorch(unittest.TestCase):
    def test_prediccion(self):
        modelo = Modelo()
        entrada = torch.tensor([[10.0]])
        prediccion = modelo(entrada)
        self.assertIsNotNone(prediccion)

if __name__ == '__main__':
    unittest.main()
