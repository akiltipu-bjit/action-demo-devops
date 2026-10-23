"""Tests for the greeting app."""

from main import greet


def test_greet_default():
    """The default greeting should say Hello, World!"""
    assert greet() == "Hello, World!"


def test_greet_name():
    """Custom names should appear in the greeting."""
    assert greet("GitHub") == "Hello, GitHub!"
