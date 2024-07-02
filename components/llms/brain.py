from langchain_community.llms import Ollama
from langchain.chains import ConversationChain,GraphCypherQAChain
from langchain.memory import ConversationBufferWindowMemory
from components.prompts import Prompt
from components.db import Db

class Brain:
    def __init__(self):
        db = Db()
        self.graph = db.get_graph()
        self.schema = self.graph.schema
        self.memory = ConversationBufferWindowMemory(k=7)
        self.cypher_llm = self._create_cypher_llm()
        self.chat_llm = self._create_chat_llm()
        self.route_llm = self._create_route_llm()
        self.conversation = ConversationChain(llm=self.chat_llm, memory=self.memory)

    def _create_cypher_llm(self):
        return Ollama(
            model='phi3', top_k=7, top_p=0.02,
            temperature=0.00,
            system=Prompt.get_cypher_prompt(schema=self.schema)
        )

    def _create_chat_llm(self):
        return Ollama(model="phi3", temperature=45, top_k =10)

    def _create_route_llm(self):
        return Ollama(model="phi3", temperature=0.0)

    def process_query(self, query):
        route_prompt = Prompt.get_query_classifier_prompt(query=query)
        route_result = self.route_llm.invoke(route_prompt)
        db_info=""
        if "cypher_chain" in route_result.lower():
            try:
                cypher_result = GraphCypherQAChain.from_llm(llm=self.cypher_llm,graph=self.graph, schema = self.schema, verbose = True, return_direct=True).invoke(query)
                db_info = cypher_result  
                print(db_info)
            except:
                db_info =""
        else:
            db_info = ""

        self.chat_llm.system = Prompt.get_chat_prompt(
            chat_history=str(self.memory.chat_memory.messages),
            human_input=query,
            db_info=db_info
        )

        response = self.conversation.invoke(query)
        return response["response"]

