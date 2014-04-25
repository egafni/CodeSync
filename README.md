CodeSync
========

Uses the watchdog python library to rsync a directory to a server on filesystem changes.


Usage
======

    $ csync -h
    usage: csync [-h] [-x EXCLUDE_FROM] [-p PATTERNS] [-c CALLBACK] src dest

    positional arguments:
      src
      dest

    optional arguments:
      -h, --help            show this help message and exit
      -x EXCLUDE_FROM, --exclude_from EXCLUDE_FROM
                            a file containing patterns to exclude from. Passed to
                            rsyncs `exclude-from` argument.
      -p PATTERNS, --patterns PATTERNS
                            semi-colon separated list of patterns that trigger an
                            rsync (default is `*.py`)
      -c CALLBACK, --callback CALLBACK
                            Executes this string after each rsync. For example, if
                            you're on a mac, you can play a sound with: `-c
                            'afplay /System/Library/Sounds/Morse.aiff'`


Alternatives
============

lsync