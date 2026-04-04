# nj67-server

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/garethlearnscoding/nj67-server/tree/testing)

H2 Computing Papers!!

This is the server for nj67, the client can be found [here](https://github.com/ffgtfgh53/nj67-client).

Requirements: Python >= 3.10 (Tested with 3.14 on Linux), no external dependencies

## Testcases

Testcases are not to be run using the file itself, rather to be run using unittest in testcases directory

E.g. to run all testcases: 

```
cd ./nj67-papers/testcases
python -m unittest -v
```
The testcases assume that the neccessary code is present in `taskfile_n` where n is the task number.

The code must also be wrapped in a function or class that the testcase can import and run.