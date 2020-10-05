import requests

resp = requests.get("https://api.github.com/users/vittoriacassoni/followers")

user = resp.json()

print(user)
arquivo = open("teste.tsv", "a")
arquivo.write("Seguidos por Vittoria Cassoni -  GITHUB \n")

for artigos in user:
    arquivo.write("Id:{}\t Login:{}\n".format(artigos["id"], artigos["login"]))

arquivo.close()
