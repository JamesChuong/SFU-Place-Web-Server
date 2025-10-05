

def dict_to_array(d):
    """Convert nested dicts with UID keys into lists"""
    if not isinstance(d, dict):
        return d

    result = []

    for key, value in d.items():

        if isinstance(value, dict):

            value["uid"] = value.get("uid", key)
            # Recursively convert nested dicts
            for k in ["users", "strokes"]:
                if k in value:
                    value[k] = dict_to_array(value[k])

        result.append(value)

    return result
