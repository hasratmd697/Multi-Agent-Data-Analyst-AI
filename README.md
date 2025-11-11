# Multi-Agent Data Analysis AI

This project is a sophisticated AI-powered data analysis tool that leverages a multi-agent architecture to interpret natural language queries, write Python code for analysis, and execute it securely in a sandboxed Docker environment.

Built with Microsoft's AutoGen framework, this system uses a team of specialized AI agents that collaborate to perform complex data analysis tasks, providing insights from datasets based on simple user prompts.

## Features

- **Natural Language Interface**: Ask for data analysis in plain English.
- **Multi-Agent Collaboration**: A "team" of AI agents, including a Data Analyzer and a Code Executor, work together to solve tasks.
- **Secure Code Execution**: All generated Python code is executed within a Docker container to ensure safety and prevent unintended side effects on your local machine.
- **Powered by Large Language Models**: Integrates with state-of-the-art models from OpenAI to understand prompts and generate analysis code.
- **Example Included**: Comes with the classic `titanic.csv` dataset to demonstrate its capabilities out-of-the-box.

## How It Works

The workflow is orchestrated by a team of AI agents:

1.  **User Input**: The user provides a high-level data analysis query via the command line (e.g., "Analyze titanic.csv and tell me the survival rate by passenger class").
2.  **Data Analyzer Agent**: This agent receives the query, understands the goal, and writes the necessary Python code (using libraries like `pandas`, `matplotlib`, etc.) to perform the analysis.
3.  **Code Executor Agent**: This agent takes the generated Python script and executes it within a secure Docker container. This sandboxed environment has access to the necessary data files.
4.  **Result**: The output from the script (e.g., statistical summaries, text results, or paths to generated charts) is captured and presented back to the user.

## Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

- Python 3.10+
- Docker Desktop (must be running)
- Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd "TDS Project 2 Data Analysis AI Agent"
    ```

2.  **Create a Python virtual environment and activate it:**
    - On Windows:
      ```bash
      python -m venv .venv
      .\.venv\Scripts\Activate.ps1
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    Create a file named `.env` in the root of the project directory and add your API keys.
    ```env
    # .env
    OPENAI_API_KEY="your-openai-api-key"
    ```

## Usage

1.  Make sure the dataset you want to analyze is present in the `temp/` directory. The `titanic.csv` dataset is already included as an example.
2.  Run the `main.py` script from the root directory with your analysis query as an argument.

**Example:**
```bash
python main.py "Analyze the data in titanic.csv and plot a bar chart of the survival rate by gender. Save the chart to a file."
```

The agent will process the request, and the results, including the path to the saved chart file, will be printed to the console.

## Project Structure

```
.
├── agents/             # Defines the specialized AI agents (Analyzer, Executor)
├── config/             # Configuration for API clients and Docker utilities
├── team/               # Orchestrates the collaboration between agents
├── temp/               # Workspace for datasets and temporary code files
├── .env                # API keys and environment variables (must be created)
├── main.py             # Main entry point for the application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```
