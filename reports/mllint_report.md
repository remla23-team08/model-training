# ML Project Report
**Project** | **Details**
--------|--------
Date    | Wed, 21 Jun 2023 14:07:31 +0200 
Path    | `/home/jvandersaag/Documents/REMLA/project/model-training`
Config  | `.mllint.yml`
Default | Yes
Git: Remote URL | `https://github.com/remla23-team08/model-training.git`
Git: Commit     | `35e4660ad85087229f7eb187eaeb8f52b5028f25`
Git: Branch     | `pytest`
Git: Dirty Workspace?  | Yes
Number of Python files | 8
Lines of Python code   | 208

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

### Code Quality (`code-quality`) — **87.5**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
✅ | 100.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
✅ | 100.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
✅ | 100.0% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
✅ | 100.0% | 1 | Bandit reports no issues with this project | `code-quality/bandit/no-issues`
 | _Total_ | | | 
❌ | **87.5**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ✅

Hooray, all linters detected:

- Mypy
- Black
- isort
- Bandit
- Pylint


#### Details — Pylint reports no issues with this project — ✅

Congratulations, Pylint is happy with your project!

#### Details — Mypy reports no issues with this project — ❌

Mypy reported **44** issues with your project:

- `src/util.py:10,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/load_data.py:12,1` - Error: Library stubs not installed for "requests" (or incompatible with Python 3.8)  [import]
- `src/load_data.py:12,1` - Note: Hint: "python3 -m pip install types-requests"
- `src/load_data.py:12,1` - Note: (or run "mypy --install-types" to install all missing stub packages)
- `src/load_data.py:12,1` - Note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
- `src/load_data.py:14,1` - Error: Cannot find implementation or library stub for module named "util"  [import]
- `src/load_data.py:37,10` - Error: Incompatible types in assignment (expression has type "ZipFile", variable has type "_TemporaryFileWrapper[bytes]")  [assignment]
- `src/training.py:15,1` - Error: Cannot find implementation or library stub for module named "util"  [import]
- `src/training.py:24,15` - Error: No overload variant of "__getitem__" of "DataFrame" matches argument type "slice"  [call-overload]
- `src/training.py:24,15` - Note: Possible overload variants:
- `src/training.py:24,15` - Note: def __getitem__(self, str) -> Series[Any]
- `src/training.py:24,15` - Note: def __getitem__(self, Union[Series[Any], DataFrame, List[str], Index[str], ndarray[Any, Any]]) -> DataFrame
- `src/preprocessing.py:17,1` - Error: Cannot find implementation or library stub for module named "util"  [import]
- `src/preprocessing.py:23,5` - Error: Function is missing a return type annotation  [no-untyped-def]
- `src/preprocessing.py:23,5` - Note: Use "-> None" if function does not return a value
- `src/preprocessing.py:34,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/preprocessing.py:39,27` - Error: Call to untyped function "preprocess_review" in typed context  [no-untyped-call]
- `src/preprocessing.py:42,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/preprocessing.py:62,20` - Error: No overload variant of "__getitem__" of "DataFrame" matches argument type "slice"  [call-overload]
- `src/preprocessing.py:62,20` - Note: Possible overload variants:
- `src/preprocessing.py:62,20` - Note: def __getitem__(self, str) -> Series[Any]
- `src/preprocessing.py:62,20` - Note: def __getitem__(self, Union[Series[Any], DataFrame, List[str], Index[str], ndarray[Any, Any]]) -> DataFrame
- `src/preprocessing.py:69,24` - Error: Call to untyped function "Preprocessing" in typed context  [no-untyped-call]
- `src/preprocessing.py:70,19` - Error: Call to untyped function "preprocess_dataset" in typed context  [no-untyped-call]
- `src/evaluation.py:17,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `src/evaluation.py:54,15` - Error: No overload variant of "__getitem__" of "DataFrame" matches argument type "slice"  [call-overload]
- `src/evaluation.py:54,15` - Note: Possible overload variants:
- `src/evaluation.py:54,15` - Note: def __getitem__(self, str) -> Series[Any]
- `src/evaluation.py:54,15` - Note: def __getitem__(self, Union[Series[Any], DataFrame, List[str], Index[str], ndarray[Any, Any]]) -> DataFrame
- `src/evaluation.py:77,5` - Error: Call to untyped function "model_eval" in typed context  [no-untyped-call]
- `tests/test_MLdevel.py:19,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `tests/test_MLdevel.py:25,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `tests/test_MLdevel.py:28,31` - Error: Call to untyped function "get_paths" in typed context  [no-untyped-call]
- `tests/test_MLdevel.py:32,15` - Error: No overload variant of "__getitem__" of "DataFrame" matches argument type "slice"  [call-overload]
- `tests/test_MLdevel.py:32,15` - Note: Possible overload variants:
- `tests/test_MLdevel.py:32,15` - Note: def __getitem__(self, str) -> Series[Any]
- `tests/test_MLdevel.py:32,15` - Note: def __getitem__(self, Union[Series[Any], DataFrame, List[str], Index[str], ndarray[Any, Any]]) -> DataFrame
- `tests/test_MLdevel.py:36,15` - Error: No overload variant of "__getitem__" of "DataFrame" matches argument type "slice"  [call-overload]
- `tests/test_MLdevel.py:36,15` - Note: Possible overload variants:
- `tests/test_MLdevel.py:36,15` - Note: def __getitem__(self, str) -> Series[Any]
- `tests/test_MLdevel.py:36,15` - Note: def __getitem__(self, Union[Series[Any], DataFrame, List[str], Index[str], ndarray[Any, Any]]) -> DataFrame
- `tests/test_MLdevel.py:55,29` - Error: Call to untyped function "model_eval" in typed context  [no-untyped-call]
- `tests/test_MLdevel.py:59,24` - Error: Call to untyped function "model_eval" in typed context  [no-untyped-call]
- `tests/test_MLdevel.py:69,5` - Error: Call to untyped function "test_nondeterminism_robustness" in typed context  [no-untyped-call]


#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

#### Details — Bandit reports no issues with this project — ✅

Congratulations, Bandit is happy with your project!

### Testing (`testing`) — **40.6**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 62.5% | 1 | Project has automated tests | `testing/has-tests`
❌ | 0.0% | 1 | Project passes all of its automated tests | `testing/pass`
❌ | 0.0% | 1 | Project provides a test coverage report | `testing/coverage`
✅ | 100.0% | 1 | Tests should be placed in the tests folder | `testing/tests-folder`
 | _Total_ | | | 
❌ | **40.6**% | | Testing | `testing`

#### Details — Project has automated tests — ❌

There is **1** test file in your project, which meets the minimum of **1** test file required.

However, this only equates to **12.5%** of Python files in your project being tests, while `mllint` expects that **20%** of your project's Python files are tests.

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

