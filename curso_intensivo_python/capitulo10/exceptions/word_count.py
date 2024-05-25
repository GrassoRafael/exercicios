from pathlib import Path

def count_words(path):
    """ Conta o número aproximado de palavras em um arquivo"""
    try:
        contents = path.read_text(encoding='utf8')
    except FileNotFoundError:
        pass
    else:
        # Conta o número aproximado de palavras no arquivo:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


# Programa principal
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
