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

Profile a function:

```python
import yappi

def a():
    for _ in range(1000000): pass

yappi.start()
a()
yappi.get_func_stats().print_all()
yappi-get_thread_stats().print_all()
```

## [Py-spy](https://github.com/benfred/py-)

Py-spy is a sampling profiler, this means that there is no need to restart the
program or to modify the code. py-spy is written in rust for speed and does not
run on the same process as the profiled program, this means that is safe to use
against production code.

### install 
```
pip install --user py-spy
```

Or with cargo:

```
cargo install py-spy
```

### use

```
py-spy --pid 231
```
or 

```
py-spy -- python script.py
```
It's also possible to create flamegraphs by adding the parameter `--flame out.svg`