"""Тесты пакета."""

import os

import pytest


def test_exists_tests_package() -> None:
    """Существует папка с тестами."""
    expected_folder = "tests"
    assert os.path.exists(expected_folder), (
        f"Убедитесь, что в проекте `python-tools-3` "
        f"создана папка `{expected_folder}`"
    )

    assert "__init__.py" in os.listdir(expected_folder), (
        """Папка с тестами - пакет"""
        f"Убедитесь, что в проекте `python-tools-3` "
        f"`{expected_folder}` является пакетом."
    )


@pytest.mark.parametrize(
    "test_module", [
        "test_annotation.py",
        "test_main.py",
        "test_package.py",
    ]
)
def test_tests_package_contains_case(test_module: str) -> None:
    """В пакете есть необходимые модули."""
    assert test_module in os.listdir("tests"), (
        f"Убедитесь, что в проекте `python-tools-3` "
        f"в пакете `tests` содержится модуль {test_module}."
    )
