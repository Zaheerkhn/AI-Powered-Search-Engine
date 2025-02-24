import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun, ArxivQueryRun, WikipediaQueryRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq

# Load API key
groq_api = os.getenv("GROQ_API_KEY")

# Langsmith tracing
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "AI Search Engine"

# Set page config
st.set_page_config(page_title="AI Search Engine", page_icon="🔍", layout="wide")

# Custom CSS for UI enhancements
st.markdown("""
    <style>
    body {
        background-color: #f7f7f7;
    }
    .stChatMessage {
        padding: 10px;
        border-radius: 10px;
        max-width: 80%;
    }
    .assistant {
        background-color: #e8f5e9;
        text-align: left;
    }
    .user {
        background-color: #bbdefb;
        text-align: right;
    }
    /* Chat Input Box Styling */
    [data-testid="stChatInput"] textarea {
        font-size: 14px !important;
        padding: 8px !important;
        height: 40px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize search tools
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

search = DuckDuckGoSearchRun()

# Title
st.title("🔎 AI-Powered Search Engine")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! Ask me anything, and I'll search the web for you!"}]

# Display previous messages with styled chat UI
for msg in st.session_state["messages"]:
    role = msg["role"]
    avatar = "🤖" if role == "assistant" else "👤"
    st.chat_message(role, avatar=avatar).write(msg["content"])

# User Input
if prompt := st.chat_input(placeholder="Type your query here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="👤").write(prompt)

    # Initialize LLM
    llm = ChatGroq(groq_api_key=groq_api, model_name="Llama-3.3-70b-Versatile", streaming=True)
    tools = [wiki, arxiv, search]

    # Initialize agent
    search_agent = initialize_agent(
        tools, llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        handle_parsing_errors=True
    )

    with st.chat_message("assistant", avatar="🤖"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        
        # Show a loading spinner
        with st.spinner("Searching..."):
            time.sleep(1)  # Simulate processing delay
            response = search_agent.run(prompt, callbacks=[st_cb])

        # Typing animation effect
        message_placeholder = st.empty()
        full_response = ""
        for char in response:
            full_response += char
            message_placeholder.markdown(full_response)  # Update message dynamically
            time.sleep(0.02)  # Small delay to simulate typing effect

        # Store response in session state
        st.session_state.messages.append({"role": "assistant", "content": response})
