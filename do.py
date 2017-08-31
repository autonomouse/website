#!/usr/bin/env python3
import os
import sys
import argparse
from subprocess import check_call, check_output


python_version = "python3"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument('extra', nargs='*')
    args = parser.parse_args()

    args_list = []
    args_dict = {}
    for arg in args.extra:
        if '=' in arg:
            key, value = arg.split('=')
            args_dict[key] = value
        else:
            args_list.append(arg)
    private_methods = TaskBase().getAvailableMethods()
    tasks = Tasks()
    public_methods = tasks.getAvailableMethods()
    available_methods = [
        method for method in public_methods if method not in private_methods]
    try:
        method = getattr(tasks, args.command)
    except AttributeError:
        print("There is no '" + args.command + "' command.")
        print("Available commands: \n * " + "\n * ".join(available_methods))
        sys.exit()
    method(*args_list, **args_dict)


class TaskBase():
    """Helper methods, not meant to be called from the cli. """

    def getAvailableMethods(self):
        return [func for func in dir(self) if callable(getattr(self, func))
                and not func.startswith("__")]

    def sudo(self, cmd):
        sudo_cmd = ["sudo"]
        sudo_cmd.extend(cmd)
        return check_output(sudo_cmd)

    def mkdir_p(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def manage(self, cmd):
        print("Running the '" + " ".join(cmd) + "' management command")
        manage_cmd = [python_version, "django_backend/manage.py"]
        manage_cmd.extend(cmd)
        return check_output(manage_cmd)

    def install_os_deps(self):
        print("Installing dependencies via apt")
        deps = ["python3-pip"]
        cmd = ["sudo", "apt", "install"]
        cmd.extend(deps)
        return check_output(cmd)

    def install_django_deps(self):
        print("Installing django dependencies via pip")
        cmd = ["pip3", "install", "--user", "-r",
               "requirements/django.txt"]
        return check_output(cmd)


class Tasks(TaskBase):
    """Tasks meant to be callable from the cli. """

    def install(self):
        self.install_os_deps()
        self.install_django_deps()
        print("Done")

    def schema(self, filetype="png"):
        """Generates an image depicting the current database schema. """
        dot = self.manage([
            "graph_models", "-X", "TimeStampedBaseModel", "-E", "-a"])
        with open(application + ".dot", "wb") as text_file:
            text_file.write(dot)
        self.run(["dot", "-T" + filetype, application + ".dot", "-o",
                  application + "_schema." + filetype])
        self.run(["rm", application + ".dot"])
        print("Schema generated at {0}_schema.{1}".format(
              application, filetype))

    def runserver(self):
        self.manage(["collectstatic", "--noinput"])
        self.manage(["makemigrations"])
        self.manage(["migrate"])
        self.manage(["runserver"])

if __name__ == "__main__":
    sys.exit(main())
