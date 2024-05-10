def clean_autonomous_community_name(name):
    if name.split()[0].isdigit():
        return ' '.join(name.split()[1:])
    else:
        return name
