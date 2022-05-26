"""Make stimulus files for foil density MST project.

Generate 4 blocks of encoding and test stimulus files, with
each block havin a different number of foils. Save output excel
files to data/sub-1234.

Test mode writes data/sub-9999 for checking numbers of encoding stimuli,
targets, lures, and foils for each block without decoding the randomization.

Overly commented, with description of each variable to help those new to python.

Examples
--------
python build_stim_sets.py --subj 1234

python build_stim_sets.py --test-mode
"""
import os
import sys
import glob
import random
from itertools import islice
import pandas as pd
import textwrap
from argparse import ArgumentParser, RawTextHelpFormatter


def get_args():
    """Get and parse arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        "--test-mode",
        action="store_true",
        help=textwrap.dedent(
            """\
            Toggle of whether to use the test mode.
            Boolean (True if "--test-mode", else False).
            """
        ),
    )

    parser.add_argument(
        "--subj", type=int, help="Subject identifier, e.g. 1234 for sub-1234.",
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser


def main():
    """Make subject stimulus files.
    
    All work done in main() so it can be incorporated
    in PsychoPy python script. If that's done, avoid writing
    excel files, keep the enc_dict, and make unique ret_dicts.
    """
    # Get command line arguments
    args = get_args().parse_args()
    test_mode = args.test_mode
    subj_int = args.subj

    # for testing - set subject num and turn off randomizing
    if test_mode:
        subj_int = 9999

    # Setup paradigm
    #   block_foil : length = number of runs, value = number of foils in run
    block_foil = [0, 12, 24, 36]
    num_targ = 24
    num_lure = 24

    # Start output directory - determine script location,
    #   make a subject directory in data.
    proj_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(proj_dir, f"data/sub-{subj_int}")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Make list of stimuli to be used for participant.
    #   num_enc : number of encoding trials, equal to number of test target & lures
    #   base_stim : total number of stimuli in task, without foils (which vary by block, plan)
    #   total_stim : base + planned foil stim
    #   stim_all : list of all 123a.jpg found in directories called Set*, sorted
    #       (for consistent randomizing below). Also stripped of absolute path,
    #       for PsychoPy portability
    num_enc = num_targ + num_lure
    base_stim = num_enc * len(block_foil)
    total_stim = base_stim + sum(block_foil)
    stim_all = sorted(glob.glob(f"{proj_dir}/Set**/*a.jpg", recursive=True))
    stim_all = [x.replace(f"{proj_dir}/", "") for x in stim_all]
    assert (
        len(stim_all) > total_stim
    ), f"Insufficient number of stimuli in Set? directories, expected {total_stim}."

    # Set randomizing seed off of subject's int identifier, and shuffle list
    #   so a unique stimulus set is pulled for each participant.
    #   stim_subj : subset of stim_all, only the required number of stimuli needed
    if not test_mode:
        random.seed(subj_int)
        random.shuffle(stim_all)
    stim_subj = stim_all[:total_stim]

    # Split stim_subj into chunks of appropriate block length. Also randomize
    # block_foil so participants get different foil density orders.
    #   block_size : list of total stimulus needed for each block
    #   block_list : nested list of stimuli for each block, in order of block_foil
    #   block_dict : dictionary version of block_list, with foil number as key
    if not test_mode:
        random.shuffle(block_foil)
    stim_subj_iter = iter(stim_subj)
    block_size = [x + num_enc for x in block_foil]
    block_list = [list(islice(stim_subj_iter, x)) for x in block_size]
    block_dict = {}
    for idx, block_stim in enumerate(block_list):
        block_dict[block_foil[idx]] = block_stim

    # Build each block. Combine encoding, write separate retrieval files.
    #   block_num : counter for writing block numbers
    #   enc_dict : dictionary for planned encoding blocks
    #   num_foil : number of planned foils for block
    #   block_stim : stimulus list for block
    block_num = 1
    enc_dict = {}
    for num_foil, block_stim in block_dict.items():

        # Set up encoding stimuli (by remove number of foils from block_stim),
        # update encoding dictionary (enc_dict). Randomize so the same positions
        # do not become lures for every participant. enc_dict key becomes column name.
        if not test_mode:
            random.shuffle(block_stim)
        enc_stim = block_stim[: -num_foil or None]
        enc_dict[f"encoding{block_num}"] = enc_stim

        # Set up retrieval stimuli. Split block_list into target, lure, and
        # foil lists according to their desired length. Switch file name to
        # make lures, stitch back together.
        block_stim_iter = iter(block_stim)
        ret_num = [num_targ, num_lure, num_foil]
        ret_targ, ret_lure, ret_foil = [
            list(islice(block_stim_iter, x)) for x in ret_num
        ]
        ret_lure = [x.replace("a.jpg", "b.jpg") for x in ret_lure]
        ret_stim = ret_targ + ret_lure + ret_foil

        # Build retrieval column, write out excel file. Randomize
        # so target, lure, foils presented randomly.
        #   ret_dict : dictionary of retrieval stimuli, key = column name
        #   df_ret : pandas dataframe of retrieval stimulus list
        #   ret_out : output excel path, name
        if not test_mode:
            random.shuffle(ret_stim)
        ret_dict = {f"retrieval{block_num}": ret_stim}
        df_ret = pd.DataFrame(data=ret_dict)
        ret_out = os.path.join(data_dir, f"retrieval{block_num}.xlsx")
        df_ret.to_excel(ret_out, index=False)

        block_num += 1

    # Write out encoding excel sheet.
    #   df_enc : pandas dataframe encoding stimulus dictionary
    #   enc_out : output path, file name
    df_enc = pd.DataFrame(data=enc_dict)
    enc_out = os.path.join(data_dir, "encoding.xlsx")
    df_enc.to_excel(enc_out, index=False)


if __name__ == "__main__":
    main()
