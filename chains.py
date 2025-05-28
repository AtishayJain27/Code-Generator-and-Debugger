import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.getenv("GROQ_ENV_KEY")

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")
    
    def give_ans(self, question_input):
        prompt_answer = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {Question}
        
            ### INSTRUCTION:
            You are a Code Generator.
            Generate a simple code dont add too much explanation only necesarry comments for the question asked. Provide only the function do not provide the header files
            Do not provide a preamble.
            ### ANSWER (NO PREAMBLE):
        
            """
        )

        chain_answer = prompt_answer | self.llm
        res = chain_answer.invoke({"Question" : question_input })
        return res.content

    def debug_code(self, code_input):
        prompt_answer = PromptTemplate.from_template(
            """
            ### CODE DEBUGGER:
            {code}
        
            ### INSTRUCTION:
            You are a Code Debugger.
            Analyze the code and find the issues , tell about those issues and give some logic to how to fix those issues .
            Do not provide a preamble.
            ### ANSWER (NO PREAMBLE):
        
            """
        )
        chain_answer = prompt_answer | self.llm
        res = chain_answer.invoke({"code" : code_input })
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))