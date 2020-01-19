# Virtual environments

A virtual environment is a self contained directory tree that contains a
python installation for a particualr version of python, plus a number of 
additional packages. 

## Create virtual environment

```
python3 -m venv <env-name>
```

The last command will create the `<env-name>` directory if it does not exist,
and also create directoreis inside it containing a copy of the python 
interpreter, the std library and various supporting libraries.

## Activate envitonments

Once the environment has been created it needs to be activated:

```
source <env-name>/bin/activate
```

The `activate` file is a bash shell script, there are versions also for `csh`
and fish shell.

When the environment is activated the shell prompt will change, at this point
we can manage packages using `pip` which will affect only the activated env.