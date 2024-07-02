# from langchain_community.llms import Ollama
# from langchain.memory import ConversationBufferWindowMemory
# from langchain.chains import ConversationChain,LLMChain
# from langchain_core.prompts import PromptTemplate


# memory = ConversationBufferWindowMemory(k=4)
# conv = ConversationChain(llm=Ollama(model="phi3",temperature=0),memory=memory)


# print(conv.prompt.template.format)


# # conv.invoke("Dax123 is wet")
# # conv.invoke("What is India's capital?")
# # c=conv.invoke("Is Dax123 wet or dry?")

# print(memory)

# print("\n\n\n")




from components.llms import Brain



brain = Brain()

query = "Show me some properties in Worli under 400 crores"
chat_result = brain.process_query(query)
print(chat_result)
query = "Show me some Apartments in Andheri East under 5000 crores with Parking and Garden"
chat_result = brain.process_query(query)
print(chat_result)

# query = "Then, what about 3 or 4 BHK?"
# chat_result = brain.process_query(query)
# print(chat_result)


# query = "Out of that, how many are"
# chat_result = brain.process_query(query)
# print("Chat Result:")
# print(chat_result)