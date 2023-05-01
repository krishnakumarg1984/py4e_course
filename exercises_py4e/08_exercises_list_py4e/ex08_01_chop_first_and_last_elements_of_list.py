def chop(t: list[int]):
    if t:
        del t[0]
    if t:
        t.pop()


def middle(t: list[int]):
    return t[1:-1] if t else []


if __name__ == "__main__":
    mylist = [1, 2, 3]
    # mylist: list[int] = []
    chop(mylist)
    print(mylist)
    mylist2 = [1, 2, 3, 4, 5, 6]
    # mylist2 = [1, 2]
    # mylist2 = [1]
    # mylist2: list[int] = []
    print(middle(mylist2))
