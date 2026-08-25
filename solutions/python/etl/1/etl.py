def transform(legacy_data):
    data = { i.lower(): k for k, v in legacy_data.items() for i in v }

    return data
