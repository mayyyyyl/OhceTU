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
    
    def periode_journee(self, langue, periode):
        """ Renvoie les salutations suivant la période de la journée """

        if langue == "fr":
            match periode:
                case "matin":
                    return {"debut_chaine":"Bonjour","fin_chaine": "Au revoir"}
                case "soir":
                    return {"debut_chaine":"Bonsoir","fin_chaine": "Bonne Nuit"}
                case "default":
                    return {"debut_chaine":"Bien le bonjour","fin_chaine": "Au revoir"}

        if langue == "en":
            match periode:
                case "matin":
                    return {"debut_chaine":"Good Morning","fin_chaine": "Good Bye"}
                case "apres_midi":
                    return {"debut_chaine":"Good Afternoon","fin_chaine": "See you soon"}
                case "soir":
                    return {"debut_chaine":"Good Evening","fin_chaine": "Good Bye"}
                case "nuit":
                    return {"debut_chaine":"Good Night","fin_chaine": "bye bye"}
                case "default":
                    return {"debut_chaine":"Hello","fin_chaine": "Good Bye"}