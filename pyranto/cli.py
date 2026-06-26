from .functions import runpyr, printpyr, reverse_print
from pathlib import Path
import argparse

BASE_DIR = Path("pyranto/pyr_test_files").resolve()

def main():
    parser = argparse.ArgumentParser(
        prog="pyranto",
        description="Execute Python written in human languages.",
        epilog="Syntax: pyranto <mode> <file> <lang>, example: pyranto run hello.pyr tr"
    )
    
    parser.add_argument("mode", choices=["run", "print", "reverse"])
    parser.add_argument("file")
    parser.add_argument("lang")
    
    args = parser.parse_args()
    file = BASE_DIR / args.file # forcing folder for now
    
    match args.mode:
        case "run":
            runpyr(file, args.lang)
        case "print":
            printpyr(file, args.lang)
        case "reverse":
            reverse_print(file, args.lang)