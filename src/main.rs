extern crate clap;
use clap::{Arg, App};

fn main() {
    let matches = App::new("Teller")
        .version("0.1.0")
        .author("Sean Baskin <seanbaskin@gmail.com>")
        .about("Sanitizes BofA transaction statement CSV files")
        .arg(Arg::with_name("input")
            .short("i")
            .long("input")
            .help("Sets the input file containing the transactions")
            .takes_value(true)
            .required(true))
        .get_matches();

    println!("Input file: {}", matches.value_of("input").unwrap())
}
