import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
BUILD_DIR = "build"
BIN_DIR = f"{BUILD_DIR}/bin"
TARGET = "todo"
SOURCES = "main.hs",

dirs = BUILD_DIR, BIN_DIR,

if __name__ == '__main__':
    command = f"ghc -hidir {CURRENT_DIR}/{BUILD_DIR} -odir {CURRENT_DIR}/{BUILD_DIR} -o {CURRENT_DIR}/{BIN_DIR}/{TARGET} {' '.join(SOURCES)}"

    for dir in dirs:
        path = f"{CURRENT_DIR}/{dir}"

        if os.path.exists(path) == False:
            print("Creating directory:", dir)
            os.makedirs(path, exist_ok=True)

    print("Executing:", command)
    os.system(command)
