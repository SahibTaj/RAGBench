import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from config import LLM_MODEL, TEMPERATURE
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(groq_api_key = groq_api_key, model=LLM_MODEL,temperature=TEMPERATURE)



def generate_answer(question,retrieved_chunks):

    prompt =ChatPromptTemplate.from_messages(
        [
            ("system",
            """
            You are a RAG assistant.

            Answer ONLY using the provided context.

            If the answer cannot be found in the context, say:
            "I could not find that information in the provided documents."
            Do not use external knowledge.
            Context:
            {retrieved_chunks}
            """
            ),
            ("user","{question}")
        ]
    )

    chain = prompt|llm

    context = "\n\n".join(retrieved_chunks["documents"][0])

    response = chain.invoke({
        "question":question,
        "retrieved_chunks":context
    })

    return response.content