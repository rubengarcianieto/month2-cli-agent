"""Smoke test: the package can be imported."""

import month2_cli_agent


def test_package_imports() -> None:
    """The package imports without errors."""
    assert month2_cli_agent is not None
