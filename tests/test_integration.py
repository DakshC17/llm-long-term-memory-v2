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

         # Second conversation that should remember the first
        results = self.agent.search_memories("Python programming")



         # Should find the previous conversation
        self.assertTrue(len(results['documents'][0]) > 0)
        self.assertIn("Python", results['documents'][0][0])

        ##added the finding logic so that it finds the conversation if it finds we will be success full on our testing combined one with both.

    def test_personality_consistency(self):
        """Test that personality settings work"""
        agent1 = MemoryEnhancedAgent(personality="Brain_Powerhouse")
        agent2 = MemoryEnhancedAgent(personality="creative_problem_solver")


        ## above i have added my test for personality and will test it 
        
        self.assertEqual(agent1.personality, "Brain_Powerhouse")
        self.assertEqual(agent2.personality, "creative_problem_solver")

if __name__ == "__main__":
    unittest.main()


    # lets see the execution if it works or not
