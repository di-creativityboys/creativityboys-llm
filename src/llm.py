from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from pretty_print import printTask

llama_13b_chat = CTransformers(model="TheBloke/Llama-2-13B-chat-GGUF", model_file="llama-2-13b-chat.Q5_K_S.gguf", model_type="llama")
llama_7b_chat = CTransformers(model="TheBloke/Llama-2-7b-Chat-GGUF", model_file="llama-2-7b-chat.Q6_K.gguf", model_type="llama")

template = """
              ```{text}```
           """
    
prompt = PromptTemplate(template=template, input_variables=["text"])

llm_chain_13b_chat = LLMChain(prompt=prompt, llm=llama_13b_chat)
llm_chain_7b_chat = LLMChain(prompt=prompt, llm=llama_7b_chat)


news = """Martin Griffiths, the UN's humanitarian chief, has announced the arrival of 14 more trucks carrying humanitarian aid into Gaza He said it was "another small glimmer of hope" for Palestinians, but warned they still need "more, much more"
The charity Oxfam welcomed the move, as well as yesterday's first load of aid, but said sending "a few trucks a day is simply not sufficient"
Earlier, Israeli PM Benjamin Netanyahu told troops that his people are in a battle for their lives and said the war against Hamas was "do or die"
The Israeli military has vowed to intensify air strikes on Gaza and warned Palestinians still in the north of the territory to flee south
Iran's foreign minister warned Israel and the US that the Middle East may spiral out of control if Israel does not immediately stop its military action
It's been more than two weeks since Hamas launched its assault on Israel, killing more than 1,400 people. Palestinian officials in Gaza say more than 4,600 have been killed since then"""



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