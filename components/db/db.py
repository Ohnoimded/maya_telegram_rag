from langchain_community.graphs import Neo4jGraph
from components.configs import Config

class Db:
    def __init__(self) :
        pass        
    def get_graph(self):
        return Neo4jGraph(username=Config.NEO4J_USERNAME, 
                   password=Config.NEO4J_PASSWORD,
                   url=Config.NEO4J_URI, 
                   database=Config.NEO4J_DATABASE)
    
    
