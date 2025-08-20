""" The ``scripts`` directory ``generate_timeline_markdown_table`` script. """

from argparse import ArgumentParser, Namespace
from os import walk
from pathlib import Path
from re import DOTALL, search


def get_script_arguments() -> Namespace:
    """
    Get the script arguments.

    :returns: The script arguments.
    """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-idp",
        "--input_directory_path",
        default="../literature",
        type=str,
        help="The path to the input directory where the literature is stored."
    )

    return argument_parser.parse_args()


if __name__ == "__main__":
    script_arguments = get_script_arguments()

    timeline_markdown_table_rows = list()

    timeline_markdown_table_header_row = "| Publication Date | Publication | Tags | Starred |\n|:-:|-|:-:|:-:|"

    for publication_year_directory_path, _, file_names in walk(
        top=script_arguments.input_directory_path
    ):
        for file_name in file_names:
            if file_name.endswith(".md") and file_name != "format.md":
                file_path = Path(publication_year_directory_path, file_name)

                file_text = file_path.read_text()

                timeline_markdown_table_rows.append(
                    "| {publication_date:s} | [{authors:s} {title:s}]({file_path:s}) | {tags:s} | {starred:s} |".format(
                        publication_date=search(r"Publication Date:\*\*\n(.+)", file_text).group(1),
                        authors=search(r"Authors:\*\*\n(.+?)(?=\n\*)", file_text, DOTALL).group(1).strip().split(" |\n")[-1],
                        title=search(r"Title:\*\*\n(.+)", file_text).group(1),
                        file_path=Path(*file_path.parts[1:]).as_posix(),
                        tags=search(r"Tags:\*\*\n(.+)", file_text).group(1),
                        starred=":star:" if search(r"Starred:\*\*\n(.+)", file_text).group(1) == "True" else ""
                    )
                )

    print()
    print(
        "Total number of files: {total_number_of_files:d}".format(
            total_number_of_files=len(timeline_markdown_table_rows)
        )
    )
    print()
    print(
        "{timeline_markdown_table_header_row:s}\n{timeline_markdown_table_rows:s}".format(
            timeline_markdown_table_header_row=timeline_markdown_table_header_row,
            timeline_markdown_table_rows="\n".join(sorted(timeline_markdown_table_rows))
        )
    )
