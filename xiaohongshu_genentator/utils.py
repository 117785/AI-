
import os

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from prompt_template import system_template_text, user_template_text

from xiaohongshu_model import Xiaohongshu
from  langchain_openai import ChatOpenAI

def generate_xiaohongshu(theme, openai_api_key,creativity=0.7):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])

    model = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=openai_api_key,
        temperature=creativity,
        base_url="https://api.aigc369.com/v1"
    )
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result
print(generate_xiaohongshu("荷兰",  os.getenv("OPENAI_API_KEY"),creativity=0.7))