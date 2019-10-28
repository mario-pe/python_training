authors = [
    {"name": "Jan", "sname": "Kowalski"},
    {"name": "Wacek", "sname": "Młot"},
    {"name": "Kazik", "sname": "Chrząsz"},
    {"name": "Zdzis", "sname": "Perk"},
]


def search_for_author(name, sname):
    for author in authors:
        if author.get("name") == name and author.get("sname") == sname:
            print("search_for_author")
            return author
