def validLinkfunc(link2):
    linkValid = 'https://www.youtube.com/watch?v='

    if link2 == '':
        return 0

    for c in range(len(linkValid)):
        if linkValid[c] != link2[c]:
            return False

    return True