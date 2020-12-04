# xdg-binary-cache Changelog

## 1.3

* Move to using pathlib.Path rather than raw strings for most APIs

## 1.2

* Add `download_binary_with_retry(retries: int)`. Make `run_binary()` use it.

## 1.1

* Reduced log message level for "Already found `{binary_name}` at ..."

## 1.0

Initial release
