# Contributing

We're so glad you're thinking about contributing to an 18F open source project!
If you're unsure about anything, just ask — or submit the issue or pull request
anyway. The worst that can happen is you'll be politely asked to change
something. We love all friendly contributions.

We want to ensure a welcoming environment for all of our projects. Our staff
follow the [18F Code of Conduct][code] and all contributors should do the same.

We encourage you to read this project's CONTRIBUTING policy (you are here), its
[LICENSE](LICENSE.md), and its [README](README.rst).

If you have any questions or want to read more, check out the
[18F Open Source Policy GitHub repository][os-policy], or just
[shoot us an email](mailto:18f@gsa.gov).

[code]: https://github.com/18F/code-of-conduct/blob/master/code-of-conduct.md
[os-policy]: https://github.com/18f/open-source-policy

## Coding Standards

We adhere to [PEP8][] for Python code
formatting. Before committing, please use `black .` to autoformat your code.

This project has a command to run all linters and unit tests:

```sh
python setup.py ultratest
```

For more information about developing on this project, see the
[development guide](http://cg-django-uaa.readthedocs.io/en/latest/developing.html).

[PEP8]: https://www.python.org/dev/peps/pep-0008/

## Pull request guidelines

Please follow our [Git Protocol][git] and [Code Review][review] guidelines.
[Glen Sanford's thoughts on code reviews][thoughts] are also well worth
reading.

[git]: https://github.com/18F/development-guide/tree/master/git_protocol
[review]: https://github.com/18F/development-guide/tree/master/code_review
[thoughts]: http://glen.nu/ramblings/oncodereview.php

### Commit message style guide:

- Write your commit message summary in the imperative: "Fix bug" and not
"Fixed bug" or "Fixes bug."  This convention matches up with commit messages
generated by commands like `git merge` and `git revert`.

- Under the summary, start by explaining why this change is necessary, and
add details to help the person reviewing your code understand what your
pull request is about.

- If the pull request fixes a GitHub issue, mention it at the bottom using
GitHub's syntax, such as `Fixes #123`.

Example:

```
Load seed using before(:suite) in RSpec config

**Why**:
- Loading the seed in a `before(:each)` block results in an unnecessary
database call before every single test, slowing down the test suite,
and making development less efficient.

**How**:
- Use `before(:suite)` instead, since the data that is loaded is not
meant to change, and so that only one database call is made.
- To prevent the data from being wiped out after each spec, configure
Database Cleaner to ignore those static tables.

Fixes #123
```

## Public domain

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.
