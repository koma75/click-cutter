# Click-Cutter

Click-Cutter is a [Coockiecutter](https://github.com/cookiecutter/cookiecutter) template to create a quick-and-dirty CLI tool based on 
[CLICK](https://click.palletsprojects.com/).

NOTE: the base code this template generates is not really intended for production level use.

## Usage

~~~Shell
cookiecutter https://github.com/koma75/click-cutter
~~~

After executing the command above, you will be prompted with several parameter setting questions.
Enter the parameters as described below to customise the template for your project needs.

* project_name
    * Name of your project.  Can include spaces
    * default : My-Click-Project
* package_name
    * Name of your python package.  No spaces.
    * default : `{{ project_name|lower|replace(' ', '_')|replace('-', '_') }}`
* cli_name
    * Name of your CLI command
    * default : `{{ package_name|replace('_', '') }}`
* cli_type
    * Type of CLI.
    * simple (default)
        * Straight up CLI command with options and arguments
    * subcmd
        * CLI command with sub commands such as git.
* use_config_yaml
    * If your CLI takes configuration files for default settings or not
    * default : No
* project_ver
    * Initial Project version.  Used in the CHANGES.md first release entry and in
      the README versioning section.
    * default : 0.1.0
* project_desc
    * One line description of the project
    * default : This is my command-line project.
* python_ver
    * version of Python targeted by this project
    * 3.10 (default)
    * 3.11
    * 3.12
    * 3.13
    * 3.14
* author_name
    * Name of the author of this project.  Used in LICENSE
    * default : my_name
* author_email
    * email address of the athor.  Used in LICENSE
    * my_email@example.com
* license
    * License for this project.  The value is an [SPDX](https://spdx.org/licenses/)
      identifier and is used verbatim in pyproject.toml, in the source file
      headers as `SPDX-License-Identifier`, and to pick the LICENSE text.
    * MIT (default)
        * [MIT License](https://opensource.org/licenses/MIT)
    * BSD-2-Clause
        * [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause)
    * BSD-3-Clause
        * [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)
    * Apache-2.0
        * [Apache License 2.0](https://opensource.org/licenses/Apache-2.0)
    * None
        * No License specified. Only Copyright will be displayed in LICENSE
          and no `SPDX-License-Identifier` is written in the source headers.
* github_user
    * Github username of the author
    * default : my_username
* project_url
    * Project Homepage URL. defaults to github with project name based repository under
      author's username.
    * deafault : `https://github.com/{{ github_user }}/{{ project_name|replace(' ','-') }}/`
