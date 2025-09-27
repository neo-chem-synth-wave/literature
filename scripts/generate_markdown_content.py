""" The ``scripts`` directory ``generate_markdown_content`` script. """

from argparse import ArgumentParser, Namespace
from collections import defaultdict
from itertools import chain
from logging import Formatter, Logger, StreamHandler, getLogger
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
        help="The path to the input directory where the literature markdown files are stored."
    )

    return argument_parser.parse_args()


def get_script_logger() -> Logger:
    """
    Get the script logger.

    :returns: The script logger.
    """

    logger = getLogger(
        name="script_logger"
    )

    logger.setLevel(
        level="DEBUG"
    )

    formatter = Formatter(
        fmt="[{name:s} @ {asctime:s}] {levelname:s}: \"{message:s}\"",
        style="{"
    )

    stream_handler = StreamHandler()

    stream_handler.setLevel(
        level="DEBUG"
    )

    stream_handler.setFormatter(
        fmt=formatter
    )

    logger.addHandler(
        hdlr=stream_handler
    )

    return logger


if __name__ == "__main__":
    script_arguments = get_script_arguments()

    script_logger = get_script_logger()

    publication_year_to_timeline_table_rows = defaultdict(list)

    timeline_table_header_row = "| Publication Date | Publication | Tags |\n|:-:|-|:-:|"

    for directory_path, _, file_names in walk(
        top=script_arguments.input_directory_path
    ):
        for file_name in file_names:
            if file_name.endswith(".md"):
                file_path = Path(directory_path, file_name)

                file_text = file_path.read_text()

                publication_year_to_timeline_table_rows[file_path.parts[2]].append(
                    "| {publication_date:s} | [{authors:s} {title:s}]({file_path:s}) | {tags:s} |".format(
                        publication_date=search(
                            pattern=r"\*\*Publication Date:\*\*\n(.+)",
                            string=file_text
                        ).group(1),
                        authors=search(
                            pattern=r"\*\*Authors:\*\*\n(.+?)(?=\n\*)",
                            string=file_text,
                            flags=DOTALL
                        ).group(1).strip().split(" |\n")[-1],
                        title=search(
                            pattern=r"\*\*Title:\*\*\n(.+)",
                            string=file_text
                        ).group(1),
                        file_path=Path("literature", *file_path.parts[-2:]).as_posix(),
                        tags=search(
                            pattern=r"\*\*Tags:\*\*\n(.+)",
                            string=file_text
                        ).group(1)
                    )
                )

    all_timeline_table_rows = sorted(
        chain.from_iterable(publication_year_to_timeline_table_rows.values()),
        reverse=True
    )

    print("1. The 'README.md' markdown content:\n")

    print((
        "## Timeline\n[![Static Badge](https://img.shields.io/badge/total-{number_of_timeline_table_rows:d}-white)]"
        "(#timeline)"
    ).format(
        number_of_timeline_table_rows=len(all_timeline_table_rows)
    ))

    for publication_year, timeline_table_rows in publication_year_to_timeline_table_rows.items():
        print((
            "[![Static Badge](https://img.shields.io/badge/"
            "{publication_year:s}-{number_of_timeline_table_rows:d}-{color:s})](#timeline)"
        ).format(
            publication_year=publication_year,
            number_of_timeline_table_rows=len(timeline_table_rows),
            color=(
                "red" if len(timeline_table_rows) < 10 else
                "orange" if 10 <= len(timeline_table_rows) < 20 else
                "yellow" if 20 <= len(timeline_table_rows) < 30 else
                "green" if 30 <= len(timeline_table_rows) < 40 else
                "blue"
            )
        ))

    print((
        "\n{timeline_table_header_row:s}\n"
        "{timeline_table_rows:s}\n"
        "| ... | [See All](/documentation/b_timeline.md) | ... |"
    ).format(
            timeline_table_header_row=timeline_table_header_row,
            timeline_table_rows="\n".join(all_timeline_table_rows[0:10])
        )
    )

    print("\n\n2. The 'b_timeline.md' markdown content:\n")

    print((
        "# Timeline\n[![Static Badge](https://img.shields.io/badge/total-{number_of_timeline_table_rows:d}-white)]"
        "(#timeline)"
    ).format(
        number_of_timeline_table_rows=len(all_timeline_table_rows)
    ))

    for publication_year, timeline_table_rows in publication_year_to_timeline_table_rows.items():
        print((
            "[![Static Badge](https://img.shields.io/badge/"
            "{publication_year:s}-{number_of_timeline_table_rows:d}-{color:s})](#{publication_year:s})"
        ).format(
            publication_year=publication_year,
            number_of_timeline_table_rows=len(timeline_table_rows),
            color=(
                "red" if len(timeline_table_rows) < 10 else
                "orange" if 10 <= len(timeline_table_rows) < 20 else
                "yellow" if 20 <= len(timeline_table_rows) < 30 else
                "green" if 30 <= len(timeline_table_rows) < 40 else
                "blue"
            )
        ))

    for publication_year_index, publication_year in enumerate(sorted(
        publication_year_to_timeline_table_rows.keys(),
        reverse=True
    )):
        print(
            "\n\n### {publication_year:s}\n{timeline_table_header_row:s}\n{timeline_table_rows:s}".format(
                publication_year=publication_year,
                timeline_table_header_row=timeline_table_header_row,
                timeline_table_rows="\n".join(sorted([
                    publication_year_timeline_table_row.replace("(literature", "(../literature", 1)
                    for publication_year_timeline_table_row in publication_year_to_timeline_table_rows[
                        publication_year
                    ]], reverse=True))
            )
        )
