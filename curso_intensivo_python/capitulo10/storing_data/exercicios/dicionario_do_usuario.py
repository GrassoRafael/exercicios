# Exercicio 10.13
# Dicionário do usuário:

from pathlib import Path
import json

def writing_dic(path):
    """Grava 3 informações inputadas em um arquivo json"""
    info = input('Digite uma informação: ') + '\n'
    info += input('Digite mais uma informação: ') + '\n'
    info += input('Digite a última informação: ') + '\n'
    contents = json.dumps(info)
    path.write_text(contents)
    return info


def stored_dic(path):
    """Verifica se existe o arquivo na variável path, senão houver retorna None"""
    if path.exists():
        contents = path.read_text()
        info = json.load(contents)
        return info
    else:
        return None


def dicionary_user():
    path = Path('dictionary_user.json')
    info = stored_dic(path)
    if info:
        print(info)
    else:
        info = writing_dic(path)
        print(info)

# Programa principal
dicionary_user()
