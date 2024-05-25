from pathlib import Path
import json

def get_stored_username(path):
    """Obtém o nome de usuário armazenado se disponível"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Solicita o usuário pelo nome"""
    username = input("What is your name? ").title()
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def confirm_username(path):
    """Confirma o nome do usuario, caso contrário solicita um cadastro"""
    if get_stored_username(path) == None:
        return None
    else:
        name = input(f"Is your name {get_stored_username(path)} (y/n)? ").lower()
    if name == 'y':
        username = get_stored_username(path)
        return username
    elif name == 'n':
        return None


def greet_user():
    """Cumprimenta o usuário pelo nome"""
    path = Path('username.json')
    confirm = confirm_username(path)
    if confirm:
        print(f"Welcome back {confirm}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you next time {username}")


greet_user()
