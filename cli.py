#! /bin/python
import click
from extractor import extract 


@click.command()
@click.option('--filepath', default="./package.json", help="the targetted package.json uri")
def extract_dependencies(filepath):
    extract(filepath)

if __name__=="__main__":
    extract_dependencies()
