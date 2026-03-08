from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hi, i am {name} tell me a joke with my name!"
)

text = template.format(name="Felipe")

print(text)