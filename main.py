class Ohce:
    def chaine_miroir(self, mot):
        """ Renvoie la chaine en miroir """
        
        chaine_miroir = mot[::-1]

        if mot == chaine_miroir:
            return f"{chaine_miroir}  \nBien dit"

        return f"{chaine_miroir} \n"