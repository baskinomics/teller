import fire


class TransactionUtil(object):
    """ TODO: Documentation """

    def clean(self, input, output):
        """
        Reads the input transactions file and removes the preheader info.

        TODO: Explain the format of the original files.
        """

        # Read the input file into a list without the pre-header information
        with open(input) as f:
            transactions = f.readlines()[7:]

        # Write the cleaned data to a new file
        with open(output, 'w') as f:
            for record in transactions:
                f.write(record)


if __name__ == '__main__':
    fire.Fire(TransactionUtil)
