# test_swamppaprika.py
"""
Tests for SwampPaprika module.
"""

import unittest
from swamppaprika import SwampPaprika

class TestSwampPaprika(unittest.TestCase):
    """Test cases for SwampPaprika class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SwampPaprika()
        self.assertIsInstance(instance, SwampPaprika)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SwampPaprika()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
