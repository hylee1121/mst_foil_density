"""Title.

Desc.
"""
# %%
import os
import glob
import random
from itertools import islice
import pandas as pd


# %%
# def main():

# for testing
test_mode = True
subj_int = 10
proj_dir = os.getcwd()
data_dir = os.path.join(proj_dir, f"data/sub-{subj_int}")

# setup
block_foil = [0, 12, 24, 36]
num_targ = 24
num_lure = 24

# start output directory
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# make list of stimuli
num_enc = num_targ + num_lure
base_stim = num_enc * len(block_foil)
total_stim = base_stim + sum(block_foil)
stim_all = sorted(glob.glob(f"{proj_dir}/Set**/*a.jpg", recursive=True))
stim_all = [x.replace(f"{proj_dir}/", "") for x in stim_all]
assert (
    len(stim_all) > total_stim
), f"Insufficient number of stimuli, expected {stim_all}"

# get random list
random.seed(subj_int)
if not test_mode:
    random.shuffle(stim_all)
stim_subj = stim_all[:total_stim]

# %%
# split stim_subj into block chunks
if not test_mode:
    random.shuffle(block_foil)
stim_subj_iter = iter(stim_subj)
block_size = [x + num_enc for x in block_foil]
block_list = [list(islice(stim_subj_iter, x)) for x in block_size]
block_dict = {}
for idx, block_stim in enumerate(block_list):
    block_dict[block_foil[idx]] = block_stim

# %%
block_num = 1
enc_dict = {}
for num_foil, block_stim in block_dict.items():

    if not test_mode:
        random.shuffle(block_stim)
    enc_stim = block_stim[: -num_foil or None]
    enc_dict[f"encoding{block_num}"] = enc_stim

    block_stim_iter = iter(block_stim)
    ret_num = [num_targ, num_lure, num_foil]
    ret_targ, ret_lure, ret_foil = [list(islice(block_stim_iter, x)) for x in ret_num]
    ret_lure = [x.replace("a.jpg", "b.jpg") for x in ret_lure]
    ret_stim = ret_targ + ret_lure + ret_foil

    if not test_mode:
        random.shuffle(ret_stim)
    ret_dict = {f"retrieval{block_num}": ret_stim}
    df_ret = pd.DataFrame(data=ret_dict)
    ret_out = os.path.join(data_dir, f"retrieval{block_num}.xlsx")
    df_ret.to_excel(ret_out, index=False)

    block_num += 1

df_enc = pd.DataFrame(data=enc_dict)
enc_out = os.path.join(data_dir, "encoding.xlsx")
df_enc.to_excel(enc_out, index=False)

# if __name__ == "__main__":
#     main()

# %%
