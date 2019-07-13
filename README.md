# Facwash

Searches for and removes tracking data injected into JPG files uploaded to facebook.

First identified (to my knowledge) by [Edin Jusupovic](https://twitter.com/oasace/status/1149181539000864769).

## Usage

```
usage: facewash.py [-h] [-o] directory

positional arguments:
  directory        directory to search and clean

optional arguments:
  -h, --help       show this help message and exit
  -o, --overwrite  replace original files

```

Run `facewash.py` and point it to a directory, and it will work recursively. Cleaned images are saved as new files in the same folders unless the `--overwrite` flag is specified.
