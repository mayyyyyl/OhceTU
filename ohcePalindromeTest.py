from main import Ohce
import parameterized
import unittest
import logging

logging.basicConfig(level="INFO")

class PalindromeTest(unittest.TestCase):

    @parameterized.parameterized.expand([("rotor")])
    def test_miroir(self, chaine):
        
        logging.info("Test miroir")

        # QUAND on saisit une chaîne
        ohce = Ohce()
        resultat = ohce.chaine_miroir(chaine)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaine[::-1], resultat)
    
    @parameterized.parameterized.expand([("radar")])
    def test_palindrome(self, palindrome):

        logging.info("Test palindrome")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(palindrome)

        self.assertIn(palindrome, resultat)

        # ET 'Bien dit' est renvoyé ensuite
        resultat_miroir = resultat[-8: len(resultat)]
        self.assertIn("Bien dit", resultat_miroir)
    
    @parameterized.parameterized.expand([("hibou")])
    def test_pas_palindrome(self, mot):

        logging.info("Test pas palindrome")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(mot)

        # ALORS celle-ci n'est pas renvoyée en miroir
        self.assertNotIn(mot, resultat)


if __name__ == '__main__':
    unittest.main()