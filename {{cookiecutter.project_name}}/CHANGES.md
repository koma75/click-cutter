# Changelog

Change-point identifiers: **[Added]** new feature/option · **[Changed]** behavior
changed · **[Breaking]** incompatible change · **[Minor]** cosmetic/clarification
· **[Performance]** performance improvement · **[Fixed]** bug fix.

## {{cookiecutter.project_ver}} ({% now 'local', '%Y.%m.%d' %})

**Summary:** First release.

**User-facing specification changes**

- **[Added]** `{{cookiecutter.cli_name}}`{% if cookiecutter.cli_type == 'subcmd' %} subcommands (`subcmd1`, `subcmd2`).{% else %} command line tool: {{cookiecutter.project_desc}}{% endif %}

**Bug fixes**

- (No bug fixes — initial implementation.)

**Other changes**

- Package skeleton, dependencies (`click`{% if cookiecutter.use_config_yaml == 'Yes' %}, `PyYAML`{% endif %}); setuptools-scm versioning; {% if cookiecutter.license != 'None' %}{{cookiecutter.license}} license applied{% else %}no license specified{% endif %}.
