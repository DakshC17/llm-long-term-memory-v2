# LLM Long-Term Memory System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ChromaDB](https://img.shields.io/badge/vectordb-ChromaDB-green.svg)](https://www.trychroma.com/)
[![Ollama](https://img.shields.io/badge/llm-Ollama-orange.svg)](https://ollama.ai/)
[![Tests](https://img.shields.io/badge/tests-7%20passing-brightgreen.svg)](./tests/)

A production-ready system that provides Large Language Models with **persistent conversational memory** using vector databases. Meet **Bruno** - your memory-enhanced AI agent that remembers every conversation and learns from your interactions.

## Features

- **Persistent Memory**: Conversations stored in ChromaDB vector database
- **Intelligent Retrieval**: Context-aware responses using similarity search  
- **Personality System**: Customizable agent personalities (Brain_Powerhouse, Creative Problem Solver)
- **Cross-Session Continuity**: Remembers conversations across restarts
- **CLI Interface**: Production-ready command-line tool
- **Fully Tested**: Comprehensive test suite with 7 tests
- **Educational Journey**: Complete development notebooks included 

## Quick Start

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/DakshC17/llm-long-term-memory-v2.git
cd llm-long-term-memory-v2
```

2. **Set up Python environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Install Ollama and pull the model:**
```bash
# Install Ollama (visit https://ollama.ai for instructions)
ollama pull llama3.2:3b
```

### Usage

#### Interactive Chat Mode
```bash
python src/bruno_cli.py -i
```

**Example Output:**
```
BRUNO - Type 'quit' to exit

You: Hello Bruno! Can you help me with Python programming?
Bruno: Hello! I'm glad you're interested in learning about Python programming! As your technical mentor, I'm here to help you on your coding journey...

You: Do you remember we talked about machine learning before?
Bruno: Machine learning! I remember it like it was yesterday. We've had a great conversation about it in the past, haven't we?
```

<!-- #### Single Message Mode
```bash
python src/bruno_cli.py -m "Explain neural networks"
```

#### Memory Statistics
```bash
python src/bruno_cli.py -s
```
**Output:**
```
Memory: 15 conversations
Personality: Brain_Powerhouse
```

#### Custom Personality
```bash
python src/bruno_cli.py -i -p creative_problem_solver
```

## Architecture

```
llm-long-term-memory-v2/
├── Core System
│   ├── ChromaDB (Vector Storage)
│   ├── Ollama LLM (llama3.2:3b)
│   └── Memory Retrieval Engine
│
├── Development Journey
│   ├── setup_vectordb.ipynb      # Phase 1: Database Setup
│   ├── ollama_integration.ipynb  # Phase 2: LLM Integration  
│   └── agent_development.ipynb   # Phase 3: Agent Creation
│
├── Production Code
│   ├── agent.py                  # MemoryEnhancedAgent Class
│   └── bruno_cli.py             # Command Line Interface
│
├── Testing Suite
│   ├── test_agent.py            # Agent Core Tests
│   ├── test_cli.py              # CLI Command Tests
│   └── test_integration.py      # System Integration Tests
│
└── Persistent Storage
    └── chroma_db/               # Vector Database
```

## How It Works

### 1. Memory Storage
Every conversation is automatically saved to ChromaDB with:
- **Vector embeddings** for semantic similarity
- **Metadata**: timestamp, topic, personality, user level
- **Full conversation context** for retrieval

### 2. Intelligent Retrieval
When you ask Bruno something:
1. **Query vectorization** of your message
2. **Similarity search** in conversation history
3. **Context assembly** from relevant memories
4. **Enhanced response** using retrieved context

### 3. Personality System
Bruno adapts his responses based on personality:

**Brain_Powerhouse (Default):**
- Technical mentor and coding companion
- Patient and encouraging
- Explains complex concepts clearly
- Builds on your existing knowledge

**Creative Problem Solver:**
- Innovative problem-solving partner
- Thinks outside the box
- Connects ideas creatively
- Suggests novel approaches

## Example Workflow

### Memory Building Over Time

```bash
# First conversation
You: I'm learning Python
Bruno: Great! Python is excellent for beginners...

# Later conversation (Bruno remembers!)
You: Can you help with machine learning?
Bruno: Perfect! Since you're learning Python, ML is a natural next step...

# Even later (Building on context)
You: What about neural networks?
Bruno: Given our previous discussions about Python and ML, neural networks are...
```

## Testing

Run the complete test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Individual test files
python tests/test_agent.py      # Agent functionality
python tests/test_cli.py        # CLI commands  
python tests/test_integration.py # System integration
```

**Test Coverage:**
- Agent initialization and memory operations
- CLI help and statistics commands
- Memory saving and retrieval functionality
- Personality system consistency
- Full conversation workflow

## Requirements

- **Python 3.8+**
- **Ollama** with llama3.2:3b model
- **ChromaDB** for vector storage
- **Dependencies**: See `requirements.txt`

## Configuration

### Available CLI Options

```bash
python src/bruno_cli.py --help

options:
  -h, --help                    Show help message
  -i, --interactive            Start interactive chat mode
  -m, --message MESSAGE        Send a single message
  -s, --stats                  Show memory statistics  
  -p, --personality PERSONALITY Set personality (Brain_Powerhouse, creative_problem_solver)
```

### Memory Database

- **Location**: `./chroma_db/`
- **Type**: Persistent ChromaDB collection
- **Collection**: `conversation_memory`

## Use Cases

- **Personal AI Assistant**: Remember your preferences and conversation history
- **Learning Companion**: Track your educational progress and build on previous lessons
- **Technical Mentor**: Get contextual programming help that builds on your experience
- **Research Assistant**: Maintain context across long research sessions
- **Creative Partner**: Brainstorm ideas with memory of previous creative sessions

## Development Journey

This project was built in phases for educational purposes:

1. **Phase 1**: Vector database setup and conversation storage
2. **Phase 2**: LLM integration with memory-aware responses
3. **Phase 3**: AI agent development with personality system
4. **Phase 4**: Production CLI tool and testing suite

Each phase is documented in Jupyter notebooks in the `notebooks/` directory.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Run the test suite
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- **ChromaDB** for excellent vector database capabilities
- **Ollama** for local LLM inference
- **Python ecosystem** for amazing ML/AI libraries

---

**Built by [DakshC17](https://github.com/DakshC17)**

*Bruno remembers everything, so you don't have to!* -->   -->
