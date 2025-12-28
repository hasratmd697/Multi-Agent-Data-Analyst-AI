import streamlit as st
import asyncio
import os

from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from team.analyzer_gpt import get_analyzer_gpt_team
from config.openai_model_client import get_model_client
from config.docker_utils import get_docker_executor, start_docker_container, stop_docker_container

st.title("Multi-Agent Data Analyst AI")
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt", "pdf"])

if 'message' not in st.session_state:
    st.session_state.message = []
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state = None

# task = st.text_input("Enter a task", value="Can you tell me how many rows are in titanic.csv data in your working directory")

task = st.chat_input("Enter a task")

async def run_analyzer_gpt(docker,openai_model_client,task):
    
    try:
        await start_docker_container(docker)
        team = get_analyzer_gpt_team(docker,openai_model_client)
        
        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)
        
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg := f"{message.source} : {message.content}")
                #yield msg
                
                if msg.startswith("User"):
                    with st.chat_message("user", avatar='👤'):
                        st.markdown(msg)
                elif msg.startswith("Data Analyzer Agent"):
                    with st.chat_message("Data Analyst Agent", avatar='🤖'):
                        st.markdown(msg)
                elif msg.startswith("Code Executor Agent"):
                    with st.chat_message('Code Runner Agent', avatar='👨‍💻'):
                        st.markdown(msg)
                st.session_state.message.append(msg)    
                
            elif isinstance(message, TaskResult):
                print(msg := f"Stop Reason: {message.stop_reason}")
                #yield msg
                with st.chat_message('Code Runner Agent', avatar='👨‍💻'):
                    st.markdown(msg)
                    st.session_state.message.append(msg)
                
        st.session_state.autogen_team_state = await team.save_state()
        return None
    except Exception as e:
        print(e)
        return e
    finally:
        await stop_docker_container(docker)

if uploaded_file is not None:
    st.write("File uploaded successfully")
    


if st.session_state.message:
    for msg in st.session_state.message:
        st.markdown(msg)

if task:
    if uploaded_file is not None and task:

        if not os.path.exists("temp"):
            os.makedirs("temp")
        
        with open("temp/titanic.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())

    openai_model_client = get_model_client()
    docker = get_docker_executor()
    
    error = asyncio.run(run_analyzer_gpt(docker, openai_model_client, task))
    if error:
        st.error("An error occurred: ", error)

    if os.path.exists("temp/output.png"):
        st.image("temp/output.png",caption="Analysis File")
        shown = False
    
else:
    st.warning("Please upload a file and enter a task")