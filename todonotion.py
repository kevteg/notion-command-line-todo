from notion_client import Client
import logging


logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


class TodoNotion:

    fill_text = {True: "X", False: ""}
    todo_text = "[{}]"

    def __init__(self, token, page_id):
        """
        token: token to access the integration
        page_id: page to be used as the python 'interpreter'
        """
        self.notion = Client(auth=token)
        self.page_id = page_id

    def page_children(self):
        # a page is a block in notion
        children_object = self.notion.blocks.children.list(block_id=self.page_id)
        children = children_object.get("results", [])
        return children

    def list_tasks(self):
        """Prints all the found todos in the page"""
        children = self.page_children()
        text = ""

        for child in children:
            if child.get("type") == "to_do":
                is_check = child["to_do"]["checked"]
                plain_text = child["to_do"]["text"][0]["plain_text"]
                task = (
                    self.todo_text.format(self.fill_text[is_check]) + f" {plain_text}"
                )
                text += task + "\n"

        print(text)

    def add_new_task(self, task):
        """appends the result and the prompt"""
        children = [
            {
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "checked": False,
                    "text": [
                        {
                            "type": "text",
                            "text": {
                                "content": task,
                            },
                        },
                    ],
                },
            }
        ]

        self.notion.blocks.children.append(block_id=self.page_id, children=children)
        logging.info(f"'{task}' added to the page")
