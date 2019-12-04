# -*- coding: utf-8 -*-

"""scaffold module"""

import argparse
import datetime
import os
import sys
from future.utils import iteritems
from .utils import save_json, write_txt


def get_arguments():
    """Load arguments for main"""
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="""
            Create basic BIDS files and directories
            """,
            epilog="""
            Documentation at https://github.com/cbedetti/Dcm2Bids
            """,
    )

    parser.add_argument(
        "-o",
        "--output_dir",
        required=False,
        default=os.getcwd(),
        help="Output BIDS directory, Default: current directory",
        )

    args = parser.parse_args()
    return args


JSON_FILES = {
    "dataset_description.json": {
        "Name": "",
        "BIDSVersion": "1.2.0",
        "License": "",
        "Authors": [""],
        "Acknowledgments": "",
        "HowToAcknowledge": "",
        "Funding": "",
        "ReferencesAndLinks": [""],
        "DatasetDOI": ""
        },
    "participants.json": {
        "education": {
            "LongName": "Education level",
            "Description": "Education level, self-rated by participant",
            "Levels": {
                "1": "Finished primary school",
                "2": "Finished secondary school",
                "3": "Student at university",
                "4": "Has degree from university"
                }
            },
        "bmi": {
            "LongName": "Body mass index",
            "Units": "kilograms per squared meters",
            "TermURL": "http://purl.bioontology.org/ontology/SNOMEDCT/60621009"
            }
        }
    }

TEXT_FILES = {
    "README": [],
    "CHANGES": [
        "Revision history for BIDS dataset",
        "",
        "1.0.0 " + datetime.date.today().strftime("%Y-%m-%d"),
        "",
        " - Initialised study directory",
        ],
    "participants.tsv": ["participant_id\teducation\tbmi", "sub-01\tn/a\tn/a"],
    }


def main():
    """Let's go"""
    args = get_arguments()

    for _ in ["code", "derivatives", "sourcedata"]:
        # os.makedirs(os.path.join(args.output_dir, _), exist_ok=True)
        # python2 compatibility
        if not os.path.exists(os.path.join(args.output_dir, _)):
            os.makedirs(os.path.join(args.output_dir, _))

    for filename, data in iteritems(JSON_FILES):
        filepath = os.path.join(args.output_dir, filename)
        if not os.path.exists(filepath):
            save_json(filepath, data)

    for filename, data in iteritems(TEXT_FILES):
        filepath = os.path.join(args.output_dir, filename)
        if not os.path.exists(filepath):
            write_txt(filepath, data)

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())