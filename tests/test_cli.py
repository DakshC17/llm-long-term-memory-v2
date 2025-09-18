import unittest
import subprocess
import sys
from pathlib import Path

#imported the required files that will be required for cli testing..



class TestBrunoCLI(unittest.TestCase):
    def test_cli_help(self):
        """IT will Test that CLI help runs without error"""
        result = subprocess.run(
            [sys.executable, str(Path("src/bruno_cli.py")), "--help"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        ##class will check the help function for cli tetsing
        self.assertIn("Bruno - Memory AI Agent", result.stdout)
        self.assertEqual(result.returncode, 0)


##function will test the stats of runs 
    def test_cli_stats(self):
        """Test that CLI stats command runs"""
        result = subprocess.run(
            [sys.executable, str(Path("src/bruno_cli.py")), "-s"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )



        self.assertIn("Memory", result.stdout)
        self.assertEqual(result.returncode, 0)

if __name__ == "__main__":
    unittest.main()


#unit test gets completed as its very important phase for the dev


