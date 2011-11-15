# `eclipse-get`

`eclipse-get` provides an easy way to install Eclipse packages on the command line. For example, installing PyDev involves jumping through multiple dialogs to add a new repository and waiting for the slow, memory-hungry package list. this makes it as simple as `eclipse-get install pydev`.

## Super-duper-mega-pre-alpha release

At current, this is probably incomplete and broken in many ways. **Don't use it yet.**

## Usage

* `eclipse-get list` - list packages available for install.
* `eclipse-get install PACKAGE_NAME...` - install a package or multiple packages.

For more info, run `eclipse-get --help`.

## Package you want not available?

`eclipse-get` keeps its own list of available packages, which span multiple repositories and include command-line-friendly short names. If there's a package you use which isn't in there, you can:

* Fork this project, add it to `data/packages.yaml`, and send a pull request
* File an issue, with the package's name, repository (if it's not in the Eclipse releases repo) and the IU (this usually looks like `org.somebody.something.feature.group`)
