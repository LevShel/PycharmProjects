def find_key(struct, key):
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'My site'
        },
        'body': {
            'h2': 'Here is heading',
            'div': 'Here is any block',
            'p': 'Here is new paragraph'
        }
    }
}

user_key = input('Key: ')
value = find_key(site, user_key)
if value:
    print(value)
else:
    print(f'There is no key "{user_key}"')
