import json
import os
from dataclasses import dataclass


@dataclass
class Finding:
    file: str
    line: int
    message: str


def load_config(path="config.json"):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)


def analyze_lines(lines):
    findings = []
    for i, line in enumerate(lines):
        if "TODO" in line:
            findings.append(Finding(file="unknown", line=i, message="todo found"))
        if line.strip().endswith("  "):
            findings.append(Finding(file="unknown", line=i, message="trailing spaces"))
    return findings


def main():
    cfg = load_config()
    path = cfg.get("target", "README.md")
    with open(path) as f:
        lines = f.readlines()
    findings = analyze_lines(lines)
    print(findings)


if __name__ == "__main__":
    main()

