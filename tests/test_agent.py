##we willcreate a test file for testing the cli

import unittest
import sys
#remove couple of unnecessary packages 
from pathlib import Path
# WE IMPORTED THE REQUIRED PACKAGE FOR STARTING TO TEST

## Next step we will definitely add the src so that we acces the functions from there
# below is the snippet 
sys.path.append(str(Path(__file__).parent.parent / "src"))
from agent import MemoryEnhancedAgent

class TestAgent(unittest.TestCase):  # class for the test agent
    def setUp(self):
        self.agent = MemoryEnhancedAgent(name="TestBruno")
                ## definition for testing the bruno agent
    
    def test_init(self):
        #this is for creatung the test agent
        self.assertEqual(self.agent.name, "TestBruno")
        self.assertIsNotNone(self.agent.collection)

    ##now another definition willl of the save memory 
    def test_save_memory(self):
        ## it will test the save memories
        result = self.agent.save_conversation("test message", "test response")
        self.assertIsNotNone(result)
        
    