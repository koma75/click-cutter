#!/usr/bin/env python
# -*- coding: utf-8 -*-

{%- if cookiecutter.license == 'BSD3' %}
# BSD 3-Clause License
# 
# Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }} <{{cookiecutter.author_email}}>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this
#    list of conditions and the following disclaimer in the documentation and/or
#    other materials provided with the distribution.
# 
# 3. Neither the name of {{ cookiecutter.project_name }} nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
{%- elif cookiecutter.license == 'BSD2' %}
# BSD 2-Clause License
# 
# Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }} <{{cookiecutter.author_email}}>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
{%- else %}
# Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }} <{{cookiecutter.author_email}}>
# All rights reserved.
{%- endif %}

"""Main CLI Setup and Entrypoint."""

from __future__ import absolute_import, division, print_function

# Import the main click library
import click
# Import the sub-command implementations
from .{{cookiecutter.cli_name}} import {{cookiecutter.cli_name}}
# Import the version information
from {{cookiecutter.package_name}}.version import __version__

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
