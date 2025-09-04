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


    