import fire


class TransactionUtil(object):
    """ TODO: Documentation """

    def clean(self, input):
        """
        Reads the input transactions file and removes the preheader info.

        TODO: Explain the format of the original files.
        """

        # Read the input file into a list without the pre-header information
        with open(input, 'r+') as f:
            transactions = f.readlines()[6:]

            # Set the stream position to the beginning
            f.seek(0)

            # Write the data back to the file
            for record in transactions:
                f.write(record)

            # Why?
            f.truncate()


if __name__ == '__main__':
    fire.Fire(TransactionUtil)
