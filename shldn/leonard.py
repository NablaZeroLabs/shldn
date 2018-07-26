"""
Leonard always DRIVES Sheldon (this module is the __main__ driver for shldn)
"""
import os
import argparse

try:
    from cooper import Sheldon
except:
    from .cooper import Sheldon


def parse_commandline():
    parser = argparse.ArgumentParser(
        description="Find divisions in Python code")

    parser.add_argument("-u", "--human_readable",
                        help="Display friendlier output",
                        action="store_true")

    parser.add_argument("-r", "--recursive",
                        help="Scan subdirectories recursively",
                        action="store_true")

    parser.add_argument("-e", "--file_extensions",
                        type=str,
                        help="Specify Python file extensions")

    parser.add_argument("path",
                        type=str,
                        help="Path to the target file or directory")

    return parser.parse_args()


def process_files(files, readable):
    divs_found = 0
    for file in files:
        with open(file) as f:
            pysource = f.read()
            s = Sheldon(pysource, file)
            s.analyze()
            divs_found += len(s.divisions)
            s.printdivs(readable)
    return divs_found


def get_files(path, recursive, extensions):
    files = []
    extensions = extensions or Sheldon.DEFAULT_EXTENSIONS

    if os.path.isdir(path):
        for path, _, cur_files in os.walk(path):
            for f in cur_files:
                if f.endswith(tuple(extensions)):
                    files.append(os.path.join(path, f))

            if not recursive:
                break

    elif os.path.isfile(path):
        if path.endswith(tuple(extensions)):
            files.append(path)
        else:
            exit(f"{path} ends with unspecified Python extension")

    else:
        exit(f"{path} doesn't exist!")

    return files


def main():

    args = parse_commandline()

    if args.human_readable:
        def readableprint(*args, **kwargs):
            print(*args, **kwargs)
    else:
        readableprint = lambda *a, **k: None  # do - nothing function

    if args.file_extensions:
        files = get_files(args.path, args.recursive, [args.file_extensions])
    else:
        files = get_files(args.path, args.recursive, None)
    divs_found = process_files(files, args.human_readable)

    readableprint(f"{len(files)} files processed")
    readableprint(f"{divs_found} divisions found")


if __name__ == "__main__":
    main()
