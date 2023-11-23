# Importando libs
from urllib.request import urlopen
import sys

try:
    # Pegando ip informando como argumento
    ip = sys.argv[1]

    if ip:
        # URL da api
        url = f"https://ip-api.com/json/{ip}"

        # Iniciando o request
        request = urlopen(url)
        data = request.read().decode()

        # Convertendo string Api, para DICT (dicionario)
        data_dict = eval(data)

        # Iterando sobre o dicionário e imprimindo as chaves e valores
        for key, value in data_dict.items():
            print(f"{key} == {value}")

except Exception as ex:
    print(f"Error: {ex}")
