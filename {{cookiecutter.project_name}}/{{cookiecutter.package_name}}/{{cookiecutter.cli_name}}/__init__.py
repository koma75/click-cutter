#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }} <{{cookiecutter.author_email}}>
{%- if cookiecutter.license != 'None' %}
# SPDX-License-Identifier: {{cookiecutter.license}}
{%- else %}
# All rights reserved.
{%- endif %}

"""
{{cookiecutter.project_desc}}

.. currentmodule:: {{cookiecutter.package_name}}.{{cookiecutter.cli_name}}
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>
"""
