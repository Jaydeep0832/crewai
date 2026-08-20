# CrewAI Production Examples 🤖🚀

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/Framework-CrewAI-red.svg)](https://www.crewai.com/)
[![uv](https://img.shields.io/badge/Package%20Manager-uv-purple.svg)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Production-oriented, hardened **CrewAI** multi-agent examples for building, testing, and deploying autonomous agent systems, custom tools, RAG knowledge sources, and stateful CrewAI Flows.

This repository adapts and hardens learning examples from [akmadan/learn_crewai](https://github.com/akmadan/learn_crewai). Each example is structured as an isolated, independently managed Python project with crisp configuration, dependency locking (`uv`), input validation, and automated testing.

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [Requirements](#-requirements)
- [Quick Start](#-quick-start)
- [Detailed Module Walkthrough](#-detailed-module-walkthrough)
- [Environment Configuration](#-environment-configuration)
- [Testing & Quality Assurance](#-testing--quality-assurance)
- [Security Best Practices](#-security-best-practices)
- [Attribution & License](#-attribution--license)

---

## ✨ Features

- **YAML-Driven Agent Orchestration**: Declarative role, goal, backstory, and task management via YAML files.
- **RAG & Knowledge Integration**: Context-aware agents leveraging knowledge bases and vector search.
- **Custom Tool Development**: Strongly-typed custom tools (e.g., Numbers API tool) with input validation and HTTP request safety.
- **Event-Driven CrewAI Flows**: Stateful multi-step pipelines controlling execution flow and structured file outputs.
- **Isolated Environments**: Fast, deterministic dependency resolution using [`uv`](https://docs.astral.sh/uv/).
- **Production Safety**: Zero hardcoded credentials, strict input bounds, timeout limits, and automated health checks.

---

## 🏗️ Project Architecture

```text
crewai/
├── basic_crewai/       # Basic research and reporting crew (YAML configured)
├── chat_bot/           # Knowledge-backed AI assistant with RAG capabilities
├── marketing_crewai/   # Multi-agent marketing research and strategy generation crew
├── numbers_api/        # Typed custom Numbers API tool with pytest suite
├── react_agent/        # ReAct pattern agent notebook example
├── sample_flow/        # Stateful CrewAI Flow example with controlled output paths
├── learn_crew_ai/      # Repository health-check and utility CLI package
├── pyproject.toml      # Root workspace configuration
└── README.md           # Project documentation
```

### Module Comparison Matrix

| Module | Core Focus | Key Technologies / Tools | Output |
| :--- | :--- | :--- | :--- |
| `basic_crewai` | Multi-Agent Research | CrewAI, SerperDev / Web Search, OpenAI | Research reports (`.md`) |
| `chat_bot` | RAG Assistant | CrewAI Knowledge, Vector Store / ChromaDB | Interactive Q&A |
| `marketing_crewai` | Strategy & Marketing | YAML Configs, Market Research Tools | Strategy breakdown & campaign docs |
| `numbers_api` | Custom Tooling | Custom `BaseTool`, Pydantic, HTTPX, Pytest | Number fact generation & test suite |
| `sample_flow` | Stateful Flow Control | CrewAI Flows (`@flow`, `@listen`) | Structured text outputs (`poem.txt`) |
| `react_agent` | ReAct Notebook | Jupyter, LangChain / CrewAI ReAct pattern | Interactive notebook exploration |

---

## ⚙️ Requirements

- **Python**: `^3.11`
- **Package Manager**: [`uv`](https://docs.astral.sh/uv/) (installed via `pip install uv` or official installer)
- **API Key**: LLM provider key (e.g., OpenAI API Key)

---

## 🚀 Quick Start

### 1. Clone the Repository

```powershell
git clone https://github.com/Jaydeep0832/crewai.git
cd crewai
```

### 2. Set Up Root Environment

Initialize virtual environment and install development dependencies:

```powershell
uv sync --group dev
```

### 3. Run Repository Health Check

Verify installation with the built-in health check package:

```powershell
uv run learn-crew-ai
```

---

## 🔍 Detailed Module Walkthrough

Each example functions as an independent Python package with its own `pyproject.toml`.

### 1. `basic_crewai` — Research & Reporting Crew
Demonstrates multi-agent collaboration with a researcher agent gathering facts and a writer agent synthesizing markdown reports.

```powershell
cd basic_crewai
uv sync
uv run crewai run
```

### 2. `chat_bot` — RAG Knowledge Assistant
Demonstrates how to attach external context and knowledge sources to CrewAI agents for domain-specific Q&A.

```powershell
cd chat_bot
uv sync
uv run crewai run
```

### 3. `marketing_crewai` — Marketing Strategy Crew
Runs an end-to-end marketing strategy pipeline, analyzing target audiences, competitor positioning, and content calendar creation.

```powershell
cd marketing_crewai
uv sync
uv run crewai run
```

### 4. `numbers_api` — Custom Tool & Testing
Features a custom `NumbersAPITool` built with Pydantic schema validation and HTTP safety guarantees, backed by a comprehensive `pytest` test suite.

```powershell
cd numbers_api
uv sync
uv run pytest tests/ -v
uv run crewai run
```

### 5. `sample_flow` — Event-Driven CrewAI Flow
Illustrates high-level execution flows using `@flow` decorators, state management, and output directory customization.

```powershell
cd sample_flow
uv sync
uv run crewai run
```

*Customizing Output Location:*
```powershell
$env:CREW_OUTPUT_DIR = "./.crewai/output"
```

---

## 🔑 Environment Configuration

Create a `.env` file in the root directory or inside individual sub-project folders before running LLM-dependent crews:

```env
# OpenAI API Key (Required for default LLM configurations)
OPENAI_API_KEY=your-openai-api-key-here

# Optional: Custom model specification
OPENAI_MODEL_NAME=gpt-4o-mini

# Optional: Serper API Key for web search capabilities
SERPER_API_KEY=your-serper-api-key-here
```

> **Security Reminder**: Never commit `.env` files, credentials, vector databases, or output artifacts to Git. They are ignored via `.gitignore`.

---

## 🧪 Testing & Quality Assurance

To ensure repository integrity, run the complete test suite and syntax verification commands from the root directory:

```powershell
# 1. Run unit tests for custom tools
uv run pytest numbers_api/tests -q

# 2. Verify syntax compilation across all source directories
uv run python -m compileall -q main.py learn_crew_ai basic_crewai/src chat_bot/src marketing_crewai/src numbers_api/src sample_flow/src

# 3. Verify dependency lockfile consistency
uv lock --check
```

---

## 🛡️ Security Best Practices

- **API Security**: Secrets are loaded exclusively from environment variables via `python-dotenv`.
- **Bounded Requests**: Network calls inside custom tools specify explicit timeout parameters to prevent hanging processes.
- **Input Validation**: All custom tools use Pydantic models to sanitize user inputs before external API invocation.
- **Isolated Artifacts**: Generated text files and local databases (e.g., ChromaDB locks) are strictly ignored by `.gitignore`.

---

## 📄 Attribution & License

- **Attribution**: Based on educational examples from [akmadan/learn_crewai](https://github.com/akmadan/learn_crewai), restructured and hardened for production patterns.
- **License**: Released under the [MIT License](LICENSE).

