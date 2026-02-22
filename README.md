# Package Templates

This package is home to [CookieCutter](https://cookiecutter.readthedocs.io/)
templates for various types of packages.

### Creating a new Package

```shell
cruft create https://github.com/EverGrayTech/package_templates.git --directory="your chosen template"
# Answer any questions you're prompted with.
```

After applying the template, **git commit the files BEFORE making modifications** so 
that your changes can be reviewed separately from the output of the template.

```shell
cd <new directory>
git commit --all --message "Intialize package from template"
git push origin main
git checkout -b develop
```

Your newly created package likely has comments hightlighting examples, things of notes, 
and opportunities for further configuration which need to be addressed before your new 
package is released.

Search for `TODO`s within the files and update or remove them.

### Updating an existing Package

[Cruft](https://cruft.github.io/cruft/) is used to update boilerplate across packages 
when the source template changes.

```shell
cruft update
```

You may end up with `.rej` files listing merge conflicts between changes made in your 
package and the template.

Once you've resolved any conflicts, add and commit the changes including the updated 
`.cruft.json`.
