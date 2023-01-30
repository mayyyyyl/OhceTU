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
    
    @parameterized.parameterized.expand([("hibou")])
    def test_pas_palindrome(self, mot):

        logging.info("Test pas palindrome")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(mot)

        self.assertNotIn(mot, resultat)

        resultat_mirroir_debut = resultat[0:7]
        resultat_mirroir_fin = resultat[-9:len(resultat)]
        self.assertIn("Bonjour", resultat_mirroir_debut)
        self.assertIn("Au revoir", resultat_mirroir_fin)


if __name__ == '__main__':
    unittest.main()