if __name__ == '__main__':
    """ Version 1
    n = int(raw_input())
    arr = map(int, raw_input().split())
    sa = set(arr)
    la = list(sa)
    la.sort()
    print la[-2]
    """
    # version 2
    n = raw_input()
    print sorted(set(map(int, raw_input().split())))[-2]
