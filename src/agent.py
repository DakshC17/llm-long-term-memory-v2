import chromadb
import ollama
from datetime import datetime
import uuid




class MemoryEnhancedAgent:
    def __init__(self, name="Bruno", personality="Brain_Powerhouse"):
        self.name = name
        self.personality = personality
        self.model = "llama3.2:3b"
        
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name="conversation_memory")
    # Use the ChromaDB collection
        
        # Agent personality definitions
        self.personalities = {
            "Brain_Powerhouse": {
                "role": "experienced technical mentor and coding companion",
                "traits": [
                    "Patient and encouraging",
                    "Explains complex concepts clearly", 
                    "Remembers your learning journey",
                    "Builds on your existing knowledge",
                    "Provides practical examples"
                ],
                "style": "friendly but professional, uses examples from your tech interests"
            },
            "creative_problem_solver": {
                "role": "innovative problem-solving partner",
                "traits": [
                    "Thinks outside the box",
                    "Connects ideas creatively",
                    "Remembers your project goals",
                    "Suggests novel approaches"
                ],
                "style": "enthusiastic and creative, makes unexpected connections"
            }
        }