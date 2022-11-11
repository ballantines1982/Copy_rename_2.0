import unittest
from trail_n_error import InputFrame

class Testing(unittest.TestCase):
    def test_label(self):
        InputFrame.calc_stuff.antal = 10.50
        InputFrame.calc_stuff.inpris = 5
        inprisTot = InputFrame.calc_stuff.antal * InputFrame.calc_stuff.inpris
        self.assertEqual(inprisTot, 52.5)

if __name__ == '__main__':
    unittest.main()