from unidecode import unidecode


def clean_autonomous_community_name(name):
    name_without_accents = unidecode(name)
    if name_without_accents.split()[0].isdigit():
        return ' '.join(name_without_accents.split()[1:])
    else:
        return name_without_accents
