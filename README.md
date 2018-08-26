# Sitelist

usage: SiteList.py [-h] [-m MINLEN] [-d DEPTH] [-l] [-o OUTPUT] url

Generate a wordlist from the contents of a URL.

positional arguments:
  url                   The target site address.

optional arguments:
  -h, --help            show this help message and exit
  -m MINLEN, --minlen MINLEN
                        The minimum length for a word to be in the wordlist.
  -d DEPTH, --depth DEPTH
                        The maximum depth of links to parse.
  -l, --leet            Generate modified words from the existing ones using
                        leet substitution.
  -o OUTPUT, --output OUTPUT
                        Save wordlist to a file.
