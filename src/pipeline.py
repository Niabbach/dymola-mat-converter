import sys
from dymola_loader import load_dymola
from normalizer import normalize
from exporter import export_all

def run(path):
    dm = load_dymola(path)
    df, static = normalize(dm)

    name = path.split("/")[-1].replace(".mat", "")
    export_all(df, static, name)

if __name__ == "__main__":
    run(sys.argv[1])
