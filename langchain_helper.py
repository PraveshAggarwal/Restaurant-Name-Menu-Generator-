from langchain_ollama import OllamaLLM
from  langchain_classic.chains import SequentialChain
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(
    model="tinyllama:latest",
    temperature=0.6
)

def generate_restaurant_name_and_items(cuisine):

    template3 = PromptTemplate.from_template(
    input_variable = ['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fency name for this",
    )
    name_chain = LLMChain(llm=llm, prompt=template3, output_key="restaurant_name")

    # second chain
    template4 = PromptTemplate.from_template(
        input_variable = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it as a comma seperated",
    )
    food_items_chain = LLMChain(llm=llm, prompt=template4, output_key="menu_items")

    chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', 'menu_items'],
    )
    response = chain({'cuisine':cuisine})

    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Indian"))    