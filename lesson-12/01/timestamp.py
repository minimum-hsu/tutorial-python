from datetime import datetime

def parse_timestamp(t):
    try:
        return datetime.strptime(
            t,
            "%Y-%m-%dT%H:%M:%SZ"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%dT%H:%M:%S.%fZ"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%dT%H:%M:%S%z"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%dT%H:%M:%S.%f%z"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%dT%H:%M:%S"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%dT%H:%M:%S.%f"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%d %H:%M:%SZ"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%d %H:%M:%S.%fZ"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%d %H:%M:%S%z"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%d %H:%M:%S.%f%z"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%d %H:%M:%S"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%Y-%m-%d %H:%M:%S.%f"
        ).utctimetuple()
    except Exception:
        pass

    try:
        return datetime.strptime(
            t,
            "%a %b %d %H:%M:%S %Z %Y"
        ).utctimetuple()
    except Exception:
        pass

    return None
