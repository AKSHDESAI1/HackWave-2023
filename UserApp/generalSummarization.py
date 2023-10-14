# Using llama.cpp in python
import faulthandler
faulthandler.enable()
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.stdout import StdOutCallbackHandler
from langchain.schema import HumanMessage,SystemMessage,AIMessage 


template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

# prompt = PromptTemplate(template=template, input_variables=["question"])
# # Callbacks support token-wise streaming
callback_manager = CallbackManager([StdOutCallbackHandler()])
# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path="/Users/cardinal/testing/pygmalion-2-13b.Q4_K_M.gguf",
    temperature=0.7,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager, 
    verbose=True, # Verbose is required to pass to the callback manager
)
# llm.generate(
#     [
#         SystemMessage(content="You are an unhelpful AI bot that makes a joke at whatever the user says"),
#         HumanMessage(content="I would like to go to New York, how should I do this?")
#     ]
# )

llm("You are not rakesh ")
# prompt = """
# Question: When was the iphone first released?
# """
# response  = llm(prompt)
# print('Response = ', response)

