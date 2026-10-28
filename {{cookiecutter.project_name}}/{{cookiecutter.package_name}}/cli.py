#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }} <{{cookiecutter.author_email}}>
{%- if cookiecutter.license != 'None' %}
# SPDX-License-Identifier: {{cookiecutter.license}}
{%- else %}
# All rights reserved.
{%- endif %}

"""Main CLI Setup and Entrypoint."""

from __future__ import absolute_import, division, print_function

# Import the main click library
import click
# Import the sub-command implementations
from .{{cookiecutter.cli_name}} import {{cookiecutter.cli_name}}
# Import the version information
from {{cookiecutter.package_name}} import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

{%- if cookiecutter.cli_type == 'subcmd' %}
@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def cli():
    """cli tool: {{cookiecutter.project_desc}}"""
    pass

@cli.command()
@click.argument('ARG')
@click.option(
    '--flag', '-f', is_flag=True,
    help='some flag option'
    )
{%- if cookiecutter.use_config_yaml == "Yes" %}
@click.option(
    '--config', '-c', default="./{{ cookiecutter.package_name }}.yml",
    type=click.Path(exists=False, dir_okay=False, writable=True, resolve_path=True),
    metavar='<cfg>',
    help='Configuration File (default: {{ cookiecutter.package_name }}.yml)'
    )
{%- endif %}
@click.option(
    '--fmt', '-f', default="defaultvalue", type=str,
    metavar='<fmt>',
    help='string option'
    )
@click.option(
    '--verbose', '-v', is_flag=True,
    help='output in verbose mode'
    )
def subcmd1(**kwargs):
    """sample subcmd"""
    {{cookiecutter.cli_name}}.cmd(kwargs)
    pass

@cli.command()
@click.argument('ARG')
@click.option(
    '--message', '-m', multiple=True,
    help='some flag option'
    )
{%- if cookiecutter.use_config_yaml == "Yes" %}
@click.option(
    '--config', '-c', default="./{{ cookiecutter.package_name }}.yml",
    type=click.Path(exists=False, dir_okay=False, writable=True, resolve_path=True),
    metavar='<cfg>',
    help='Configuration File (default: {{ cookiecutter.package_name }}.yml)'
    )
{%- endif %}
@click.option(
    '--choice', '-c', type=click.Choice(['choice1', 'choice2']),
    help='choice option'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
def subcmd2(**kwargs):
    """sample subcmd"""
    #{{cookiecutter.cli_name}}.cmd2(kwargs)
    print(kwargs)
    pass
{%- else %}
@click.command()
@click.argument('ARG')
@click.option(
    '--flag', '-f', is_flag=True,
    help='some flag option'
    )
{%- if cookiecutter.use_config_yaml == "Yes" %}
@click.option(
    '--config', '-c', default="./{{ cookiecutter.package_name }}.yml",
    type=click.Path(exists=False, dir_okay=False, writable=True, resolve_path=True),
    metavar='<cfg>',
    help='Configuration File (default: {{ cookiecutter.package_name }}.yml)'
    )
{%- endif %}
@click.option(
    '--fmt', '-f', default="defaultvalue", type=str,
    metavar='<fmt>',
    help='string option'
    )
@click.option(
    '--verbose', '-v', count=True,
    help='output in verbose mode'
    )
@click.version_option(version=__version__)
def cli(**kwargs):
    """{{cookiecutter.project_desc}}
    """
    {{cookiecutter.cli_name}}.cmd(kwargs)
    print(kwargs)
    pass
{%- endif %}

# Entry point
def main():
    """Main script."""
    cli()

if __name__ == '__main__':
    main()
