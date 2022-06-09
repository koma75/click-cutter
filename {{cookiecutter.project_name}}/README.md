{{cookiecutter.project_name}}
========================================================================

{{cookiecutter.project_desc}}

ADD MY CLI DETAIL DESCRIPTION HERE

Installation
------------------------------------------------------------------------

~~~shell
> pip install {{cookiecutter.package_name}}
~~~

Usage
------------------------------------------------------------------------
{% if cookiecutter.cli_type == "subcmd" %}

### Subcmd 1

Subcmd description

~~~shell
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

~~~shell
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

Known Issues
------------------------------------------------------------------------

Need to be implemented.

Development
------------------------------------------------------------------------

### Building an Executable

Install pyinstaller and package the project.
May want to use venv when executing the pyinstaller.

First, enter venv and install the local package and pyinstaller

~~~shell
>. .venv/Scripts/activate
(.venv) >pip install .
Processing /path/to/proj/{{cookiecutter.project_name}}
~snip~
Installing collected packages: {{cookiecutter.package_name}}
    Running setup.py install for {{cookiecutter.package_name}} ... done
Successfully installed {{cookiecutter.package_name}}-0.1.0

(.venv) >pip install pyinstaller
~snip~
Successfully installed pyinstaller-3.6
~~~

Use pyinstaller to build the exe file.

~~~shell
(.venv) >pyinstaller {{cookiecutter.package_name}}\cli.py --onefile --name {{cookiecutter.cli_name}}
~snip~
13691 INFO: Building EXE from EXE-00.toc completed successfully.
~~~

Executable should be ready in dist/{{cookiecutter.cli_name}}.exe

### Versioning

The project will follow the [semver2.0](http://semver.org/) versioning scheme.  
With initial development phase starting at 0.1.0 and increasing
minor/patch versions until we deploy the tool to production
(and reach 1.0.0).

{%- if cookiecutter.use_config_yaml == 'Yes' %}
The interface relevant to versioning is whatever defined in this
document's "Usage" section (includes all (sub)commands, their cli arguments,
and the format of the configuration file "{{cookiecutter.package_name}}.yaml").
{%- else %}
The interface relevant to versioning is whatever defined in this
document's "Usage" section (includes all (sub)commands, and their cli arguments.
{%- endif %}

Version History
------------------------------------------------------------------------

Date        | Version   | Changes
:--         | --:       | :--
{% now 'local', '%Y.%m.%d' %}  | 0.1.0     | First Release
