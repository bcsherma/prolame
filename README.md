# `prolame`
A logic programming language for reasoning about integers. The interperter is packaged as a single python script called `prolame`.

## Prerequisites
1. `Python 3+`
2. [`Ply`](http://www.dabeaz.com/ply/)
3. [`Pycosat`](https://github.com/ContinuumIO/pycosat)

Note that (2) and (3) are installed by default with the Anaconda distribution of Python.

## Running

Here is the usage message generated by `prolame` when the `-h` or `--help` arguments are given.

```
usage: prolame [-h] [--max MAX] program

prolame: A logic programming language for reasoning about natural numbers

positional arguments:
  program     prolame program to be run

optional arguments:
  -h, --help  show this help message and exit
  --max MAX   largest number to be considered
```

## Getting Started

Try running the programs in the `examples` directory. By default the maximum number considered by the interpreter is 50, but try seeing how the running time of each program changes when you pass different values of max to each program. You should see that the running time has a bottleneck of max^k, where k is the maximum predicate arity in the program.

Once you understand the behavior of the example programs, try writing a program that defines a unary predicate `odd` and then proves that some numbers are either `odd` or `not odd`.