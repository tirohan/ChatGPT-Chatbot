import streamlit as st
import openai 

st.title("Let's Chat")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       **Author: Tanbin Islam Rohan**
       '''
)

model_engine = "text-davinci-003"
openai.api_key = "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"


def main():
    # Get user input
    user_query = st.text_input(
        "Enter query here, to exit enter :q", "what is Machine Learning?")
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT subprocess
        response = ChatGPT(user_query)
        return st.write(f"{user_query} {response}")

# Use the OpenAI API to generate a response

def ChatGPT(user_query):


    completion = openai.Completion.create(
        engine=model_engine,
        prompt=user_query,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response


main()

