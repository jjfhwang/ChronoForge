# test_chronoforge.py
"""
Tests for ChronoForge module.
"""

import unittest
from chronoforge import ChronoForge

class TestChronoForge(unittest.TestCase):
    """Test cases for ChronoForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChronoForge()
        self.assertIsInstance(instance, ChronoForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChronoForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
