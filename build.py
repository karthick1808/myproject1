# build.py

from pybuilder.core import use_plugin, init, task

use_plugin("python.core", version="0.13.10")
use_plugin("python.unittest", {"output_directory": "target/reports/tests"})
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")
use_plugin("python.integrationtest")

default_task = "publish"
# build.py

project_name = "myproject1"
project_version = "1.0.0"

default_task = "publish"

@init
def set_properties(project):
    project.depends_on_requirements("requirements.txt")
    project.build_depends_on("pytest")

@task
def publish(project, logger):
    # Add your publishing logic here
    logger.info("Publishing the package")


@task("analyze")
def analyze():
    pass  # Add analysis tasks as needed


@task("clean")
def clean():
    pass  # Add clean-up tasks as needed
