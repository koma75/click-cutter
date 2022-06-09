#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packaging settings."""

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

# from __future__ import absolute_import, unicode_literals
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

exec(compile(open('{{cookiecutter.package_name}}/version.py', "rb").read(),'{{cookiecutter.package_name}}/version.py', 'exec'))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{{ cookiecutter.project_name|replace(' ','-') }}',
    version=__version__,
    description='{{cookiecutter.project_desc}}',
    long_description=long_description,
    url='{{cookiecutter.project_url}}',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
{%- if cookiecutter.license == 'MIT' %}
    license='MIT',
{%- elif cookiecutter.license == 'BSD2' %}
    license='BSD 2-Clause',
{%- elif cookiecutter.license == 'BSD3' %}
    license='BSD 3-Clause',
{%- elif cookiecutter.license == 'Apache2' %}
    license='Apache',
{%- elif cookiecutter.license == 'None' %}
    license='None',
{%- endif %}
    classifiers=[
        # Maturity of the project
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
{%- if cookiecutter.license == 'MIT' %}
        'License :: OSI Approved :: MIT License',
{%- elif cookiecutter.license == 'BSD2' %}
        'License :: OSI Approved :: BSD License',
{%- elif cookiecutter.license == 'BSD3' %}
        'License :: OSI Approved :: BSD License',
{%- elif cookiecutter.license == 'Apache2' %}
        'OSI Approved :: Apache Software License',
{%- elif cookiecutter.license == 'None' %}
{%- endif %}
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: {{cookiecutter.python_ver}}',
        'Topic :: Utilities',
    ],

    keywords='cli',

    packages=find_packages(
        exclude=['dist', 'build', 'contrib', 'docs', 'tests']
        ),

    # add your package requirements
{%- if cookiecutter.use_config_yaml == 'Yes' %}
    install_requires=['click>=8,<9', 'PyYaml>=6,<7'],
{%- else %}
    install_requires=['click>=8,<9'],
{%- endif %}

    entry_points={
        'console_scripts': [
            '{{cookiecutter.cli_name}}={{cookiecutter.package_name}}.cli:main',
        ],
    },
)
