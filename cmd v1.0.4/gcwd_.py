import sys, os;
def getcwd() -> str:
    return os.path.dirname(os.path.realpath(sys.argv[0]));
