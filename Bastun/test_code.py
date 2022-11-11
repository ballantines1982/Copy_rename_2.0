import unittest
from bastun_final import Bastu

class TestFahrToCel(unittest.TestCase):
    
    def test_inputFahrInt(self):
        app = Bastu()
        result = app.fahr_to_cel(50)
        self.assertEqual(result, 10)
        result = app.fahr_to_cel(30)
        self.assertEqual(result, -1.11)
        result = app.fahr_to_cel(100)
        self.assertEqual(result, 37.78)
        
    def test_float_Exception(self):
        app = Bastu()
        self.assertRaises(TypeError, app.fahr_to_cel(10.0))
        
        
if __name__ == '__main__':
    unittest.main()