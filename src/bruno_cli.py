
"""
Bruno CLI - Memory-Enhanced AI Agent Command Line Interface
"""

import sys
import os
import argparse
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import chromadb
import ollama
from datetime import datetime
import json
import uuid

# ------------Now we will start to build the cli-------------------



def create_cli_parser():
    """Create command line argument parser"""
    parser = argparse.ArgumentParser(description="Bruno - Memory-Enhanced AI Agent")
    parser.add_argument("--interactive", "-i", action="store_true", help="Start interactive chat mode")
    parser.add_argument("--message", "-m", type=str, help="Send a single message to Bruno")
    parser.add_argument("--memory-stats", action="store_true", help="Show memory statistics")
    parser.add_argument("--personality", "-p", type=str, default="Brain_Powerhouse", 
                       help="Set Bruno's personality (default: Brain_Powerhouse)")
    return parser

def print_welcome():
    """Print welcome message"""
    print("=" * 60)
    print("BRUNO - Memory Enhanced AI Agent")
    print("=" * 60)
    print("Bruno remembers your conversations and learns from them!")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.")
    print("=" * 60)

def interactive_mode(agent):
    """Run Bruno in interactive chat mode"""
    print_welcome()
    
    while True:
        try:
            user_input = input("\n💭 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(" Bruno: Goodbye! I'll remember our conversation.")
                break
                
            if not user_input:
                continue
                
            print(" Bruno: ", end="")
            response = agent.agent_chat(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n Bruno: Goodbye! I'll remember our conversation.")
            break
        except Exception as e:
            print(f"Error: {e}")