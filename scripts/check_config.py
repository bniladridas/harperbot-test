import json
import os

def main():
    script_dir = os.path.dirname(__file__)
    c os.path.join(script_dir, "..", "config.json")
    with open(config_path) as f:
        cfg = json.load(f)
    print("ok", cfg.get("target"))


if __name__ == "__main__":
    main()

