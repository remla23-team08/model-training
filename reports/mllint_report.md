# ML Project Report
**Project** | **Details**
--------|--------
Date    | Mon, 26 Jun 2023 16:14:26 +0200 
Path    | `/home/jvandersaag/Documents/REMLA/project/model-training`
Config  | `.mllint.yml`
Default | No
Git: Remote URL | `https://github.com/remla23-team08/model-training.git`
Git: Commit     | `c3e2cf34acbf5bebc2f2698a107ad708780d705b`
Git: Branch     | `testing`
Git: Dirty Workspace?  | Yes
Number of Python files | 11
Lines of Python code   | 253

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

### Dependency Management (`dependency-management`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project properly keeps track of its dependencies | `dependency-management/use`
✅ | 100.0% | 1 | Project should only use one dependency manager | `dependency-management/single`
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
✅ | **100.0**% | | Dependency Management | `dependency-management`

### Code Quality (`code-quality`) — **65.3**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 76.5% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
❌ | 0.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
❌ | 80.4% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`
 | _Total_ | | | 
❌ | **65.3**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Mypy
- Black
- isort
- Bandit
- Pylint


#### Details — Pylint reports no issues with this project — ❌

Pylint reported **6** issues with your project:

- `tests/test_integration.py:19,0` - _(C0303)_ Trailing whitespace
- `tests/test_integration.py:24,0` - _(C0303)_ Trailing whitespace
- `tests/test_integration.py:41,0` - _(C0303)_ Trailing whitespace
- `tests/test_integration.py:53,0` - _(C0304)_ Final newline missing
- `tests/test_integration.py:51,12` - _(E0602)_ Undefined variable 'evaluate_model'
- `tests/test_integration.py:53,11` - _(R1716)_ Simplify chained comparison between the operands


#### Details — Black reports no issues with this project — ❌

Black reported **4** files in your project that it would reformat:

- `tests/test_modeldevelopment.py`
- `tests/test_features.py`
- `tests/conftest.py`
- `tests/test_integration.py`

Black can fix these issues automatically when you run `black .` in your project.

#### Details — isort reports no issues with this project — ❌

isort reported **2** files in your project that it would fix:

- `tests/test_integration.py` - Imports are incorrectly sorted and/or formatted.
- `tests/conftest.py` - Imports are incorrectly sorted and/or formatted.

isort can fix these issues automatically when you run `isort .` in your project.

#### Details — Bandit reports no issues with this project — ❌

Bandit reported **2** issues with your project:

- `tests/test_integration.py:52` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.5/plugins/b101_assert_used.html)
- `tests/test_integration.py:53` - _(B101, severity: LOW, confidence: HIGH)_ - Use of assert detected. The enclosed code will be removed when compiling to optimised byte code. [More Info](https://bandit.readthedocs.io/en/1.7.5/plugins/b101_assert_used.html)


### Testing (`testing`) — **83.2**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project has automated tests | `testing/has-tests`
✅ | 100.0% | 1 | Project passes all of its automated tests | `testing/pass`
❌ | 32.7% | 1 | Project provides a test coverage report | `testing/coverage`
✅ | 100.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **83.2**% | | Testing | `testing`

#### Details — Project has automated tests — ✅

Great! Your project contains **3** test files, which meets the minimum of **1** test files required.

This equates to **27.272727%** of Python files in your project being tests, which meets the target ratio of **20%**

#### Details — Project passes all of its automated tests — ✅

Congratulations, all **6** tests in your project passed!

#### Details — Project provides a test coverage report — ❌

Your project's tests achieved **26.1%** line test coverage, but **80.0%** is the target amount of test coverage to beat. You'll need to further improve your tests.

### Continuous Integration (`ci`) — **100.0**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project uses Continuous Integration (CI) | `ci/use`
 | _Total_ | | | 
✅ | **100.0**% | | Continuous Integration | `ci`

