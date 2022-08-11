"""Tests for `{{ cookiecutter.project_slug }}` package."""

from click.testing import CliRunner
import pytest
from {{cookiecutter.project_slug}} import (  # noqa
    cli,
    {{ cookiecutter.project_slug }},
)


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
