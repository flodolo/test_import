#! /usr/bin/env python3

import argparse
import os
import shutil

files = [
    "vpn.ftl",
]

parser = argparse.ArgumentParser()
parser.add_argument("code_path", help="Path to the main repository")
parser.add_argument("l10n_path", help="Path to the l10n repository")
args = parser.parse_args()

excluded_folders = [".git", "en-US"]
folders = [
    f.path
    for f in os.scandir(args.l10n_path)
    if f.is_dir() and os.path.basename(os.path.normpath(f)) not in excluded_folders
]

for folder in folders:
    locale = os.path.basename(os.path.normpath(folder))
    output_folder = os.path.join(args.code_path, "locales", locale)
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    for f in files:
        l10n_file = os.path.join(args.l10n_path, locale, f)
        if os.path.isfile(l10n_file):
            print(f"Copying {f} for {locale}")
            dest_file = os.path.join(output_folder, f)
            shutil.copyfile(l10n_file, dest_file)
        else:
            print(f"ERROR: {l10n_file} is missing")
