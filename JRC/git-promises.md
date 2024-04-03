# Git Promises

## Version Bumps while Beta-testing

- Now i will talk about how the current Vecto release process
- deals with unforseen features & bugfixes.

- Let's assume that we plan to release version 4.0.0 - dates are not important here.
- We just have PROMISED that specific version-id.
- The development starts...
  - and after all foreseen features & bugfixes are in place,  ...
  - we publish a "Release Candidate" for our BETA testers.

  > COMMENT: publishing a "BETA"
  > is also similar

- While awaiting feedback from testers ...
- an UNFORSEEN feature gets merged,
  - for example, JRC propores VTP.

- The Q is: should the new *merge* affect the version-number?

> COMMENT: assuming no *code-freeze*
> enacted after RC...

- Based on the promise,... we should NOT!
  - Bumping the RC number is the only possibility.

- BUT we're now 2 development teams,
- *Semantic Versioning* facilitate communications.
- versionS 4.1.x would be much easier to remember
- that it is all these version that contain VTP.

- To conclude, it is the **promise** that prevent us fron using
  version IDs to their full potential.

## Faulty Releases

- I want to talk about the current Vecto release process, specifically, ...
  - how it deals with *faulty packages*.

- Let's assume that we're on May,  and
    - we plan to release version 3.15 on June.

> COMMENT: talking about 2-number versions for brevity

- That's a PROMISE for version 3.15 on a rough date.
- We implement the foreseen bugs & features,  ...
  - update all DOCUMENTS in the sources,
  - add the *Release Candidate* marker, ..
  - commit, and ...
  - publish the new "RC" to our BETA testers.

- Based on their feedback,
  - we do any final fixes,
  - edit ALL DOCS once more to remove the "RC" marker, AND ...
  - to mention it's now a release **Blessed for Certification**,
  - commit, release, and ...
  - this time, announce it, to ALL our Users.

- The working assumption HERE is that users reported back the release as BROKEN!

- What do we do?
- Certainly we need another release, but what version should that be?

- Same as before? ...version 3.15??
  - That would confuse BOTH the Users, and the Computers.

- For the Users, ...they need a significant digit bump on the version-string, ...
  - to discern the NEW 3.15 from the OLD one.
- That's what *Semantic Versioning* stands for.

> COMMENT:
> Vecto uses 4th element *build-day*
> incompatible with *SemVer* & NuGet

- For DevOps, both CI & NugGet need a different tag/version each time,

- If we bump it to 3.16 instead...
  - we now have to update ALL THE Documents,
  - to mark the previous 3.15 as Broken,  ...
  - "Bless" the 3.16, ...
  - and *commit* ...
  - something WHICH is equivalent to a NEW(!) PROMISE,
  - looping us back to the same tarpit we started from!.

- To conclude, it is the **promised version ids**, ...
- AND the *"blessing of releases"* within their own sources
- that burdens the release process.

## Solution

- The alternative is to let the version-ID to "float" freely & semantically...
- *Decoupled* from the certification "Blessing", ...
- like this:

- We promise version `4.x.x` at a rough date,
  - we **tag** the repo as `v4.0.0-alpha.0`
  - and start developing ...
  - if during development some features & bugfixes require beta-testing, ...
  - they are described *semantically* with bumps in the version-IDs, ...
  - which would be an important aid when deciding merge bases & targets.

> COMMENT: see another video for the brahching strategy.

- For example, we get here `4.0.0`, ...
- `4.0.0-alpha.1` and ...
- `4.1.0`,

- Documents in the sources are edited to describe just the changes of each intermediate release
  - **WITHOUT** the "RC" or "BETA" specifiers.
  - And that's important later, for the final release.
- The Version ID of the executable is derrived ONLY from the LATEST git TAG.
- Versions WITH or WITHOUT prerelease specifiers are allowed.


> COMMENT: requires a build plugin
> [such as](https://github.com/TurnerSoftware/BuildVersioning) or
> [alternatives](https://www.google.com/search?q=dotnet+build+plugin+version+from+git-tags)

- If Beta Testers prove a "Release Candidate" GOOD for Certification , ...
  -  a NEW **final** TAG is added on that commit, **in addition** to the "RC" one.
- The "blessed" release is specified EXCLUSIVELY in the Wiki release-table & codeu pages, ...
  - which are both editable post-factum (like tags).
