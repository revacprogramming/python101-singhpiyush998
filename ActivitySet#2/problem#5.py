

def get_cs():
    """get string input"""


def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    return dict(i.split('=') for i in cs.split(';'))


def dict_to_cs(d):
    """convert a dictionary to connect string"""
    return ';'.join('='.join(i) for i in d.items())


def main():
    cs = get_cs()

    d = cs_to_dict(cs)  # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
