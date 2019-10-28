from pymemcache.client import base

client = base.Client(("localhost", 11211))


def check_cache(author):
    result = client.get(author)
    if result is None:
        print("nie w cachu")
        response_str = domain_response()
        client.set(response_str, response_str)
        return response_str
    else:
        print("jest w cacheu")
        return result


def domain_response():
    return "JanKowalski"


def do_staff():
    return check_cache("JanKowalski")


for i in range(2):
    print("do stuff: {}".format(do_staff()))
