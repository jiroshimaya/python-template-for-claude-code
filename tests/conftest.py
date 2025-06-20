"""Pytest configuration and fixtures."""

import logging
import os
import tempfile
from collections.abc import Iterator
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir() -> Iterator[Path]:
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture(autouse=True)
def reset_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Reset environment variables for each test."""
    # Remove any test-specific environment variables
    test_env_vars = [var for var in os.environ if var.startswith("TEST_")]
    for var in test_env_vars:
        monkeypatch.delenv(var, raising=False)


@pytest.fixture
def capture_logs(caplog: pytest.LogCaptureFixture) -> pytest.LogCaptureFixture:
    """Capture logs for testing with proper level."""
    # テスト用にログレベルを設定
    caplog.set_level(logging.DEBUG)
    return caplog


# pytestの起動時の基本設定
def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest with basic setup."""
    pass
