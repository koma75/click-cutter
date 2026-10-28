#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }} <{{cookiecutter.author_email}}>
{%- if cookiecutter.license != 'None' %}
# SPDX-License-Identifier: {{cookiecutter.license}}
{%- else %}
# All rights reserved.
{%- endif %}

from enum import IntEnum

{% if cookiecutter.use_config_yaml == 'Yes' %}
import yaml
{%- endif %}
import os
import re
from pprint import pformat
import click

class Level(IntEnum):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

def pout(msg=None, Verbose=0, level=Level.INFO, newline=True):
    """stdout support method
    All Error, Critical and Info are printed out.
    while Warning and Debug are printed only with verbosity setting.
    INFO -- Intended for standard output. output to STDOUT
    DEBUG -- Intended for debug output. Shown only in verbosity>=2 output to STDOUT
    WARNING -- Intended to show detailed warning. Shown only in verbosity>=1.  output to STDERR
    ERROR -- Intended to show error.  output to STDERR
    CRITICAL -- Intended to show critical error. output to STDERR

    Keyword Arguments:
        msg (string) -- message to print (default: {None})
        Verbose (Int) -- Set True to print DEBUG message (default: {0})
        level (Level) -- Set message level for coloring (default: {Level.INFO})
        newline (bool) -- set to False if trailing new line is not needed (default: {True})
    """
    error=False
    if level in {Level.NOTSET, Level.DEBUG}:
        # blah
        if Verbose < 2:
            return
        fg = "magenta"
    elif level == Level.INFO:
        fg = "green"
    elif level == Level.WARNING:
        if Verbose < 1:
            return
        fg = "yellow"
        error = True
    elif level in {Level.ERROR, Level.CRITICAL}:
        fg = "red"
        error = True
    else:
        fg = "white"
        pass
    click.echo(click.style(str(msg), fg=fg), nl=newline, err=error)

{% if cookiecutter.use_config_yaml == 'Yes' %}
def createConf(conf, verbose):
    """Generate default configuratino at path specified in conf

    Args:
        conf (string): Path to generate default configuration file to.
        verbose (int): Verbosity level
    """
    try:
        with click.open_file(conf, 'w', 'utf-8') as fd:
            fd.writelines([
                "option1: option1param\n",
                "option2: option2param\n",
                "optionArray:\n",
                "  - item1\n",
                "  - item2\n",
                "optionDict:\n",
                "  key1: item1\n",
                "  key2: item2\n",
                "  key3: item3\n",
            ])
    except:
        pout("could not create {file}".format(file=conf), verbose, Level.ERROR)
    pass
{%- endif %}

def cmd(kwargs):
    """{{cookiecutter.project_desc}}
    Implementation.

    Args:
        kwargs (dict): command line arguments parsed by Click library
    """
    verbose = kwargs["verbose"]
    pout("Command line arguments:", verbose, Level.INFO)
    pout(pformat(kwargs,depth=3,indent=4), verbose, Level.INFO)

{% if cookiecutter.use_config_yaml == 'Yes' %}
    # 0. Get information from config.yml
    # If file does not exist, create a default config file
    if not os.path.exists(kwargs['config']):
        createConf(kwargs['config'], verbose)
    try:
        with click.open_file(kwargs['config'], 'r') as cnf:
            conf = yaml.safe_load(cnf)
    except:
        pout("could not open config file: {file}".format(file=kwargs['config']), verbose, Level.ERROR)

    pout("Read config file:", verbose, Level.INFO)
    pout(pformat(conf,depth=3,indent=4), verbose, Level.INFO)
{%- endif %}
    # 1. Now parse kwargs
{%- if cookiecutter.use_config_yaml == 'Yes' %}
    # TODO: it may be a good time to merge the options specified in kwargs into conf to put all
    #       execution parameters in one place.
{%- endif %}

    # 2. and do it's bidding

    pass
