from ohce import Ohce
import parameterized
import unittest
import logging

logging.basicConfig(level="INFO")

class SalutationsTest(unittest.TestCase):
    @parameterized.parameterized.expand([
    ("fr", "hibou", "matin", "Bonjour"),
    ("en", "hibou", "matin", "Good Morning"),
    ("fr", "hibou", "soir", "Bonsoir"),
    ("en", "hibou", "nuit", "Good Night")
    ])    
    def test_bonjour(self, langue, mot, periode, debut_chaine):

        logging.info("Test bonjour")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(langue, periode, mot)

        self.assertNotIn(mot, resultat)

        resultat_mirroir_debut = resultat[0:len(debut_chaine)]
        self.assertIn(debut_chaine, resultat_mirroir_debut)
    
    
    @parameterized.parameterized.expand([
    ("fr", "hibou", "matin", "Au revoir"),
    ("en", "hibou", "matin", "Good Bye"),
    ("fr", "hibou", "soir", "Bonne Nuit"),
    ("en", "hibou", "nuit", "bye bye")
    ])  
    def test_aurevoir(self, langue, mot, periode, fin_chaine):

        logging.info("Test au revoir")

        ohce = Ohce()
        resultat = ohce.chaine_miroir(langue, periode, mot)

        self.assertNotIn(mot, resultat)

        resultat_mirroir_fin = resultat[-len(fin_chaine):len(resultat)]
        self.assertIn(fin_chaine, resultat_mirroir_fin)


if __name__ == '__main__':
    unittest.main()