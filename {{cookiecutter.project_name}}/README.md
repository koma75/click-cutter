# {{cookiecutter.project_name}}

{{cookiecutter.project_desc}}

ADD MY CLI DETAIL DESCRIPTION HERE

## Installation

~~~console
> pip install {{cookiecutter.package_name}}
~~~

## Usage

{% if cookiecutter.cli_type == "subcmd" %}

### Subcmd 1

Subcmd description

~~~console
> {{cookiecutter.cli_name}} subcmd1 --option1 --argopt1 arg -v
~~~

* -o, --option1
    * description
* -a, --argopt1 ARG
    * description
{%- if cookiecutter.use_config_yaml == 'Yes' %}
* -c, --config CFG
    * CFG: Path to Configuration File (default: {{cookiecutter.package_name}}.yml)
{%- endif %}
* -v, --verbose
    * verbosity

{% else %}

Command Line tool description

~~~console
> {{cookiecutter.cli_name}} --option1 --argopt1 arg -v
~~~

* -o, --option1
    * description
* -a, --argopt1 ARG
    * description
{%- if cookiecutter.use_config_yaml == 'Yes' %}
* -c, --config CFG
    * CFG: Path to Configuration File (default: {{cookiecutter.package_name}}.yml)
{%- endif %}
* -v, --verbose
    * verbosity

{% endif %}

{%- if cookiecutter.use_config_yaml == 'Yes' %}

### Configuration file

YAML based configuration file (default file name: {{cookiecutter.package_name}}.yaml)
is used to store default settings for the tool.
The command line options will take precedence over the configuration parameters.

following shows the default settings of the configuration

~~~yaml
option1: option1param
option2: option2param
optionArray:
  - item1
  - item2
optionDict:
  key1: item1
  key2: item2
  key3: item3
~~~
{%- endif %}

## Known Issues

Need to be implemented.

## Development

### Building an Executable

Install pyinstaller and package the project.
The project venv is managed by uv, so use uv to provision and run it.

First, create the dev venv and install the local package and pyinstaller

~~~console
>uv venv --python {{cookiecutter.python_ver}} .venv
>uv pip install --editable .
Processing /path/to/proj/{{cookiecutter.project_name}}
~snip~
Installing collected packages: {{cookiecutter.package_name}}
Successfully installed {{cookiecutter.package_name}}-{{cookiecutter.project_ver}}

>uv pip install pyinstaller
~snip~
Successfully installed pyinstaller-6.14.0
~~~

Use pyinstaller to build the exe file.

~~~console
>uv run pyinstaller {{cookiecutter.package_name}}/cli.py --onefile --name {{cookiecutter.cli_name}}
~snip~
13691 INFO: Building EXE from EXE-00.toc completed successfully.
~~~

Executable should be ready in dist/{{cookiecutter.cli_name}}.exe

### Versioning

The project will follow the [semver2.0](http://semver.org/) versioning scheme.  
With initial development phase starting at {{cookiecutter.project_ver}} and increasing
minor/patch versions until we deploy the tool to production
(and reach 1.0.0).

{% if cookiecutter.use_config_yaml == 'Yes' %}
The interface relevant to versioning is whatever defined in this
document's "Usage" section (includes all (sub)commands, their cli arguments,
and the format of the configuration file "{{cookiecutter.package_name}}.yaml").
{%- else %}
The interface relevant to versioning is whatever defined in this
document's "Usage" section (includes all (sub)commands and their cli arguments).
{%- endif %}

## Version History

See [CHANGES.md](CHANGES.md) for the full release history.
