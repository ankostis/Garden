# Git stuff

- ["Saucage making" rules](http://sethrobertson.github.io/GitBestPractices/#sausage), discovered from ...
- this y-combinator post: ["Why is git pull considered harmful? (2013)"](https://news.ycombinator.com/item?id=7385087)
- [triangular workflow](https://www.git-scm.com/docs/gitrevisions#Documentation/gitrevisions.txt-emltbranchnamegtpushemegemmasterpushemempushem)
  uprtream RTB differs from default push target
- [Recovering from a rebase upstream](https://git-scm.com/docs/git-rebase#_recovering_from_upstream_rebase)
- [commit-message guidelines](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project)
- Martin Fowler's git book
- *git.git* Gitworkflows:
  - [man page](https://git-scm.com/docs/gitworkflows)
  - [mailling-list](https://github.com/git/git/blob/master/Documentation/howto/maintain-git.txt)
- dotnet versioning from git *tags*:
  - [blog with some links to plugins (2018)](https://medium.com/@michael.wolfenden/simplified-versioning-and-publishing-for-net-libraries-a28e5e740fa6) such as ...
  ["semantic release" JS project](https://github.com/semantic-release/semantic-release)
    - this [auto-versioning plugin](https://github.com/GitTools/GitVersion)
      - with its versioning explained in
        [this blog](https://www.xavierdecoster.com/post/2013/04/29/semantic-versioning-auto-incremented-nuget-package-versions.html)
  - but [this plugin](https://github.com/TurnerSoftware/BuildVersioning#Version-Strings)
    manually sets all 3 assembly versions
- NuGet:
  - [NuGet vs Semantic versioning (2021)](https://learn.microsoft.com/en-us/nuget/create-packages/prerelease-packages)
  - [MS NuGet recommendations (2013)](https://learn.microsoft.com/en-us/archive/msdn-magazine/2012/november/nuget-top-10-nuget-anti-patterns)
  - [*SemVer* support in *NuGet* >= 4.3(Aug 2017)](https://devblogs.microsoft.com/nuget/whats-nu-in-nuget-with-visual-studio-2017-version-15-3/)
  - [NuGet vs SemVer](https://learn.microsoft.com/en-us/nuget/concepts/package-versioning#where-nugetversion-diverges-from-semantic-versioning)
  - [4-part versions deprecated in NuGet](https://blog.inedo.com/nuget/package-versioning/#:~:text=Although%204%2Dpart%20numbers%20are%20supported%2C%20Microsoft%20no%20longer%20recommends%20this%20format.)
- [Versioning blog in MS not mentioning Build-number at all (Aug 2023)](https://learn.microsoft.com/en-us/dotnet/csharp/versioning)
- [Versioning blog in MS recomending SemVer for NuGet (Sep 2021))](https://learn.microsoft.com/en-us/dotnet/csharp/versioning)
- [DevOps deducing SemVer from git commit headers](https://medium.com/agoda-engineering/automating-versioning-and-releases-using-semantic-release-d16c5672fbe1)
  based on "semantic release" plugin.

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
