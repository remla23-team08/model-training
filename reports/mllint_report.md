# ML Project Report
**Project** | **Details**
--------|--------
Date    | Thu, 08 Jun 2023 23:37:26 +0200 
Path    | `/home/amoraru/Documents/MSc/Q4/REMLA/model-training`
Config  | `pyproject.toml`
Default | No
Git: Remote URL | `git@github.com:remla23-team08/model-training.git`
Git: Commit     | `91ed538432de0e9248fdb9d974eadae2a339fedd`
Git: Branch     | `feature/improve-code-quality`
Git: Dirty Workspace?  | Yes
Number of Python files | 9
Lines of Python code   | 209

---

## Config

**Note** — The following rules were disabled in `mllint`'s configuration:
- `dependency-management/single`

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
✅ | 100.0% | 1 | Project places its development dependencies in dev-dependencies | `dependency-management/use-dev`
 | _Total_ | | | 
❌ | **66.7**% | | Dependency Management | `dependency-management`

### Code Quality (`code-quality`) — **76.5**%

Passed | Score | Weight | Rule | Slug
:-----:|------:|-------:|------|-----
❌ | 60.0% | 1 | Project should use code quality linters | `code-quality/use-linters`
❌ | 80.0% | 1 | All code quality linters should be installed in the current environment | `code-quality/linters-installed`
❌ | 95.2% | 1 | Pylint reports no issues with this project | `code-quality/pylint/no-issues`
✅ | 100.0% | 1 | Pylint is configured for this project | `code-quality/pylint/is-configured`
❌ | 0.0% | 1 | Mypy reports no issues with this project | `code-quality/mypy/no-issues`
✅ | 100.0% | 1 | Black reports no issues with this project | `code-quality/black/no-issues`
✅ | 100.0% | 1 | isort reports no issues with this project | `code-quality/isort/no-issues`
✅ | 100.0% | 0 | isort is properly configured | `code-quality/isort/is-configured`
 | _Total_ | | | 
❌ | **76.5**% | | Code Quality | `code-quality`

#### Details — Project should use code quality linters — ❌

Linters detected:

- Black
- isort
- Pylint


However, these linters were **missing** from your project:

- Mypy
- Bandit


We recommend that you start using these linters in your project to help you measure and maintain the quality of your code.

This rule will be satisfied, iff for each of these linters:
- **Either** there is a configuration file for this linter in the project
- **Or** the linter is a dependency of the project

Specifically, we recommend adding each linter to the development dependencies of your dependency manager,
e.g. using `poetry add --dev mypy` or `pipenv install --dev mypy`


#### Details — All code quality linters should be installed in the current environment — ❌

The following linters were not installed, so we could not analyse what they had to say about your project:

- Bandit


#### Details — Pylint reports no issues with this project — ❌

Pylint reported **1** issues with your project:

- `tests/test_MLdevel.py:20,35` - _(W0621)_ Redefining name 'trained_model' from outer scope (line 14)


#### Details — Mypy reports no issues with this project — ❌

Mypy reported **179** issues with your project:

- `setup.py:5,1` - Error: Skipping analyzing "setuptools": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_expected_degree_sequence.py:9,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:85,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:91,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:98,5` - Error: Need type annotation for "dlist" (hint: "dlist: List[<type>] = ...")  [var-annotated]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:107,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:109,13` - Error: Call to untyped function "digitsrep" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:116,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:122,21` - Error: Call to untyped function "powersum" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:126,25` - Error: Call to untyped function "powersum" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:130,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:136,17` - Error: Call to untyped function "powersum" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:140,21` - Error: Call to untyped function "powersum" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:148,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:149,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:150,16` - Error: Call to untyped function "powersum" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:152,12` - Error: Call to untyped function "discrete_dynamics_digraph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:155,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:156,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:157,16` - Error: Call to untyped function "powersum" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:159,12` - Error: Call to untyped function "discrete_dynamics_digraph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:162,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:163,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:164,16` - Error: Call to untyped function "powersum" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:166,12` - Error: Call to untyped function "discrete_dynamics_digraph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:169,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:187,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:188,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:194,12` - Error: Call to untyped function "discrete_dynamics_digraph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:197,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:206,5` - Error: Call to untyped function "cubing_153_digraph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_iterated_dynamical_systems.py:210,7` - Error: Call to untyped function "fixed_points" in typed context  [no-untyped-call]
- `src/pipeline/util.py:10,2` - Error: "staticmethod" used with a non-method  [misc]
- `src/pipeline/util.py:11,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `venv/bin/find_spark_home.py:28,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `venv/bin/find_spark_home.py:34,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/bin/find_spark_home.py:57,43` - Error: Item "None" of "Optional[ModuleSpec]" has no attribute "origin"  [union-attr]
- `venv/bin/find_spark_home.py:57,43` - Error: Argument 1 to "dirname" has incompatible type "Union[str, None, Any]"; expected "PathLike[Any]"  [arg-type]
- `venv/bin/find_spark_home.py:69,47` - Error: Call to untyped function "is_spark_home" in typed context  [no-untyped-call]
- `venv/bin/find_spark_home.py:88,11` - Error: Call to untyped function "_find_spark_home" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/graph/plot_morse_trie.py:11,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_morse_trie.py:83,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/graph/plot_morse_trie.py:87,16` - Error: Call to untyped function "morse_encode" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/graph/plot_morse_trie.py:95,12` - Error: Call to untyped function "morse_encode" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/graph/plot_morse_trie.py:97,17` - Error: Call to untyped function "morse_encode" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_center_node.py:11,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/3d_drawing/mayavi2_spring.py:8,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/3d_drawing/mayavi2_spring.py:10,1` - Error: Cannot find implementation or library stub for module named "mayavi"  [import]
- `src/pipeline/load_data.py:12,1` - Error: Cannot find implementation or library stub for module named "Util"  [import]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:14,18` - Error: Class cannot subclass "Graph" (has type "Any")  [misc]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:21,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:30,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:34,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:36,13` - Error: Call to untyped function "add_node" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:38,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:42,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:44,13` - Error: Call to untyped function "remove_node" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:46,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:50,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:53,13` - Error: Call to untyped function "add_edge" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:55,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:59,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:62,13` - Error: Call to untyped function "remove_edge" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:64,5` - Error: Function is missing a return type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:64,5` - Note: Use "-> None" if function does not return a value
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:69,5` - Error: Call to untyped function "PrintGraph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:70,1` - Error: Call to untyped function "add_node" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:71,1` - Error: Call to untyped function "add_nodes_from" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:72,1` - Error: Call to untyped function "remove_node" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:73,1` - Error: Call to untyped function "remove_nodes_from" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:75,1` - Error: Call to untyped function "add_edge" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:77,1` - Error: Call to untyped function "remove_edge" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:78,1` - Error: Call to untyped function "add_edges_from" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:80,1` - Error: Call to untyped function "remove_edges_from" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_printgraph.py:83,5` - Error: Call to untyped function "PrintGraph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:19,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:23,17` - Error: Class cannot subclass "Graph" (has type "Any")  [misc]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:38,5` - Error: Function is missing a return type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:43,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:61,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:71,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:140,5` - Error: Function is missing a return type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:184,30` - Error: Call to untyped function "degree" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:185,63` - Error: Call to untyped function "degree" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:187,30` - Error: Call to untyped function "degree" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/subclass/plot_antigraph.py:188,68` - Error: Call to untyped function "degree" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:23,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:26,1` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:30,5` - Error: Function is missing a type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:40,21` - Error: Call to untyped function "edit_distance_one" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:49,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:54,16` - Error: Incompatible types in assignment (expression has type "str", variable has type "bytes")  [assignment]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:55,28` - Error: Argument 1 to "startswith" of "bytes" has incompatible type "str"; expected "Union[bytes, Tuple[bytes, ...]]"  [arg-type]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:59,12` - Error: Call to untyped function "generate_graph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/graph/plot_words.py:62,5` - Error: Call to untyped function "words_graph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/graph/plot_triad_types.py:14,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_triad_types.py:37,47` - Error: "List[List[Axes]]" has no attribute "flatten"  [attr-defined]
- `venv/share/doc/networkx-3.1/examples/graph/plot_roget.py:28,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_roget.py:31,1` - Error: Function is missing a return type annotation  [no-untyped-def]
- `venv/share/doc/networkx-3.1/examples/graph/plot_roget.py:41,16` - Error: Incompatible types in assignment (expression has type "str", variable has type "bytes")  [assignment]
- `venv/share/doc/networkx-3.1/examples/graph/plot_roget.py:42,28` - Error: Argument 1 to "startswith" of "bytes" has incompatible type "str"; expected "Union[bytes, Tuple[bytes, ...]]"  [arg-type]
- `venv/share/doc/networkx-3.1/examples/graph/plot_roget.py:44,28` - Error: Argument 1 to "startswith" of "bytes" has incompatible type "str"; expected "Union[bytes, Tuple[bytes, ...]]"  [arg-type]
- `venv/share/doc/networkx-3.1/examples/graph/plot_roget.py:45,20` - Error: Cannot determine type of "oldline"  [has-type]
- `venv/share/doc/networkx-3.1/examples/graph/plot_roget.py:46,47` - Note: (Skipping most remaining errors due to unresolved imports or missing stubs; fix these first)
- `venv/share/doc/networkx-3.1/examples/graph/plot_roget.py:66,5` - Error: Call to untyped function "roget_graph" in typed context  [no-untyped-call]
- `venv/share/doc/networkx-3.1/examples/graph/plot_napoleon_russian_campaign.py:11,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_mst.py:14,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_karate_club.py:17,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_football.py:20,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_erdos_renyi.py:15,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_degree_sequence.py:9,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/graph/plot_dag_layout.py:11,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_weighted_graph.py:9,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_unix_email.py:24,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_tsp.py:14,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_tsp.py:15,1` - Error: Skipping analyzing "networkx.algorithms.approximation": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_tsp.py:15,1` - Error: Skipping analyzing "networkx.algorithms": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_spectral_grid.py:25,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_simple_path.py:9,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_selfloops.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_sampson.py:19,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_random_geometric_graph.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_rainbow_coloring.py:21,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_node_colormap.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_multipartite_graph.py:9,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_labels_and_colors.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_knuth_miles.py:31,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_knuth_miles.py:94,1` - Error: Cannot find implementation or library stub for module named "cartopy.crs"  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_knuth_miles.py:94,1` - Error: Cannot find implementation or library stub for module named "cartopy"  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_knuth_miles.py:95,1` - Error: Cannot find implementation or library stub for module named "cartopy.io.shapereader"  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_knuth_miles.py:95,1` - Error: Cannot find implementation or library stub for module named "cartopy.io"  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_house_with_colors.py:9,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_four_grids.py:13,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_eigenvalues.py:9,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_ego_graph.py:13,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_edge_colormap.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_directed.py:13,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_degree.py:16,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_custom_node_icons.py:12,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_custom_node_icons.py:13,1` - Error: Cannot find implementation or library stub for module named "PIL"  [import]
- `venv/share/doc/networkx-3.1/examples/drawing/plot_chess_masters.py:29,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/basic/plot_simple_graph.py:9,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/basic/plot_read_write.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/basic/plot_properties.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_subgraphs.py:12,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_snap.py:14,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_rcm.py:14,1` - Error: Cannot find implementation or library stub for module named "seaborn"  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_rcm.py:15,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_parallel_betweenness.py:24,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_maximum_independent_set.py:13,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_maximum_independent_set.py:14,1` - Error: Skipping analyzing "networkx.algorithms": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_krackhardt_centrality.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_girvan_newman.py:14,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_dedensification.py:11,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_davis_club.py:16,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_davis_club.py:17,1` - Error: Skipping analyzing "networkx.algorithms": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_circuits.py:16,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_blockmodel.py:27,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_blockmodel.py:29,1` - Error: Skipping analyzing "scipy.cluster": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_blockmodel.py:30,1` - Error: Skipping analyzing "scipy.spatial": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_betweenness_centrality.py:13,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/algorithms/plot_beam_search.py:14,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/3d_drawing/plot_basic.py:10,1` - Error: Skipping analyzing "networkx": module is installed, but missing library stubs or py.typed marker  [import]
- `venv/share/doc/networkx-3.1/examples/3d_drawing/plot_basic.py:13,1` - Error: Cannot find implementation or library stub for module named "mpl_toolkits.mplot3d"  [import]
- `src/pipeline/training.py:9,1` - Error: Skipping analyzing "joblib": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/training.py:11,1` - Error: Skipping analyzing "sklearn.feature_extraction.text": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/training.py:12,1` - Error: Skipping analyzing "sklearn.model_selection": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/training.py:13,1` - Error: Skipping analyzing "sklearn.naive_bayes": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/preprocessing.py:11,1` - Error: Skipping analyzing "joblib": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/preprocessing.py:12,1` - Error: Skipping analyzing "nltk": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/preprocessing.py:14,1` - Error: Skipping analyzing "nltk.corpus": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/preprocessing.py:15,1` - Error: Skipping analyzing "nltk.stem.porter": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/preprocessing.py:16,1` - Error: Cannot find implementation or library stub for module named "Util"  [import]
- `src/pipeline/evaluation.py:11,1` - Error: Skipping analyzing "joblib": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/evaluation.py:11,1` - Note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
- `src/pipeline/evaluation.py:13,1` - Error: Skipping analyzing "sklearn.metrics": module is installed, but missing library stubs or py.typed marker  [import]
- `src/pipeline/evaluation.py:14,1` - Error: Skipping analyzing "sklearn.model_selection": module is installed, but missing library stubs or py.typed marker  [import]
- `tests/test_MLdevel.py:7,1` - Error: Skipping analyzing "joblib": module is installed, but missing library stubs or py.typed marker  [import]


#### Details — Black reports no issues with this project — ✅

Congratulations, Black is happy with your project!

#### Details — isort reports no issues with this project — ✅

Congratulations, `isort` is happy with your project!

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

