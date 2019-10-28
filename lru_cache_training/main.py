from functools import lru_cache

from lru_cache_training.service import search_for_author


def import_autors():
    for author in range(2):
        author = get_auhor("Jan", "Kowalski")
        print(author)
    for author in range(2):
        author = get_auhor("Wacek", "Młot")
        print(author)
    for author in range(2):
        author = get_auhor("Jan", "Kowalski")
        print(author)

@lru_cache(maxsize=None)
def get_auhor(name, sname):
    return search_for_author(name, sname)

import_autors()
