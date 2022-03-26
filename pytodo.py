import argparse
from todonotion import TodoNotion


def init() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pytodonotion",
        usage="%(prog)s [COMMAND]",
        description="Adds or retrieve the code in the notion page",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} version 0.0.1"
    )
    parser.add_argument(
        "-t", "--token", dest="token", required=True
    )
    parser.add_argument(
        "-p", "--page", dest="page_id", required=True
    )
    parser.add_argument('task', nargs='*', help='New task to be added')
    parser.add_argument('-l', const=True, nargs='?', dest="list", default=False, help='List existing tasks in the page')
    return parser


def main() -> None:
    parser = init()
    args = parser.parse_args()
    token = args.token
    page_id = args.page_id
    todo = TodoNotion(token, page_id)
    if args.list:
        todo.list_tasks()
    else:
        new_task = " ".join(args.task)
        todo.add_new_task(new_task)

if __name__ == "__main__":
    main()

