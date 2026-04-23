import requests
import time
from decouple import config

# Configuration
API_KEY = config('FOOTBALL_API_KEY')
HEADERS = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
}

def analyser_matchs_live():
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    try:
        response = requests.get(url, headers=HEADERS)
        matchs = response.json().get('response', [])
        
        if not matchs:
            print("Aucun match en direct pour le moment.")
            return

        for match in matchs:
            equipe_dom = match['teams']['home']['name']
            equipe_ext = match['teams']['away']['name']
            score_dom = match['goals']['home']
            score_ext = match['goals']['away']
            temps = match['fixture']['status']['elapsed']

            # --- LOGIQUE DE PRONOSTIC (Exemple) ---
            # Si une équipe gagne et qu'on est après la 80ème minute
            # La probabilité que le résultat reste ainsi est forte.
            print(f"[{temps}'] {equipe_dom} {score_dom}-{score_ext} {equipe_ext}")
            
            if temps > 80 and score_dom > score_ext:
                print(f"-> PRONO : Victoire probable de {equipe_dom}")
            elif temps > 80 and score_ext > score_dom:
                print(f"-> PRONO : Victoire probable de {equipe_ext}")

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    print("Démarrage du Bot de Pronostics...")
    analyser_matchs_live()
