from ting_file_management.priority_queue import PriorityQueue

import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    regular_priority_1 = {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": [],
    }

    regular_priority_2 = {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": [],
    }

    high_priority_1 = {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }

    high_priority_2 = {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": [],
    }

    priority_queue.enqueue(regular_priority_1)
    priority_queue.enqueue(high_priority_1)
    priority_queue.enqueue(regular_priority_2)
    priority_queue.enqueue(high_priority_2)

    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue.high_priority) == 2

    remove_first = priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 1
    assert len(priority_queue.regular_priority) == 2
    assert remove_first == high_priority_1

    assert priority_queue.search(0) == high_priority_2
    assert priority_queue.search(1) == regular_priority_1
    assert priority_queue.search(2) == regular_priority_2

    remove_second = priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 2
    assert remove_second == high_priority_2

    assert priority_queue.search(0) == regular_priority_1
    assert priority_queue.search(1) == regular_priority_2

    remove_third = priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 1
    assert remove_third == regular_priority_1

    assert priority_queue.search(0) == regular_priority_2

    priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(50)
