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
        if isinstance(value, type):
            return ""
        return str(value).strip()
    elif schema is bool:
        if isinstance(value, type):
            return False
        return bool(value)
    elif isinstance(schema, (tuple, list, dict)):
        if not value or not isinstance(value, type(schema)):
            return type(schema)()
        if not schema:
            return value
        if isinstance(schema, dict):
            collection = {}
            for k in schema.keys():
                node_value = value if k in value else schema
                node = validate(node_value[k], schema[k])
                if node:
                    collection[k] = node
            return collection
        else:
            collection = []
            for item in value:
                node = validate(item, schema[0])
                if node:
                    collection.append(validate(item, schema[0]))
            return type(schema)(collection)
    return None
