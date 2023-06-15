import sys
from ting_file_management.file_management import txt_importer


def out_file(path_file):
    file = txt_importer(path_file)
    out_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    print(str(out_process))


def process(path_file, instance):
    if path_file in instance._data:
        return None
    out_file(path_file=path_file)
    instance.enqueue(path_file)


def remove(instance):
    if instance.__len__() == 0:
        return print(str('Não há elementos'))
    file = instance.dequeue()
    print(str(f"Arquivo {file} removido com sucesso"))


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        out_file(path_file=path_file)
    except IndexError:
        sys.stderr.write("Posição inválida")
