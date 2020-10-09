from pathlib import Path
import sys

import pytest


_SCRIPT_DIR = Path(__file__).absolute().parent
sys.path.insert(0, str(_SCRIPT_DIR / ".." / ".." / "genpinctrl"))


@pytest.fixture()
def data():
    """Pytest fixture to load test data files"""
    return _SCRIPT_DIR / "data"


@pytest.fixture()
def cubemx(data):
    """Pytest fixture to load test CubeMX files"""
    return data / "cubemx"
