import os

__base__ = os.path.dirname(os.path.abspath(__file__))

try:
    with open(f"{__base__}/../.env", "r") as env_file:
        for line in env_file:
            line = line.strip()
            if line.startswith("#") or (line.startswith("[") and line.endswith("]")) or not line:
                continue

            var, val = line.split("=", maxsplit=1)
            os.environ[var] = val.strip()
except OSError:
    pass

DATA_DIR = os.getenv("DATA_DIR", f"{__base__}/../data")
MODEL_DIR = os.getenv("MODEL_DIR", f"{__base__}/../models")

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)