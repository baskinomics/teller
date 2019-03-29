extern crate clap;
use clap::{App, Arg};
use std::fs;

/// TODO Documentation
fn main() {
    let matches = App::new("Teller")
        .version("0.1.0")
        .author("Sean Baskin <seanbaskin`@gmail.com>")
        .about("Sanitizes BofA transaction statement CSV files")
        .arg(
            Arg::with_name("INPUT")
                .short("i")
                .long("input")
                .required(true)
                .takes_value(true)
                .help("Sets the input file containing the transactions"),
        )
        .get_matches();

    // Sanitize the input file
    let input: &str = matches.value_of("INPUT").unwrap();
    sanitize(&input);
}

/// Sanitizes the input file stream. Specifically, this function removes
/// the pre-header information prior to the data itself.
fn sanitize(filename: &str) {
    // 1. Read the file
    let contents = fs::read_to_string(filename).expect("Something went wrong reading the file");
    // Debugging
    println!("INPUT FILE\n{}", &contents);

    // 2. Remove the pre-header information
    // 3. Write the output to a new file
}
