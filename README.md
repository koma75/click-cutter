# Click-Cutter

Click-Cutter is a [Coockiecutter](https://github.com/cookiecutter/cookiecutter) template to create a quick-and-dirty CLI tool based on 
[CLICK](https://click.palletsprojects.com/).

## Usage

~~~Shell
> coockiecutter path/to/click-cutter
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
    * Initial Project version (default is set to 0.1.0 since Semver is initially implied in Readme)
    * default : 0.1.0
* project_desc
    * One line description of the project
    * default : This is my command-line project.
* python_ver
    * version of Python targeted by this project
    * 3.8 (default)
    * 3.9
    * 3.10
* author_name
    * Name of the author of this project.  Used in LICENSE
    * default : my_name
* author_email
    * email address of the athor.  Used in LICENSE
    * my_email@example.com
* license
    * License for this project
    * MIT (default)
        * [MIT License](https://opensource.org/licenses/MIT)
    * BSD2
        * [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause)
    * BSD3
        * [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)
    * Apache2
        * [Apache License 2.0](https://opensource.org/licenses/Apache-2.0)
    * None
        * No License specified. Only Copyright will be displayed in LICENSE
* github_user
    * Github username of the author
    * default : my_username
* project_url
    * Project Homepage URL. defaults to github with project name based repository under
      author's username.
    * deafault : `https://github.com/{{ github_user }}/{{ project_name|replace(' ','-') }}/`
