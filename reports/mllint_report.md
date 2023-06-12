# ML Project Report
**Project** | **Details**
--------|--------
Date    | Mon, 12 Jun 2023 14:25:13 +0200 
Path    | `/home/amoraru/Documents/MSc/Q4/REMLA/model-training`
Config  | `pyproject.toml`
Default | Yes
Git: Remote URL | `git@github.com:remla23-team08/model-training.git`
Git: Commit     | `80dc0969aae353303cb3868c51a425f903ba053d`
Git: Branch     | `feature/improve-code-quality`
Git: Dirty Workspace?  | Yes
Number of Python files | 9
Lines of Python code   | 219

---

## Reports

### Version Control (`version-control`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Git | `version-control/code/git`
✅ | 100.0% | 1 | Project should not have any large files in its Git history | `version-control/code/git-no-big-files`
✅ | 100.0% | 1 | DVC: Project uses Data Version Control | `version-control/data/dvc`
✅ | 100.0% | 1 | DVC: Is installed | `version-control/data/dvc-is-installed`
✅ | 100.0% | 1 | DVC: Folder '.dvc' should be committed to Git | `version-control/data/commit-dvc-folder`
✅ | 100.0% | 1 | DVC: Should have at least one remote data storage configured | `version-control/data/dvc-has-remote`
✅ | 100.0% | 1 | DVC: Should be tracking at least one data file | `version-control/data/dvc-has-files`
✅ | 100.0% | 1 | DVC: File 'dvc.lock' should be committed to Git | `version-control/data/commit-dvc-lock`
 | _Total_ | | | 
✅ | **100.0**% | | Version Control | `version-control`

### Dependency Management (`dependency-management`) — **66.7**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
❌ | 0.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
❌ | **66.7**% | | Dependency Management | `dependency-management`

#### Details — Project should only use one dependency manager — ❌

Your project was found to be using multiple dependency managers: [Poetry setup.py]

The `setup.py` in your project is redundant and should be removed, as you can also use Poetry to build your project into a Python package using `poetry build`, see the [Poetry Docs](https://python-poetry.org/docs/libraries/#packaging) to learn more.

### Code Quality (`code-quality`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
✅ | 100.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
✅ | 100.0% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`
 | _Total_ | | | 
✅ | **100.0**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Black
- isort
- Bandit
- Pylint
- Mypy


#### Details — Pylint reports no issues with this project — ✅

Congratulations, Pylint is happy with your project!

#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — Bandit reports no issues with this project — ✅

Congratulations, Bandit is happy with your project!

### Testing (`testing`) — **38.9**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 55.6% | 1 | Project has automated tests | `testing/has-tests`
❌ | 0.0% | 1 | Project passes all of its automated tests | `testing/pass`
❌ | 0.0% | 1 | Project provides a test coverage report | `testing/coverage`
✅ | 100.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **38.9**% | | Testing | `testing`

#### Details — Project has automated tests — ❌

There is **1** test file in your project, which meets the minimum of **1** test file required.

However, this only equates to **11.111111%** of Python files in your project being tests, while `mllint` expects that **20%** of your project's Python files are tests.

#### Details — Project passes all of its automated tests — ❌

No test report was provided.

Please update the `testing.report` setting in your project's `mllint` configuration to specify the path to your project's test report.

When using `pytest` to run your project's tests, use the `--junitxml=<filename>` option to generate such a test report, e.g.:
```sh
pytest --junitxml=tests-report.xml
```


#### Details — Project provides a test coverage report — ❌

No test coverage report was provided.

Please update the `testing.coverage.report` setting in your project's `mllint` configuration to specify the path to your project's test coverage report.

Generating a test coverage report with `pytest` can be done by adding and installing `pytest-cov` as a development dependency of your project. Then use the following command to run your tests and generate both a test report as well as a coverage report:
```sh
pytest --junitxml=tests-report.xml --cov=path_to_package_under_test --cov-report=xml
```


### Continuous Integration (`ci`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
✅ | **100.0**% | | Continuous Integration | `ci`

## Errors

1 error(s) occurred while analysing your project:
- ❌ **Code Quality** - 1 error occurred:
	* Mypy failed to run: failed to parse Mypy message 'tests/test_MLdevel.py:10: error: Unused "type: ignore" comment': error parsing ' error' as column number: strconv.Atoi: parsing " error": invalid syntax


