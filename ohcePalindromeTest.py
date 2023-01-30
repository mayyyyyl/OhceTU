from main import Ohce
import parameterized
import unittest
import logging

logging.basicConfig(level="INFO")

class PalindromeTest(unittest.TestCase):

    @parameterized.parameterized.expand([("rotor")])
    def test_miroir(self, chaine):
        
        logging.info("Test miroir")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(chaine)

        self.assertIn(chaine[::-1], resultat)


if __name__ == '__main__':
    unittest.main()