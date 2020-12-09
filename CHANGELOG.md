# xdg-binary-cache Changelog

## 1.4

* Fix bug introduced in 1.3 which failed to handle situations where argument flags were not provided.

## 1.3

* Use fcntl.flock() to coordinate parallel runs attemting to download the binary at the same time
* Move to using pathlib.Path rather than raw strings for most APIs

## 1.2

* Add `download_binary_with_retry(retries: int)`. Make `run_binary()` use it.

## 1.1

* Reduced log message level for "Already found `{binary_name}` at ..."

## 1.0

Initial release
