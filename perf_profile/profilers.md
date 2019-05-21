# Profile Python


## Profiling with cProfile

To get  the top calls:

```
python -m cProfile -o report.prof my_pythonapp.py arg1 arg2
```

This generates the ouput file __report.prof__, to read this
archive

```py
import pstats
p = pstats.Stats("report.prof")
p.sort_stats("cumulative").print_stats(10)
```