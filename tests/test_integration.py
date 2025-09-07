import unittest
import sys
from pathlib import Path

#added the import files that will be required for the final testing ..
#in this testing we will be doing the combine cli as well as agent testing
#next we will do the same thing by adding the src


# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from agent import MemoryEnhancedAgent

# here we will be adding the src path for the memory agent 
# for the memory agent 


class TestMemoryIntegration(unittest.TestCase):

    #created the class for the testing integratively
    def setUp(self):
        self.agent = MemoryEnhancedAgent(name="TestBruno")

        #setup of the memory enhance function is done

    def test_full_conversation_flow(self):
        """Test complete conversation with memory"""
        # First conversation
        self.agent.save_conversation(
            "I'm learning Python", 
            "Great! Python is an excellent language to start with."
        )

    ## i have now added the conversation for testting we will test the function with this convo
    # but ya we will add another conversation so that we do not rely on just one convo..