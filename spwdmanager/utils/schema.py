def validate(value, schema):
    """"Declarative object validator."""
    if value is None:
        return validate(schema, schema)
    elif schema in (int, float):
        try:
            return schema(value)
        except (TypeError, ValueError):
            return 0
    elif schema is str:
        if isinstance(type(value), type):
            return ""
        return str(value).strip()
    elif schema is bool:
        if isinstance(type(value), type):
            return False
        return bool(value)
    elif isinstance(schema, (tuple, list, dict)):
        if value is None or not isinstance(value, type(schema)):
            return type(schema)()
        if not schema:
            return value
        if isinstance(schema, dict):
            collection = {}
            for k in schema.keys():
                node = value if k in value else schema
                collection[k] = validate(node[k], schema[k])
            return collection
        else:
            collection = []
            for item in value:
                collection.append(validate(item, schema[0]))
            return type(schema)(collection)
    return None
