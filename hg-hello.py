# Menggunakan Hugging FaceHub
import os
from langchain_community.llms import HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "api_key_here"
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")
text = "Beritahu fakta menarik tentang kentang!"
result = llm.invoke(text)
print(result)