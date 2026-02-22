from subprocess import check_call

# When the hook scripts are run, their current working directory is the root of the generated project.

# Initialize the git repo.
check_call(["git", "init", "--initial-branch", "main"])
check_call(["git", "add", ".gitignore"])
check_call(["git", "commit", "--message", "Add .gitignore", "--no-verify"])
check_call(["git", "remote", "add", "origin", "{{cookiecutter.package_url}}"])
check_call(["git", "add", "."])
