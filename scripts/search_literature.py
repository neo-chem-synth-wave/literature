""" The ``scripts`` directory ``search_literature`` script. """

from argparse import ArgumentParser, Namespace
from collections import defaultdict
from os import walk
from pathlib import Path
from re import search


def get_script_arguments() -> Namespace:
    """
    Get the script arguments.

    :returns: The script arguments.
    """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-idp",
        "--input_directory_path",
        type=str,
        help="The path to the input directory where the literature is stored."
    )

    argument_parser.add_argument(
        "-st",
        "--search_tags",
        nargs="+",
        default=None,
        type=str,
        help="The tags of the search."
    )

    return argument_parser.parse_args()


if __name__ == "__main__":
    script_arguments = get_script_arguments()

    file_paths = list()
    search_tags = list() if script_arguments.search_tags is None else script_arguments.search_tags

    for publication_year_directory_path, _, file_names in walk(
        top=script_arguments.input_directory_path
    ):
        for file_name in file_names:
            if file_name.endswith(".md") and file_name != "format.md":
                file_path = Path(publication_year_directory_path, file_name)

                file_text = file_path.read_text()

                file_tags = search(r"Tags:\*\*\n(.+)", file_text).group(1).split(", ")

                if all(
                    any(search_tag in file_tag for file_tag in file_tags)
                    for search_tag in search_tags
                ):
                    file_paths.append(
                        file_path.as_posix()
                    )

    print("The search for the tags [{search_tags:s}] returned the following literature:".format(
        search_tags=", ".join("'{search_tag:s}'".format(
            search_tag=search_tag
        ) for search_tag in search_tags)
    ))

    if file_paths:
        publication_year_to_file_paths = defaultdict(list)

        for file_path in sorted(file_paths):
            publication_year_to_file_paths[file_path.split("/")[-2]].append(
                file_path
            )

        for publication_year in publication_year_to_file_paths.keys():
            print()
            print(publication_year)

            for file_path in publication_year_to_file_paths[publication_year]:
                print(file_path)

    else:
        print("\nNone")
