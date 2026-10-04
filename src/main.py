import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set")

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0,
    )

    response = llm.invoke(
        "Explain what an AI agent is in three sentences."
    )

    print(response.content)


if __name__ == "__main__":
    main()