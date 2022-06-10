
def get_cs():
    """get string input"""
    return input()


def cs_to_lot(cs: str):
    """convert connected string to list of strings"""
    return [tuple(i.split('=')) for i in cs.split(';')]


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
