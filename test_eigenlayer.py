# test_eigenlayer.py
"""
Tests for EigenLayer module.
"""

import unittest
from eigenlayer import EigenLayer

class TestEigenLayer(unittest.TestCase):
    """Test cases for EigenLayer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EigenLayer()
        self.assertIsInstance(instance, EigenLayer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EigenLayer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
