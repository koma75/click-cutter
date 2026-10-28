import os, glob
from invoke import task

##############################################
### Setup default variables
##############################################

PY_VERSION = "{{cookiecutter.python_ver}}"

##############################################
### Helper Functions
##############################################

def run_rm(c, paths):
    """run rm -rf command equivalent for each of paths

    Args:
        c (Obj): invoke context object
        paths (List): List of paths to remove
    """
    # May not be necessary for *nix since rm command works on both files and directories,
    # But to keep consistency across platforms, use Python glob to expand all wildcards.
    files = []
    for f in paths:
        files.extend(glob.glob(f))

    # run file removal function based on platform
    if os.name == 'nt':
        for f in files:
            if os.path.isdir(f):
                c.run(f"rmdir /s /q {f}")
            else:
                c.run(f"del /f /q {f}")
    else:
        for f in files:
            c.run(f"rm -rf {f}")
    pass


##############################################
### Invoke Task Definitions
##############################################

@task()
def clean(c):
    """remove package artifacts"""
    run_rm(c, ["dist", "*.egg-info"])
    pass

@task()
def venv(c):
    """initialize a uv-managed dev venv"""
    c.run(f"uv venv --python {PY_VERSION} .venv")
    c.run("uv pip install build twine")

@task()
def freeze(c):
    """save requirements.txt"""
    c.run("uv pip freeze > requirements.txt")
    pass

@task(pre=[clean])
def package(c):
    """Generate sdist"""
    c.run("uv build")

@task(pre=[package])
def publish(c):
    """upload to PyPi"""
    c.run("uv run twine upload dist/*")
    pass

@task(pre=[package])
def pubtest(c):
    """upload to pypitest"""
    c.run("uv run twine upload --repository pypitest dist/*")
    pass

@task(pre=[freeze])
def install(c):
    """install package from requirements.txt"""
    c.run("uv pip install -r requirements.txt")

@task(pre=[venv], default=True)
def build(c):
    """Build and install as editable"""
    c.run("uv pip install --editable .")
    pass
