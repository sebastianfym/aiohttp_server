import hashlib


def value_hash(value):
    value_bytes = value.encode('utf-8')

    hash_obj = hashlib.sha256()

    hash_obj.update(value_bytes)

    hashed_string = hash_obj.hexdigest()

    return hashed_string