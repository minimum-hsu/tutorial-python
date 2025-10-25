from datetime import datetime

def parse_timestamp(t):
    try:
        return datetime.strptime(
            t,
            '%Y-%m-%dT%H:%M:%SZ'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%dT%H:%M:%S.%fZ'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%dT%H:%M:%S%z'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%dT%H:%M:%S.%f%z'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%dT%H:%M:%S'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%dT%H:%M:%S.%f'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%d %H:%M:%SZ'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%d %H:%M:%S.%fZ'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%d %H:%M:%S%z'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%d %H:%M:%S.%f%z'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%d %H:%M:%S'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%Y-%m-%d %H:%M:%S.%f'
        ).utctimetuple()
    except:
        pass

    try:
        return datetime.strptime(
            t,
            '%a %b %d %H:%M:%S %Z %Y'
        ).utctimetuple()
    except:
        pass

    return None
