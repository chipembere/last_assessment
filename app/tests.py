import unittest
from generator import get_random_idea

class Gen_Test(unittest.TestCase):
    def setUp(self):
        pass

    # love the fact these tests are here and run - but naming could be improved, currently ambiguous 
    def test_gen(self):
        act = get_random_idea()
        self.assertTrue(type(act) is tuple)
        #for pair in zip()

if __name__ == '__main__':
    unittest.main()