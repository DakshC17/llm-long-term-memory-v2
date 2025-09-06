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