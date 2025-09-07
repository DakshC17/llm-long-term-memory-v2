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