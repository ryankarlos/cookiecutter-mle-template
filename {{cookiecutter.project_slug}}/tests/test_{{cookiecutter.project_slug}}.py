"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }} import cli

{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}


def test_command_line_interface():
    """Test the CLI."""
    { % - if cookiecutter.command_line_interface | lower == 'click' %}
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{   %- endif %}
