import sys


def txt_importer(path_file):
    content = []
    try:
        if not path_file.endswith('.txt'):
            sys.stderr.write('Formato inválido')

        with open(path_file, 'r') as file:
            for line in file:
                content.append(line.strip())

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    return content
