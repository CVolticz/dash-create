#!/usr/bin/env python
# Main CLI setup definition file
import click
import os, sys, subprocess
from .fs_generator import FSGenerator


def _test_filepath(current, new):
    """ TODO: implment me
        # unit testing function for file path
        # return to cwd if build is not successful
    """
    try:
        os.chdir(new)
        print("Inserting inside-", os.getcwd())

    # Caching the exception
    except:
        print("Something wrong with specified \
            directory. Exception- ", sys.exc_info())

    # handling with finally
    finally:
        print("Restoring the path")
        os.chdir(current)
        print("Current directory is-", os.getcwd())


def generate_contents(dir):
    """
        function to generate contents 
        when builder is call
    """
    cwd = os.getcwd() + '/' + dir
    feGenObj = FSGenerator(cwd)
    feGenObj.generate_file_structure()


@click.group()
def main():
    """
        Simple CLI wrapper for interfacing
    """
    pass


# @click.argument('new', type=str)
# @click.option('--dash', '-d', default=True, type=bool, help='Generate Dash FrontEnd File Structure')
@main.command()
def build():
    """
        CLI Builder Tool to generate a file structure for plotly dash web application
    """
    dir_name = input('[project-name]: ')
    generate_contents(dir_name)


@main.command()
def run_app():
    """
        CLI Tool to run plotly application on dev mode
        Features:
            - check current dir,
            - if not project dir, raise warning
    """

    try:
        subprocess.run(['python', 'index.py'])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()


