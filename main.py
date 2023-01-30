class Ohce:
    def chaine_miroir(self, mot):
        """ Renvoie la chaine en miroir """
        
        chaine_miroir = mot[::-1]

        chaine_miroir = mot[::1]

        if mot == chaine_miroir:
            return f"Bonjour {chaine_miroir}  \n Bien dit"

        return f"Bonjour {chaine_miroir} \n Au revoir"