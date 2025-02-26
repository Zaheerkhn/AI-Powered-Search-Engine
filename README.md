# 🔎 AI-Powered Search Engine

An AI-powered search engine built using **Streamlit** and **LangChain**, leveraging **Groq's LLM**, Wikipedia, Arxiv, and DuckDuckGo for retrieving accurate and relevant information.

## 🚀 Features
- 🌍 **Web Search**: Searches the web using DuckDuckGo.
- 📖 **Wikipedia Search**: Retrieves concise information from Wikipedia.
- 📚 **Arxiv Search**: Fetches academic papers from Arxiv.
- 🤖 **AI-Powered Responses**: Uses LLM (Llama-3.3-70b-Versatile) for intelligent query handling.
- 💬 **Interactive Chat Interface**: Built with Streamlit's chat UI.
- 🎨 **Custom Styling**: Enhanced UI with CSS.

## 🛠️ Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/Zaheerkhn/AI-Powered-Search-Engine
   cd AI-Powered-Search-Engine
   ```

2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project directory and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

## 🚀 Running the App

To start the Streamlit app, run:
```sh
streamlit run app.py
```

## 📂 Project Structure
```
📂 ai-search-engine
├── 📜 app.py             # Main Streamlit app
├── 📜 requirements.txt  # Required dependencies
├── 📜 .env.example      # Example environment file
└── 📜 README.md         # Project documentation
```

## 📜 Environment Variables
The application requires the following environment variables:
- `GROQ_API_KEY`: API key for Groq's LLM
- `LANGCHAIN_API_KEY`: API key for LangChain

## 🔗 Dependencies
- **Streamlit** - For the interactive UI
- **LangChain** - For integrating various search tools and LLMs
- **Groq** - For LLM-based responses
- **DuckDuckGoSearchRun** - For web searches
- **ArxivQueryRun** - For academic paper search
- **WikipediaQueryRun** - For Wikipedia queries

## 📜 License
This project is licensed under the **Apache License 2.0**.

## 🎯 Future Enhancements
- [ ] Add support for more LLMs
- [ ] Improve UI with more interactivity
- [ ] Implement caching for faster responses

## 🙌 Contributing
Pull requests are welcome! Feel free to open an issue if you have suggestions.

## 📞 Contact
For queries, reach out via **zaheerkhan00457@gmail.com** or create an issue in the repository.

---

🚀 **Enjoy your AI-powered search experience!** 🔎


