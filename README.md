# Multi-Agent Data Analyst AI

This project is a sophisticated AI-powered data analysis tool that leverages a multi-agent architecture to interpret natural language queries, write Python code for analysis, and execute it securely in a sandboxed Docker environment.

Built with Microsoft's AutoGen framework, this system uses a team of specialized AI agents that collaborate to perform complex data analysis tasks, providing insights from datasets based on simple user prompts.

## Features

- **Streamlit Web Interface**: Modern chat-based UI with real-time agent conversations
- **Multi-Agent Collaboration**: A "team" of AI agents, including a Data Analyzer and a Code Executor, work together to solve tasks
- **Secure Code Execution**: All generated Python code is executed within a Docker container
- **OpenRouter API Integration**: Flexible LLM provider supporting multiple models (Gemini, GPT, Claude, etc.)
- **Session State Management**: Maintains conversation history across interactions
- **Visualization Support**: Automatically generates and displays charts (saved as `output.png`)
- **Chat Avatars**: Visual distinction between agents (👤 User, 🤖 Data Analyst, 👨‍💻 Code Executor)

## How It Works

The workflow is orchestrated by a team of AI agents:

1. **User Input**: The user provides a data analysis query via the Streamlit chat interface
2. **Data Analyzer Agent** 🤖: Understands the goal and writes Python code for analysis
3. **Code Executor Agent** 👨‍💻: Executes the code in a secure Docker container
4. **Result**: Output and visualizations are displayed in the chat interface

## Getting Started

### Prerequisites

- Python 3.10+
- Docker Desktop (must be running)
- Git
- OpenRouter API Key (or other supported LLM provider)

### Installation

1. **Clone the repository:**

   ```bash
   git clone <your-repository-url>
   cd "Data Analysis AI Agent"
   ```

2. **Create a Python virtual environment and activate it:**

   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the project root:
   ```env
   OPENROUTER_API_KEY=your-openrouter-api-key
   ```

## Usage

### Streamlit Web App (Recommended)

```bash
streamlit run streamlit_app.py
```

Then open http://localhost:8501 in your browser.

1. Upload your CSV/TXT/PDF file
2. Enter your analysis query in the chat input
3. Watch the agents collaborate to solve your task
4. View generated charts automatically displayed in the UI

### Command Line

```bash
python main.py "Analyze titanic.csv and plot survival rate by gender"
```

## Project Structure

```
.
├── agents/             # AI agent definitions
│   ├── code_executor_agent.py
│   ├── data_analyzer_agent.py
│   └── prompts/        # System prompts for agents
├── config/             # Configuration files
│   ├── openai_model_client.py  # OpenRouter/LLM client setup
│   ├── docker_utils.py         # Docker container management
│   └── constants.py
├── team/               # Agent team orchestration
│   └── analyzer_gpt.py
├── temp/               # Workspace for datasets and outputs
├── .env                # API keys (create this file)
├── main.py             # CLI entry point
├── streamlit_app.py    # Web UI entry point
├── requirements.txt    # Python dependencies
└── README.md
```

## Configuration

The LLM client is configured in `config/openai_model_client.py`:

- **Model**: `google/gemini-2.0-flash-001` (changeable via OpenRouter)
- **Base URL**: `https://openrouter.ai/api/v1`
- **Retry Logic**: 5 retries with 120s timeout for reliability

## Recent Updates

- ✅ Migrated from OpenAI/Gemini to **OpenRouter API** for flexible model selection
- ✅ Added **Streamlit chat interface** with session state management
- ✅ Implemented **emoji avatars** for visual agent distinction
- ✅ Added **automatic chart display** (`output.png`) in the UI
- ✅ Added **retry logic** (5 retries) for handling transient API errors
- ✅ Improved **error handling** and user feedback
