import click
from scrummy.rollover import rollover_todo


@click.group()
def cli():
    pass


@cli.command()
@click.argument('when')
def rollover(when):
    rollover_todo(when)


if __name__ == '__main__':
    cli()
