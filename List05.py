def main(n1, n2):
    """
    You are given a list called numbers1 and numbers2.
    Delete the last item in the first list and add that deleted item to the beginning of the second list.
    Merge the first list into the second and return.
    Args:
        numbers1(list): parameter
        numbers2(list): parameter
    Returns:
        list: return answer
    """
    a=n1.pop(len(n1)-1)
    n2.insert(0,a)
    n1.extend(n2)
    return n1
print(main([1,3,5],[3,5,7]))