# Maya Telegram Bot : Phi3

Maya is a AI real estate agent powered by the most powerful LLMs available. 

## Features

- Friendly chatbot.
- Get property recommendations and advice on buying properties.
- RAG for accurate, up to date information on properties.
- Uses Langchain (Tis nothing but a bug. Not recommended.)

## Installation


1. Clone the repository: `git clone https://github.com/your-username/maya-ai.git`
2. Download Ollama, pull Phi3 (latest) model and follow the steps: [Ollama](https://github.com/ollama/ollama)
3. Download Neo4j Desktop/Create an account on the website and create a database
4. Using `test_db.json` and the commands in the test_app folder, populate the db
5. Using telegram BotFather, create a bot and get the API token
6. Rename `.env.txt` to `.env` and add Neo4j connection details and telegram API token
7. Install the required dependencies: `pip install -r requirements.txt`
8. Run the main script: `python main.py`

## Usage

Test data is synthetic and limited to Mumbai, but you can have any kind of data you want.
You may want to update the `cypher_query_template.txt` file to be more in line with your data.

To use Maya AI, run the following command:

```
python main.py
```

## License

This project is licensed under the [License](LICENSE).
