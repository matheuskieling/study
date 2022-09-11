import csv
from sys import argv


def main():

    # TODO: Check for command-line usage
    if len(argv) == 3:
        if argv[1] == "databases/large.csv":
            # TODO: Read database file into a variable
            with open(argv[1], "r") as data_dict:
                reader = csv.DictReader(data_dict)
                data = []
                for row in reader:
                    data.append(row)
            with open(argv[1], "r") as data_dict:
                subsequences_list = data_dict.readline()
                subsequences_list = subsequences_list.replace("\n", "").split(",")
            # TODO: Read DNA sequence file into a variable
            with open(argv[2], "r") as sequence:
                dna_sequence = sequence.readline()
            # TODO: Find longest match of each STR in DNA sequence
            long_match_list = []
            for _ in subsequences_list[1::]:
                long_match = longest_match(dna_sequence, _)
                long_match_list.append(long_match)
            # TODO: Check database for matching profiles
            for dict in data:
                if (
                    dict["AGATC"] == str(long_match_list[0])
                    and dict["TTTTTTCT"] == str(long_match_list[1])
                    and dict["AATG"] == str(long_match_list[2])
                    and dict["TCTAG"] == str(long_match_list[3])
                    and dict["GATA"] == str(long_match_list[4])
                    and dict["TATC"] == str(long_match_list[5])
                    and dict["GAAA"] == str(long_match_list[6])
                    and dict["TCTG"] == str(long_match_list[7])

                ):
                    return dict["name"]
            return "No match"

        elif argv[1] == "databases/small.csv":
            # TODO: Read database file into a variable
            with open(argv[1], "r") as data_dict:
                reader = csv.DictReader(data_dict)
                data = []
                for row in reader:
                    data.append(row)
            with open(argv[1], "r") as data_dict:
                subsequences_list = data_dict.readline()
                subsequences_list = subsequences_list.replace("\n", "").split(",")
            # TODO: Read DNA sequence file into a variable
            with open(argv[2], "r") as sequence:
                dna_sequence = sequence.readline()
            # TODO: Find longest match of each STR in DNA sequence
            long_match_list = []
            for _ in subsequences_list[1::]:
                long_match = longest_match(dna_sequence, _)
                long_match_list.append(long_match)
            # TODO: Check database for matching profiles
            for dict in data:
                if (
                    dict["AGATC"] == str(long_match_list[0])
                    and dict["AATG"] == str(long_match_list[1])
                    and dict["TATC"] == str(long_match_list[2])
                ):
                    return dict["name"]
            return "No match"
    else:
        print("Usage: python dna.py data.csv sequence.txt")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


print(main())
