from notion_client import Client
import logging


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class TodoNotion:


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

    def add_new_todo(self, task):
        """appends the result and the prompt"""
        children = [
            {
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "text": [
                        {
                            "type": "text",
                            "text": {
                                "content": task,
                            },
                        },
                    ],
                    "color": "green",
                },
            }
        ]

        return self.notion.blocks.children.append(
            block_id=self.page_id, children=children
        )


