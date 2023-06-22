# Live Coding on airdrag

## legend:

- root-level: section-title
- indented-level: one of advice, note, comment
  - advice: yellow-StickIt + bottom-right
  - comment: red-cloud + top-right
  - note: blue-cloud + center

§

## Contents

- 00:30: **(1)** IDE: install LiveShare plugin
  - 01:02: IDE: LiveShare not FOSS
  - 03:50: @@@ IDE: LiveShare installed
  - 04:05: act: navigate code with regexes
    - 04:32: ...advice: regexes are nice
  - 04:53: ...advice(IDE): vscode has ScreenCast mode
  - 05:58: act: Typing-hints for args
    - 06:10: ...advice(code): fix styling & LoCs widths with black formatter
    - 06:36: ...comment(IDE): "where am i?  i need bookmarks in the code!"
- 07:13: **(2)** @@@ prepare styling & sort & fix (missing) imports
    - 07:34: @@@ ...note(IDE): numba is missing from `setup.cfg` dependencies
    - 07:52: @@@ ...[numba+numpy advice](https://numba.pydata.org/numba-doc/dev/reference/numpysupported.html)
  - 08:49: @@@ IDE: google how to organize imports redproducibly (across IDEs)
    - 09:19: @@@ ... comment(IDE): no googling failed!
      [were supposed to organize imports with [a pipy library](https://12ft.io/proxy?&q=https%3A%2F%2Flevelup.gitconnected.com%2Fuse-isort-to-sort-your-python-module-imports-automatically-40918f3e2a8b), eg `isort`, we better agree on [some `isort` alternative](https://www.libhunt.com/r/isort) as a team)
        NOTE: ensure [`isort` works compatibly with `black`](https://blog.osull.com/2022/03/02/python-vs-code-make-black-and-organize-imports-work-together-on-save/)
  - 09:22: @@@ IDE: auto-formatting on save
    - 09:33: ...advice(IDE): black+auto-save (with git-hooks as alternative)
    - 09:54: @@@ ...comment(IDE): auto-organize imports will be added later (when??)
    - 10:01: @@@ ...advice(IDE): do'nt place choice that modify the code in User-settings
    - 10:17: ...advice(IDE): time spend on customizing your preferences is time spent wise
  - 11:20: Bookmarks plugin & IDEs commands
    - 11:51: ...advice(IDE): VSCode + PyChar command pallet shortcuts
  - 13:57: commit(1): Style(black) & unused imports
    - 14:12: @@@ draft 1st commit msg
  - 15:03: IDE "Zen" mode (configs)
    - 15:15: ...note(IDE): Zen mode shortcut
    - 15:30: Config VSCode Zen mode visible UI elements
    - 16:15: @@@ ...comment(IDE) tooling is important
    - 16:38: ...advice(IDE): VSCode + PyChar command pallet shortcuts (REPEATED)
- 16:50: **(§3)** Start Vectorizing outer loop
  - 18:20: commit(2): vectorize outer loop
- 18:58: **(§4)** Demeter Law for testable APIs
  - 19:21: note(git) ...announce reshufling of vectorization commit after TC.
  - 24:15: @@@ ...note(git): if future unit-test were to discover any bug....
    the fix would be squashed with this commit.
  - 24:22: commit(3): Demeter's Law
  - 24:48: advice(git): commit message widths
- 26:01: **(§5)** Start PyTesting
  - 26:38: setup.cfg testing dependencies
  - 27:05: @@@ fixture: dumy dataframe as input
  - 27:11: ...advice(test): fixtures are good
  - 28:41: ...comment(test): Perlin noise (not Sobol Sequences)
  - 29:04: @@@ Search for df columns
  - 31:14: CONNECTION BROKEN
  - 32:21: advice(test): unit-tests must not contain more data
  - 33:30: @@@ pytest dirs layout
    - 33:30: advice(test): google for pytest-layout+goodpractices
    - 34:02: @@@ delibarate on how to split unit-tests in test-files
    - 35:44: ... note(test): test-files splitting not yet decided
  - 36:03: @@@ creating the unit-test function
  - 36:28: @@@ Yes! (reply to Thoma's Q about how a fixture works)
  - 37:31: @@@ decide the number of dummy rows as a power of 2
  - 38:28: @@@ IDE: evaluate code interactively with [Shift+Enter]
  - 39:36: comment(build): explain `scipy` lib originates from my OS's Python from
  - 40:00: Morph input data
    - 40:49: @@@ ...note(IDE): most of the actions in this session heppen with the keyboard
    - 42:08: @@@ ...note(IDE): plotting diagrams in the interactive panel
    - 43:06: comment(test): Sobols were an accident, it was Perlin Noise that i had in mind
  - 45:47: advice(code): temp variables aliases are ok
  - 46:13: Extract dummy df creation in a utility function (vs fixtures)
  - 48:02: note(IDE) ...a CoPilot intervention
  - 49:17: @@@ advice(test): ...`configtest.py` with [this SO](https://stackoverflow.com/a/34520971/548792)
  - 49:38: @@@ comment/advice(test): ... apologies, utility functions need own files,
    (not `configtest.py`), meaning you need convert tests dir to a package with `tests/__init__.py`
  - 52:15: @@@ note(python): google: python+dunder+methods - but Python has no accessibility modifiers
  - 52:20: pytest configs
    - 53:06: @@@ advice(build): python projects have many ways to cofigure:
      config files: pyproject.toml, setup.cfg, setup.py(deprecated),
      other [build libraries](https://packaging.python.org/en/latest/key_projects/#build)
      poetry, flit, hatch, build, ...
    - 54:02: attempt for doctesting modules (and what is it?)
      - 54:09: @@@ comment(test): ...spoiler: we will fail to doctest...
        due to many pre-existing errors
      - 54:43: @@@ advice(test): doctest mixes documentation with unit-testing,
        which if checked regularly, serves as an API call example code.
- 57:50: **(§6)** fix module import errors
  - 58:28: advice(test): a new Python interpeter facilitates debugging import errors
  - 1:00:27: @@@ advice(imports) 3 different import syntaxes:
    - import a_package.a_module as foo
    - from a_package import a_module [as foo]
    - from a_package.a_module import a_function [as bar]
  - 1:00:45: debugging & recreattting my problematic venv
  - 1:03:37: advice(IDE) mismatches between selected-interpeter vs terminal is the root of many problems
  - 1:03:55: @@@ Discovered `tqdm` unused package in imports
  - 1:04:22: @@@ git-knit(1) fixup unused-import fix into style-commit
    - 1:04:55: comment(git) big mistake mixing style & refactorings
  - 1:06:11: @@@ git-knit(2) reword style-commit msg about BUG
  - 1:06:24: @@@ advice(git) annotate commits that are known to contain a bug
    either by rewritting the commit msg
    or with git-notes
  - 1:07:48: relative imports
    - 1:08:31: advice(imports) import conventions for readability
    - 1:10:24: comment(imports) stuttered bc of a more succicnt import syntax
  - 1:10:42: commit(4) fix relative commits
    - 1:10:46: @@@ comment(git,IDE) Selecting changed code and with a shortcut...i staged the changes for the next commit
    - 1:11:20: comment(git) hounored sepration of commits this time...
    - 1:11:29: @@@ advice(git, IDE) Change your code feeely and before committing,
      preview changes and SELECTIVELY stage related ones in separate commits.
    - 1:12:30: @@@ note(git) notice how much time is spent on commit msg...that's ok, it's investment when programming in time
  - 1:12:40: Wandered studing rel-imports
    - 1:12:52: comment(imports) ...waste a bit of time studying about rel-imports
  - 1:14:35: advice(code) keep side notes
  - 1:15:0: @@ git-knit(3): push package-fix earlier
    - 1:15:50: @@@ note(git) git rebase explanation
  - 1:16:20: @@@ commit(5) WIP PyTest
    - 1:16:26: @@@ advice(git) Instead of git-stash, a more verbose way is to commit a WIP-commit and git reset @~ )parent) later
    - 1:17:13: @@@ comment(imports) checking my modules once more with a pristine Python interpreter...
    - 1:17:27: comment(IDE) Exited my shared-terminal by habit....
    - 1:18:39: comment(IDE) Recreated my shared-terminal.
    - 1:19:13: git aliases for bash
    - 1:20:23: note: bookmarks & terminal misshups
    - 1:20:40: explain git-reset
- 1:22:11: **(§7)** Pytest part-2: seatbelt construction
  - 1:25:32: @@@ advice(code) always use `pathlib` for path manipulations
  - 1:26:38: Auto-organize imports on VSCode
  - 1:29:40: @@@ Recommence pytest
  - 1:30:07: code: pathlib manipulations
    - 1:29:40: advice(code) pathlib manipulations
  - 1:30:58: advice(data) accuracy-preserving file formats
  - 1:33:29: advice(data) union-typing supported by Python3.10
  - 1:35:42: advice(data) prefer defaults are false, OR stick to your convention
  - 1:41:00: Post-mortem debugging with pytest
  - 1:45:20: commit(6): seatbelt commit
- 1:47:15: **(§8)** @@ git-knit(2) fixup style changes & rewrite
  - 1:50:00: @@ git-knit(4) resolve conflicts while reshuffling
    - 1:50:45: Demeter Law, 2nd take
    - 1:52:02: advice(git) program in time needs disciplined commits
  - 1:53:03: reshuffle: preparing 1st conflict-resolved commit
    - 1:54:58: note(IDE) Ctrl+D to multi-select
    - 1:54:58: advice(git) tip: read the git-rebase prompt at the terminal to understand which changes needs to go
  - 1:59:57: reshuffle: preparing 2nd conflict-resolved commit
  - 2:02:56: Programming in time
- 2:05:27: **(§9)** @@ Chapter:Seatbelt finds vectorization BUG
  - 2:09:36: @@ git-knit(5): fixup timings into TC commit
  - 2:10:29: Study Vectorization BUG with git-diff
  - 2:12:33: LiveShare woes when git diffing
  - 2:15:00: Research vectorization bug (after resolving LiveShare woes)
  - 2:16:50: Draw internal loop
  - 2:18:40: Explain broadcasting for vectorization bug
  - 2:21:10: Resolved  vectorization bug
  ..."with many eyballs, all bug are shallow"
  - 2:23:28: Thomas asks for proof bug is solved
  - 2:24:48: x200 faster!
  - 2:25:40: ...3k rows is NOT 1 hour but 10 hours/1Hz or 1H/10Hz
  - 2:26:30: Ask +10min to extend the live-coding session
    ...but actually it took another +25min for the sesion to end!
  - 2:27.31: ...insist on 1h-->36κ rows!!!
  - 2:29:20: ...TC generates 2^15--32k rows, not 2^14
- 2:30:20: **(§10)** REFACT common code in temporary variables
  - 2:31:12: Auto-save enabled by user-prefs
  - 2:31:49: Continue REFACT extracting temp-vars (inner loop `heights_ratio`)
  - 2:33:10: Continue REFACT extracting temp-vars (v-veh in kmh)
  - 2:34:20: Continue REFACT extracting temp-vars (rel_wind)
  - 2:35:25: Continue REFACT linearity simplification
  - 2:36:48: ...must leave a comment explaining this original formulas!!
  - 2:37:36: ...f@ck!
  - 2:38:28: ...Readability not Speed
  - 2:39:15: Continue REFACT radians
  - 2:40:20: ...+BUG in Radians!!
  - 2:40:24: Continue REFACT reusing new series without indexing dataframes
  - 2:42:10: Radians-per-degrees saga!
    - 2:43:01: REALIZED there is a BUG
    - 2:45:51: RESOLVED the BUG it was the inverse radians-per-degrees
  - 2:46:41: ...TCs must be instant, to TC on every keystroke
  - 2:47:15: Redo REFACTs new series in tmp var (lost when searching bug)
  - 2:47:50: FINISHED REFACT temp-vars, fast, readable & tested code.
  - 2:48:32: FINAL tmp-vars commit (same speed)
- 2:49:32: **(§11)** PUSH to pub repo (through an intermediate local)
  - 2:50:04: ...mean repo
  - 2:51:39: END


## TODO

- 11:16 mention where copilot appear in the time-in-video
- 11:20: compress bookmarks plugin installation
- 1:50:00, 2:05:25: repetition of "resolve-conflic" title

## OpenShot Profile for MSTeams

description=MSTeams 16fps HD 1080p (1920x1080)
frame_rate_num=16
frame_rate_den=1
width=1920
height=1080
progressive=1
sample_aspect_num=1
sample_aspect_den=1
display_aspect_num=16
display_aspect_den=9

This reshuffling situation explains perfectly well
why we try so hard to keep git history "clean"
and how this intermingles with
testability & modularity (low coupling)
