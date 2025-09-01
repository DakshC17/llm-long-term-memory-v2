"""
Bruno Agent - Memory Enhanced AI Agent
Imports functions from the notebook implementation
"""

import sys
import os
from pathlib import Path

# Add project root and notebooks to path
project_root = Path(__file__).parent.parent
notebooks_path = project_root / "notebooks"
sys.path.append(str(project_root))
sys.path.append(str(notebooks_path))

# Import required libraries
import chromadb
import ollama
from datetime import datetime
import uuid

class MemoryEnhancedAgent:
    def __init__(self, name="Bruno", personality="Brain_Powerhouse"):
        self.name = name
        self.personality = personality
        self.model = "llama3.2:3b"
        
        # Connect to persistent ChromaDB (project root, not src folder)
        db_path = Path(__file__).parent.parent / "chroma_db"
        client = chromadb.PersistentClient(path=str(db_path))
        self.collection = client.get_or_create_collection(name="conversation_memory")
        
        # Agent personality definitions (from notebook)
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
    
    def search_memories(self, query, n_results=3):
        """Search for relevant conversations in memory"""
        try:
            if self.collection.count() == 0:
                return {'documents': [[]], 'metadatas': [[]]}
            
            results = self.collection.query(
                query_texts=[query],
                n_results=min(n_results, self.collection.count())
            )
            
            return results
            
        except Exception as e:
            print(f"Search error: {e}")
            return {'documents': [[]], 'metadatas': [[]]}

    def save_conversation(self, user_message, ai_response, topic=None):
        """Save conversation to vector memory"""
        try:
            conversation_id = str(uuid.uuid4())
            
            conversation_text = f"User: {user_message}\nAI: {ai_response}"
            
            metadata = {
                "conversation_id": conversation_id,
                "timestamp": datetime.now().isoformat(),
                "user_message": user_message,
                "ai_response": ai_response,
                "topic": topic or "general",
                "user_level": "learning",
                "agent_name": self.name,
                "personality": self.personality
            }
            
            self.collection.add(
                documents=[conversation_text],
                metadatas=[metadata],
                ids=[conversation_id]
            )
            
            return conversation_id
            
        except Exception as e:
            print(f"Save error: {e}")
            return None

    def format_memory_context(self, search_results):
        """Format search results into context for the LLM"""
        if not search_results['documents'][0]:
            return "No relevant conversation history found."
        
        context = "=== RELEVANT CONVERSATION HISTORY ===\n\n"
        
        for i, (doc, metadata) in enumerate(zip(
            search_results['documents'][0], 
            search_results['metadatas'][0]
        )):
            context += f"Memory {i+1}:\n{doc}\n"
            context += f"Topic: {metadata.get('topic', 'Unknown')}\n"
            context += f"User Level: {metadata.get('user_level', 'Unknown')}\n"
            context += f"Date: {metadata.get('timestamp', 'Unknown')}\n"
            context += "-" * 50 + "\n\n"
        
        return context

    def get_personality_prompt(self):
        """Get personality-specific prompt"""
        personality_info = self.personalities.get(self.personality, self.personalities["Brain_Powerhouse"])
        
        prompt = f"""You are {self.name}, a {personality_info['role']}.

YOUR PERSONALITY TRAITS:
{chr(10).join(f"- {trait}" for trait in personality_info['traits'])}

COMMUNICATION STYLE: {personality_info['style']}

You maintain consistent personality while being genuinely helpful and contextual."""
        
        return prompt

    def agent_chat(self, user_message, save_to_memory=True, topic=None):
        """Main chat function with memory integration and learning"""
        try:
            # Search for relevant memories
            memory_results = self.search_memories(user_message)
            memory_context = self.format_memory_context(memory_results)
            
            # Build enhanced prompt with personality + memory
            personality_prompt = self.get_personality_prompt()
            
            system_prompt = f"""{personality_prompt}

{memory_context}

ENHANCED INSTRUCTIONS:
- Use the conversation history to provide personalized responses
- Reference relevant past discussions naturally
- Maintain your personality consistently
- Build upon the user's learning journey
- Show genuine interest in their progress
- If the memory context isn't relevant, focus on being helpful with your established personality

Remember: You are {self.name} with a {self.personality} personality. Always maintain this character while being helpful and contextual."""

            # Generate response with Ollama
            response = ollama.chat(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': user_message}
                ]
            )
            
            ai_response = response['message']['content']
            
            # Save conversation to memory (if enabled)
            if save_to_memory:
                self.save_conversation(
                    user_message=user_message,
                    ai_response=ai_response,
                    topic=topic
                )
            
            return ai_response
            
        except Exception as e:
            error_msg = f"Sorry, I encountered an error: {e}"
            return error_msg

# For backward compatibility and testing
def create_agent(name="Bruno", personality="Brain_Powerhouse"):
    """Factory function to create a MemoryEnhancedAgent"""
    return MemoryEnhancedAgent(name=name, personality=personality)

# Test if module is run directly
if __name__ == "__main__":
    print("Testing Bruno Agent...")
    bruno = MemoryEnhancedAgent()
    print(f"Agent created: {bruno.name}")
    print(f"Personality: {bruno.personality}")
    print(f"Memory count: {bruno.collection.count()}")
    print("✅ Agent module working!")