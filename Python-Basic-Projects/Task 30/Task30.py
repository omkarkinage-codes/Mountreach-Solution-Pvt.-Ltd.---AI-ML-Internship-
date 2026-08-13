
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# groq_key = os.getenv("GROQ_API_KEY")
# mistral_key = os.getenv("MISTRAL_API_KEY")

# print("Q2: API Key Management ")
# if groq_key and mistral_key:
#     print("All API keys (GROQ_API_KEY & MISTRAL_API_KEY) loaded successfully!")
# else:
#     print("Failed to load one or more API keys.")



# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# # Initialize ChatGroq model
# llm = ChatGroq(
#     model_name="llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY")
# )

# # Send prompt
# prompt = "Introduce yourself in 3 sentences."
# response = llm.invoke(prompt)

# print("Q3: Basic LLM Call ")
# print(response.content)



# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# # 1. Load environment variables
# load_dotenv()

# # 2. Initialize ChatGroq model with temperature=0.2 and max_tokens=50
# llm = ChatGroq(
#     model_name="llama-3.1-8b-instant",
#     temperature=0.2,
#     max_tokens=50,
#     api_key=os.getenv("GROQ_API_KEY"),
# )

# # 3. Send the same prompt from Q3
# prompt = "Introduce yourself in 3 sentences."
# response = llm.invoke(prompt)

# print("Q4: Parameter Controlled Output ")
# print(response.content)




# import os
# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI

# # 1. Load environment variables from .env
# load_dotenv()

# # 2. Initialize the Mistral model (mistral-small-2603)
# llm = ChatMistralAI(
#     model="mistral-small-2603",
#     api_key=os.getenv("MISTRAL_API_KEY")
# )

# # 3. Send prompt and print complete response
# prompt = "Explain what is Artificial Intelligence in simple words."
# response = llm.invoke(prompt)

# print("Q5: Mistral Model Response ")
# print(response.content)





# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_mistralai import ChatMistralAI

# # Load environment variables
# load_dotenv()

# # Define prompt
# prompt = "What are the advantages of using LangChain?"

# # Initialize both LLMs
# groq_llm = ChatGroq(
#     model_name="llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY")
# )

# mistral_llm = ChatMistralAI(
#     model="mistral-small-2603",
#     api_key=os.getenv("MISTRAL_API_KEY")
# )

# #  Invoke both models
# groq_res = groq_llm.invoke(prompt)
# mistral_res = mistral_llm.invoke(prompt)

# #  Display output clearly labeled
# print("Groq Response ")
# print(groq_res.content)

# print("\nMistral Response ")
# print(mistral_res.content)





# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# # 1. Load environment variables
# load_dotenv()

# # 2. Define creative prompt
# prompt = "Write a short creative story about a robot learning to cook."

# # 3. Test three different temperature settings
# temperatures = [0.1, 0.7, 1.2]

# print("Q7: Temperature Experiment ")

# for temp in temperatures:
#     llm = ChatGroq(
#         model_name="llama-3.1-8b-instant",
#         temperature=temp,
#         api_key=os.getenv("GROQ_API_KEY"),
#     )
#     res = llm.invoke(prompt)

#     print(f"\nTemperature = {temp} ")
#     print(res.content)
#     print("-" * 50)




# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# # 1. Load environment variables
# load_dotenv()

# # 2. Initialize ChatGroq model
# llm = ChatGroq(
#     model_name="llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY")
# )

# print("Q8: Simple Command-Line Chatbot ")
# print("Type your message below (type 'exit' to quit):\n")

# # 3. Chat loop
# while True:
#     user_input = input("You: ").strip()
    
#     # Check for exit condition
#     if user_input.lower() == "exit":
#         print("Bot: Goodbye!")
#         break
    
#     # Skip empty inputs
#     if not user_input:
#         continue

#     # Send input to model and print response
#     response = llm.invoke(user_input)
#     print(f"\nBot: {response.content}\n" + "-" * 40)





# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# # 1. Load environment variables
# load_dotenv()


# # 2. Define structured function
# def generate_topic_summary(topic: str):
#     llm = ChatGroq(
#         model_name="llama-3.1-8b-instant",
#         temperature=0.3,
#         api_key=os.getenv("GROQ_API_KEY"),
#     )

#     prompt = f"""
# You are an expert AI tutor. For the topic provided below, strictly structure your response into the following 3 sections:
# 1. A Short Definition (1-2 sentences)
# 2. Three Key Points (bullet points)
# 3. One Real-life Example

# Topic: {topic}
# """
#     response = llm.invoke(prompt)
#     return response.content


# # 3. Test with topic "Machine Learning"
# if __name__ == "__main__":
#     print(" Q9: Structured Prompting Result ")
#     output = generate_topic_summary("Machine Learning")
#     print(output)







import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI

# 1. Load environment variables
load_dotenv()


def get_groq_llm():
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError("GROQ_API_KEY is missing from .env file.")
    return ChatGroq(
        model_name="llama-3.1-8b-instant", temperature=0.7, api_key=key
    )


def get_mistral_llm():
    key = os.getenv("MISTRAL_API_KEY")
    if not key:
        raise ValueError("MISTRAL_API_KEY is missing from .env file.")
    return ChatMistralAI(model="mistral-small-2603", api_key=key)


def main():
    print("   Multi-Model AI Assistant Mini Project  ")

    while True:
        print("\nChoose Model:")
        print("1. Groq (llama-3.1-8b-instant)")
        print("2. Mistral (mistral-small-2603)")
        print("Type 'quit' to exit.")

        choice = input("\nEnter choice (1/2/quit): ").strip().lower()

        if choice == "quit":
            print("\nExiting Assistant. Have a great day!")
            break

        if choice not in ["1", "2"]:
            print("Invalid selection. Please enter 1, 2, or 'quit'.")
            continue

        user_question = input("Enter your question: ").strip()
        if not user_question:
            print("Question cannot be empty.")
            continue

        # Error Handling Block
        try:
            if choice == "1":
                print("\n[Sending request to Groq...]")
                llm = get_groq_llm()
            else:
                print("\n[Sending request to Mistral...]")
                llm = get_mistral_llm()

            response = llm.invoke(user_question)

            print("\nResponse ")
            print(response.content)
            print("=" * 45)

        except Exception as e:
            print(f"\nError occurred: {e}")


if __name__ == "__main__":
    main()