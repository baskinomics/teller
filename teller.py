import sys


def clean(input, output):
    """
    Reads the input transactions file and removes the un-needed descriptors.

    TODO: Explain the format of the original files.
    """
    with open(input) as f:
        transactions = f.readlines()[7:]

    with open(output, 'w') as f:
        for record in transactions:
            f.write(record)


# Run the function
clean(sys.argv[1], sys.argv[2])
