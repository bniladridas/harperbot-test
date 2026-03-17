import json


def main():
    with open("config.json") as f:
        cfg = json.load(f)
    print("ok", cfg.get("target"))


if __name__ == "__main__":
    main()

