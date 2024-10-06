from src.Parser import Parser
from src.Utils import Utils
from src.Bot import Bot
from src.Model import Model

# data_sources = [
#   "https://eve.fandom.com/sitemap-newsitemapxml-index.xml"
# ]

# data_urls = []

# parser = Parser()
# for data_source in data_sources:  
#     print(parser.parse_sitemap(data_source))
#   #data_urls.append(parser.parse_sitemap(data_source))

# exit()

# #data = [WebBaseLoader(url).load() for url in data_urls]
# data_list = [item for sublist in data for item in sublist]
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
# data_splits = text_splitter.split_documents(data_list)

# vectorstore = Chroma.from_documents(
#   documents=data_splits, 
#   collection_name="rag-chroma", 
#   embedding=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text')
# )
# retriever = vectorstore.as_retriever()


if __name__ == "__main__":
  print("Welcome to EveSight.")
  print("Trying to get the token from environment variables...")
  
  token = Utils.retrieve_token()

  model = Model(name="llama3.1")

  evesight = Bot(command_prefix="!", self_bot=False, model=model)
  evesight.run(token)