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
    
    @parameterized.parameterized.expand([("radar")])
    def test_palindrome(self, palindrome):

        logging.info("Test palindrome")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(palindrome)

        self.assertIn(palindrome, resultat)

        resultat_miroir = resultat[-8: len(resultat)]
        self.assertIn("Bien dit", resultat_miroir)


if __name__ == '__main__':
    unittest.main()