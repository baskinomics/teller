# Teller

Teller is a command-line interface ("CLI") program used to sanitize Bank of America transaction statements provided in a `.txt` file. These `.txt` files are downloaded from the BofA website and intended to be imported into Excel.

I, however, intend to access this data via a programmatic approach for analysis. Unfortunately the content of the file does not conform to a tabular data structure causing an unnecessary headache. Specifically there is descriptive information with its own columns and values prior to the actual tabular data representing the transactions themselves, i.e.

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

This project uses [Rust](https://www.rust-lang.org/). To run:

```bash
$ git clone git@github.com:baskinomics/teller.git
$ cd teller/
$ cargo run --input /path/to/statements/transactions.txt
```
