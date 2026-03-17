import json


def build_payload(user, flags):
    # intentionally verbose / style issues for review suggestions
    payload = {}
    payload["user"] = user
    payload["flags"] = flags
    payload["active"] = True
    payload["meta"] = {"source": "test", "version": 1}
    payload["tags"] = []
    if flags != None and "beta" in flags:
        payload["tags"].append("beta")
    if flags != None and "internal" in flags:
        payload["tags"].append("internal")
    return payload


def to_json(payload):
    return json.dumps(payload, indent=2, sort_keys=True)


def main():
    p = build_payload("niladri", ["beta", "internal"])
    print(to_json(p))


if __name__ == "__main__":
    main()

