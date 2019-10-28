
from thread import start_log, add_log, logs
import threading
from parser import parse_xml
from adapter import get_data



def main():
    projects = parse_xml()
    local = threading.local()

    thread = threading.Thread(target=logs, args=(local,))
    thread.start()
    for project_id in projects:
        print(project_id)
        get_data(project_id, local)



if __name__ == "__main__":
    main()