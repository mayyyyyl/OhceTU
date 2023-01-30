class Ohce:
    def chaine_miroir(self, langue, mot):
        """ Renvoie la chaine en miroir en fonction de la langue """
        
        chaine_miroir = mot[::-1]

        if langue == 'fr':
            if mot == chaine_miroir :
                return f"Bonjour \n{chaine_miroir}  \nBien dit"
            else:
                return f"Bonjour \n{chaine_miroir} \nAu revoir"

        if langue == "en":
            if mot == chaine_miroir :
                return f"Hello \n{chaine_miroir}  \nWell said"
            else:
                return f"Hello \n{chaine_miroir} \nGood Bye"
