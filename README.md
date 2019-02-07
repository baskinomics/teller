# Teller

Teller is a utility script used to sanitize Bank of America transaction statements provided in a `.csv` file. These `.csv` files are downloaded from the BofA website and intended to be imported into Excel.

I intend to access this data via a programmatic approach for analysis, but the content of the file does not conform to a tabular data structure causing an unnecessary headache. Specifically there is descriptive information with its own columns and values prior to the actual tabular data representing the transactions themselves, i.e.

```
Description,,Summary Amt.
Beginning balance as of 01/01/2019,,"1000.00"
Total credits,,"1000.00"
Total debits,,"700.00"
Ending balance as of 01/31/2019,,"300.00"

Date,Description,Amount,Running Bal.
...
```

The purpose of this script is to remove that information.

## Getting Started

This project uses [Python Fire](https://github.com/google/python-fire). To run:

```bash
$ git clone git@github.com:baskinomics/teller.git
$ cd teller/
$ python3 teller.py clean /path/to/statements/transactions.txt /path/to/output/filename.txt
```
