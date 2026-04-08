# nj67-server

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/garethlearnscoding/nj67-server/tree/testing)

H2 Computing Papers!!

This is the server for nj67, the client can be found [here](https://github.com/ffgtfgh53/nj67-client).

## Requirements: 
Python >= 3.14 on UNIX

Dependencies: 
* flask >= 3.0 (and dependencies)
* (optional) jupyterlab/notebook for ipynb support (only to use the notebook yourself, not required for server)

Might possibly support:
* Python > 3.8
* Windows systems
* Other non-UNIX systems

No support for:
* Python <= 3.8 (no type annotations and no flask support, also ./securetest.py is broken in 3.8)

Mainly tested on Python 3.14 on Linux. <!--𝜋thon amirite-->

## Cloning

Since `nj67-papers` is a submodule, to fully clone this repo we need an additional flag `--recurse-submodules` to tell git to also clone the submodule repo.

The full command looks like this: 
```
git clone --recurse-submodules https://github.com/garethlearnscoding/nj67-server.git
```
Similarly, to pull any update you also need the `--recurse-submodules` flag, like this:
```
git pull --recurse-submodules
```
If you forgot the flag (either from `git clone` or `git pull`), simply run the following command from this project root to initialise and update all submodules.
```
git submodule update --init --recursive
```

If the command fails, there may be a possibility that the `.gitmodules` file was updated. To fix this, run the following command to syncrhonise the submodules with the server
```
git submodule sync
```
It is possible to add the `--recurse-submodules`  flag to `git pull` and `git clone` by default, read the [git submodule documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules) for more info. (TL;DR, run `git config submodule.recurse true`)

## Testcases

Testcases are not to be run using the file itself, rather to be run using unittest in testcases directory

E.g. to run all testcases: 

```
cd ./nj67-papers/testcases
python -m unittest -v
```
The testcases assume that the neccessary code is present in `taskfile_n` where n is the task number.

The code must also be wrapped in a function or class that the testcase can import and run.

### ATTENTION

While there is some minimal patching of user code (meaning no exec() and other functions), it DOES NOT apply to loose code at the cell level which when collected into a single file, WILL BE RUN when importing a function from the same file. I have yet to re-wrap the entire code cell in another function to prevent this loose code, so this warning (meant for me or whoever this may concern (also me)) will stay here until this is resolved

<!--
Honestly this README.md is here just so i don't forget
Documentation for me lmao
Documnting all this things i need to do lmao
-->