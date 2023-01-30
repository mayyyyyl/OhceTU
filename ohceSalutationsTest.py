from main import Ohce
import parameterized
import unittest
import logging

logging.basicConfig(level="INFO")

class SalutationsTest(unittest.TestCase):
    @parameterized.parameterized.expand([("fr", "hibou", "Bonjour"), ("en", "hibou", "Hello")])    
    def test_bonjour(self, langue, mot, debut_chaine):

        logging.info("Test bonjour")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(langue, mot)

        self.assertNotIn(mot, resultat)

        resultat_mirroir_debut = resultat[0:len(debut_chaine)]
        self.assertIn(debut_chaine, resultat_mirroir_debut)
    
    
    @parameterized.parameterized.expand([("fr", "hibou", "Au revoir"), ("en", "hibou", "Good Bye")])  
    def test_aurevoir(self, langue, mot, fin_chaine):

        logging.info("Test au revoir")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(langue, mot)

        self.assertNotIn(mot, resultat)

        resultat_mirroir_fin = resultat[-len(fin_chaine):len(resultat)]
        self.assertIn(fin_chaine, resultat_mirroir_fin)

if __name__ == '__main__':
    unittest.main()