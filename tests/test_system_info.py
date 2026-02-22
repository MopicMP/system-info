"""Tests for system-info."""

import pytest
from system_info import info


class TestInfo:
    """Test suite for info."""

    def test_basic(self):
        """Test basic usage."""
        result = info("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            info("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = info(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
