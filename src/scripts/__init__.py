import click, datetime
from . import covid

@click.group()
def cli():
    click.echo("Hello world!!")

@click.command()
@click.option('--day', default=datetime.date.today(), help="day to check history")
@click.option('--country', default="India", help="country to check history")
def history(day, country):
    print(covid.history(day, country))

@click.command()
def stat():
    click.echo("printing statistics...")

cli.add_command(history)
cli.add_command(stat)