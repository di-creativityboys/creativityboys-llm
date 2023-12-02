from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from pretty_print import printTask

#llama_13b_chat = CTransformers(model="TheBloke/Llama-2-13B-chat-GGUF", model_file="llama-2-13b-chat.Q5_K_S.gguf", model_type="llama")
#llama_7b_chat = CTransformers(model="TheBloke/Llama-2-7b-Chat-GGUF", model_file="llama-2-7b-chat.Q6_K.gguf", model_type="llama")
llama_7b_chat = CTransformers(model="./models/llama-2-7b-chat.Q6_K.gguf", model_type="llama")
llama_13b_chat = CTransformers(model="./models/llama-2-13b-chat.Q5_K_S.gguf", model_type="llama")

template = """
              ```{text}```
           """
    
prompt = PromptTemplate(template=template, input_variables=["text"])

llm_chain_13b_chat = LLMChain(prompt=prompt, llm=llama_13b_chat)
llm_chain_7b_chat = LLMChain(prompt=prompt, llm=llama_7b_chat)



async def query_llm(prompt, model_name):
    printTask(f"{model_name}: {prompt}")

    result = ""

    if model_name == "llama_13b_chat":
        result = llm_chain_13b_chat.run(prompt)
    if model_name == "llama_7b_chat":
        result = llm_chain_7b_chat.run(prompt)
    
    printTask(f"{model_name} result:")
    print(result)

    return result