# Teller

Teller in its current state represents the early days of a utility program used to perform ETL on Bank of America (BofA) transaction text files. At the time of this writing it merely removes the pre-header information from the file.

## Getting Started

This project uses [Python Fire](https://github.com/google/python-fire). To run:

```bash
$ git clone git@github.com:baskinomics/teller-py.git
$ cd teller-py/
$ python3 teller.py clean /path/to/statements/transactions.txt /path/to/output/filename.txt
```
