# Git stuff

- ["Saucage making" rules](http://sethrobertson.github.io/GitBestPractices/#sausage), discovered from ...
- this y-combinator post: ["Why is git pull considered harmful? (2013)"](https://news.ycombinator.com/item?id=7385087)
- [triangular workflow](https://www.git-scm.com/docs/gitrevisions#Documentation/gitrevisions.txt-emltbranchnamegtpushemegemmasterpushemempushem)
  uprtream RTB differs from default push target
- [Recovering from a rebase upstream](https://git-scm.com/docs/git-rebase#_recovering_from_upstream_rebase)

## terminology

Borrow images from [this SO](https://stackoverflow.com/a/49755270/548792).

- **remote:**
  - **repo(*):** a repo on a remote server, implied  term if not specified
  - **branch:** a branch in a remote repo
  - **tracking branch(rtb):** e.g. `origin/master`, stored in `.git/refs/remotes/origin/master`
- **tracking branch:** a local branch that is tracking a remote branch via some rtb
- **upstream:** often abused, usually means the remote repo OR branch you push/pull from/to
  - **repo:** git being distributed, there is no single upstream repo BUT conventionally
    the repo you cloned from the project is the upstream repo.
  - **branch:** the remote branch that the current branch is tracking
  - see [this SO](https://stackoverflow.com/questions/2739376/definition-of-downstream-and-upstream/6244487#6244487)
- **push target:** the remote branch that the current branch is pushing to
