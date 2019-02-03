import sys


def clean(input, output):
    """
    Reads the input transactions file and removes the un-needed descriptors.

    TODO: Explain the format of the original files.
    """

    # Read the input file into a list without the pre-header information
    with open(input) as f:
        transactions = f.readlines()[7:]

    # Write the cleaned data to a new file
    with open(output, 'w') as f:
        for record in transactions:
            f.write(record)


# Run the function using the second and third arguments
clean(sys.argv[1], sys.argv[2])
