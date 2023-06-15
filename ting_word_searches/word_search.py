from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    files_with_word = []
    for file in instance._data:
        content = txt_importer(file)
        lines_with_word = [
            {"linha": index + 1}
            for index, line in enumerate(content)
            if word.lower() in line.lower()
        ]

        if lines_with_word:
            files_with_word.append(
                {
                    "palavra": word,
                    "arquivo": file,
                    "ocorrencias": lines_with_word,
                }
            )

    return files_with_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
