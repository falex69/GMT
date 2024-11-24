# GMT check and push to the forum

import re
import requests

channel = "https://www.youtube.com/@BenoistRousseau/streams"
html = requests.get(channel + "/videos").text
info = re.search('(?<={"label":").*?(?="})', html).group()
url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

print("1) Verification du dernier direct")
print(f"   Video : {info}")
print(f"   Liens {url}")

choix = input("Voulez-vous publier ce liens [yes/no] ?")

if choix == "yes":
    print("2) Connexion")
    l = input("Votre login ?")
    p = input("votre p.....d ?")

    andlil_login_url = "https://www.andlil.com/forum/ucp.php?mode=login&redirect=index.php"
    r = requests.get(andlil_login_url).text
    #print(r)
    #TODO : Debug de la sessionde login pour ensuite poster une page.
    # CErtaineemn,t en 3 temps :
    # 1) Connexion a la page de login (récupération des sid et autres cookie)
    # 2) POST du formulaire de login
    # 3) Get de la page d'index
    # 4) Post de la page cible.
elif choix == "no":
    print("Ok !")
else:
    print("Goodbye!")