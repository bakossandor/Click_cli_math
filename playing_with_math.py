import click
from hello_helper import operation

@click.command()
@click.argument("first_num")
@click.argument("operator")
@click.argument("second_num")
def cli(first_num, operator, second_num):
    """A math cli program which can execute the basic 4 operation /\n 
    summation, substraction, multiplication, division
    it requires 3 parameters\n
    first_num - an integer or a float number\n
    operator - +,-,*,/\n
    second_num - an integer or a float number"""
    click.echo(str(operation(first_num, operator, second_num)))