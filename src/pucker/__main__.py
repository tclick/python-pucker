"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Pucker."""


if __name__ == "__main__":
    main(prog_name="python-pucker")  # pragma: no cover
