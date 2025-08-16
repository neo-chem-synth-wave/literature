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
        "-ldp",
        "--literature_directory_path",
        default="../literature",
        type=str,
        help="The path to the directory where the literature is stored."
    )

    argument_parser.add_argument(
        "-st",
        "--search_tags",
        nargs="+",
        default=None,  # ["uspto"],
        type=str,
        help="The search tags."
    )

    return argument_parser.parse_args()


if __name__ == "__main__":
    script_arguments = get_script_arguments()

    search_results = list()
    search_tags = list() if script_arguments.search_tags is None else script_arguments.search_tags

    for literature_year_directory_path, _, literature_file_names in walk(
        top=script_arguments.literature_directory_path
    ):
        for literature_file_name in literature_file_names:
            if literature_file_name.endswith(".md"):
                literature_file_text = Path(literature_year_directory_path, literature_file_name).read_text()

                literature_file_tags = search(r"\*\*Tags:\*\*\s*\n(.+)", literature_file_text).group(1).split(", ")

                if all(
                    any(search_tag in literature_file_tag for literature_file_tag in literature_file_tags)
                    for search_tag in search_tags
                ):
                    search_results.append(
                        literature_file_name
                    )

    print("The search results for the tags [{search_tags:s}] are as follows:".format(
        search_tags=", ".join(
            "'{search_tag:s}'".format(
                search_tag=search_tag
            ) for search_tag in search_tags
        )
    ))

    if search_results:
        search_results_by_year = defaultdict(list)

        for literature_file_name in sorted(search_results):
            search_results_by_year[literature_file_name[:4]].append(
                literature_file_name
            )

        for year in search_results_by_year.keys():
            print()
            print(year)

            for literature_file_name in search_results_by_year[year]:
                print(literature_file_name)

    else:
        print("\nNo results.")
