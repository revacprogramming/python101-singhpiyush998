

def get_cs():
    """get string input"""
    return input()


def cs_to_lot(cs):
    """convert connected string to list of strings"""
    return [tuple(i.split('=')) for i in cs.split(';')]



def lot_to_cs(lot):
    """convert list of strings to connected string"""
    return ';'.join('='.join(i) for i in lot)


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs = lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)

if __name__ == '__main__':
    main()
