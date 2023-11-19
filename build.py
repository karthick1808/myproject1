# build.py

from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
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
