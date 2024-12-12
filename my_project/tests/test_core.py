"""
Tests for core functionality.
"""

from my_project.core import hello_world

def test_hello_world():
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"
    assert hello_world("Python") == "Hello, Python!" 