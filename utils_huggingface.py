##from langchain.agents import create_pandas_dataframe_agent #This import has been recently replaced by the below
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
#from langchain.llms import OpenAI
#New import from langchain, which replaces the above
from langchain_openai import OpenAI

def query_agent(data, query, openai_api_key=None):
    # Parse the CSV file and create a Pandas DataFrame from its contents.
    df = pd.read_csv(data)

    if openai_api_key:
        llm = OpenAI(api_key=openai_api_key)
    else:
        llm = OpenAI()  # Create OpenAI instance without API key

    # Create a Pandas DataFrame agent.
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    # Invoke the agent with the query
    return agent.invoke(query)