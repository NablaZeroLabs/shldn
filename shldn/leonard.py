"""
Leonard always DRIVES Sheldon (this module is the __main__ driver for Sheldon)
"""
import os
import argparse

try:
    from cooper import Sheldon
except:
    from .cooper import Sheldon

# Extensions for python source files
EXTENSIONS = [".py", ".mpy"]


def parse_commandline():
    parser = argparse.ArgumentParser(
        description="Find divisions in Python code")

    parser.add_argument("-u", "--human_readable",
                        help="Display friendlier output",
                        action="store_true")

    parser.add_argument("-r", "--recursive",
                        help="Scan subdirectories recursively",
                        action="store_true")

    parser.add_argument("path",
                        type=str,
                        help="Path to the target file or directory")

    return parser.parse_args()


def process_files(files, divs_found, readable, path=""):
    for filename in files:
        fpath = os.path.join(path, filename)
        with open(fpath) as f:
            pysource = f.read()
            s = Sheldon(pysource, fpath)
            s.analyze()
            divs_found += len(s.divisions)
            s.printdivs(readable)
    return divs_found


def main():
    args = parse_commandline()

    if args.human_readable:
        def readableprint(*args, **kwargs):
            print(*args, **kwargs)
    else:
        readableprint = lambda *a, **k: None  # do - nothing function

    files_checked = 0
    divs_found = 0

    # Directory path
    if os.path.isdir(args.path):
        for path, _, _ in os.walk(args.path):
            files = [f for f in os.listdir(
                path) if f.endswith(tuple(EXTENSIONS))]
            files_checked += len(files)

            divs_found = process_files(
                files, divs_found, args.human_readable, path=path)

            if not args.recursive:
                exit(0)

        readableprint(f"{files_checked} files checked")
        readableprint(f"{divs_found} divisions found")

    # File path
    elif os.path.isfile(args.path):
        files = [f for f in [args.path]
                 if args.path.endswith(tuple(EXTENSIONS))]

        divs_found = process_files(files, divs_found, args.human_readable)

        readableprint(f"{divs_found} divisions found")

    # Error
    else:
        exit(f"{args.path} doesn't exist!")


if __name__ == "__main__":
    main()
