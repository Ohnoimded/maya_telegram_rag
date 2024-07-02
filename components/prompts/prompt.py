import os

class Prompt:
    _cypher_query_template = None
    _chat_template = None
    _query_classifier_template = None

    @classmethod
    def load_template(cls, template_file):
        with open(template_file, 'r') as file:
            template = file.read()
        return template

    @classmethod
    def get_cypher_prompt(cls, schema):
        if cls._cypher_query_template is None:
            cls._cypher_query_template = cls.load_template(os.path.join(os.path.dirname(__file__), '..', 'templates', 'cypher_query_template.txt'))
        return cls._cypher_query_template.format(schema=schema)

    @classmethod
    def get_chat_prompt(cls, chat_history, human_input, db_info):
        if cls._chat_template is None:
            cls._chat_template = cls.load_template(os.path.join(os.path.dirname(__file__), '..', 'templates', 'chat_template.txt'))
        return cls._chat_template.format(chat_history=chat_history, human_input=human_input, db_info=db_info)

    @classmethod
    def get_query_classifier_prompt(cls, query):
        if cls._query_classifier_template is None:
            cls._query_classifier_template = cls.load_template(os.path.join(os.path.dirname(__file__), '..', 'templates', 'query_classifier_template.txt'))
        return cls._query_classifier_template.format(query=query)
