
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