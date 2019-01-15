import click
from click.testing import CliRunner
from playing_with_math import cli

def test_math1():
    runner = CliRunner()
    result = runner.invoke(cli, ["1","+","4"])
    assert result.exit_code == 0
    assert result.output == "5.0\n"

if __name__ == '__main__':
    test_math1()