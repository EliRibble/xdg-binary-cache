# xdg-binary-cache

This is a simple library that is used to download a pre-compiled binary
into the `$XDG_CACHE` directory. The library is meant to be used by
[pre-commit](https://pre-commit.com) hooks that I've authored.

## Hacking

You'll want to install the developer dependencies:

```
pip install -e .[develop]
```

This will include `nose2` which is the test runner of choice. After you make modifications you can run tests with

```
nose2
```

When you're satisfied you'll want to update the version number and do build-and-upload:

```
python setup.py sdist bdist_wheel
twine upload dist/* --verbose
```
