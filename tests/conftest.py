from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(scope="session")
def baseline_activities():
    """Capture the original in-memory data once for deterministic test resets."""
    return deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities(baseline_activities):
    """Reset mutable in-memory activity state before every test."""
    activities.clear()
    activities.update(deepcopy(baseline_activities))


@pytest.fixture
def client():
    return TestClient(app)
