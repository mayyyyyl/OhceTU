class Ohce:
    def chaine_miroir(self, langue, periode, mot):
        """ Renvoie la chaine en miroir en fonction de la langue """
        
        periode = self.periode_journee(langue, periode)
        chaine_miroir = mot[::-1]

        if langue == 'fr':
            if mot == chaine_miroir :
                return f"{periode['debut_chaine']} \n{chaine_miroir}  \nBien dit"
            else:
                return f"{periode['debut_chaine']} \n{chaine_miroir} \n{periode['fin_chaine']}"

        if langue == "en":
            if mot == chaine_miroir :
                return f"{periode['debut_chaine']} \n{chaine_miroir}  \nWell said"
            else:
                return f"{periode['debut_chaine']} \n{chaine_miroir} \n{periode['fin_chaine']}"
    