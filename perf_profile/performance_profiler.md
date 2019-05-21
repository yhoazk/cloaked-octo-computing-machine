# Profile

CPython std distribution come with three profilers:

* `cProfile`: C module based on `lsprof`
* `Profile`: pure python profiler
* `hotshot`: Can be seen as a subset of `cProfile`

## Yappi

Example to profile a python application using [`yappi`](https://github.com/sumerc/yappi).

The main difference between the last profilers is that all of them lack of
support for multi-threading and cpu time

call yappi from command line:
```sh
python3 -m yappi -o profile.cprof script.py
```