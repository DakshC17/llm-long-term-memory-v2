
"""Bruno CLI - Memory Enhanced AI Agent Interface"""

import sys
import argparse
from pathlib import Path


sys.path.append(str(Path(__file__).parent.parent))
from agent import MemoryEnhancedAgent

def main():
    # parsers
    parser = argparse.ArgumentParser(description="Bruno - Memory AI Agent")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("-m", "--message", help="Single message")
    parser.add_argument("-s", "--stats", action="store_true", help="Memory stats")
    parser.add_argument("-p", "--personality", default="Brain_Powerhouse", help="Personality")
    args = parser.parse_args()
    
    # creating bruno here
    bruno = MemoryEnhancedAgent(personality=args.personality)
    
    # Handle commands
    if args.stats:
        print(f" Memory: {bruno.collection.count()} conversations")
        print(f" Personality: {bruno.personality}")
        return
    
    if args.message:
        print(f"🧠 Bruno: {bruno.agent_chat(args.message)}")
        return
    
    if args.interactive:
        print("🧠 BRUNO - Type 'quit' to exit")
        while True:
            try:
                msg = input("\n💭 You: ").strip()
                if msg.lower() in ['quit', 'exit', 'bye']:
                    print("🧠 Bruno: Goodbye!")
                    break
                if msg:
                    print(f"🧠 Bruno: {bruno.agent_chat(msg)}")
            except KeyboardInterrupt:
                print("\n🧠 Bruno: Goodbye!")
                break
        return
    
    #  show help
    parser.print_help()

if __name__ == "__main__":
    main()