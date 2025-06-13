#!/usr/bin/env python

import subprocess
import glob

def main():

#    run_programs("./")
    run_programs("../../")
    clean_pickles()

    return


def run_programs(path2scripts):

    p2s = path2scripts

    subprocess.call(["python",p2s+"inread.py"])
    subprocess.call(["python",p2s+"mag_ani_coeffs.py"])
    subprocess.call(["python",p2s+"coeffs2params.py"])
    subprocess.call(["python",p2s+"params2constants.py"])
    subprocess.call(["python",p2s+"write_constants.py"])

    return

def clean_pickles():

    # Get a list of .pkl files in the current directory
    pkl_files = glob.glob("*.pkl")

    # Check if any .pkl files were found
    if pkl_files:
        # Delete .pkl files using subprocess
        subprocess.run(["rm"] + pkl_files)
    else:
        print("No .pkl files found in the current directory.")

    return

main()
