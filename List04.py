def main(n,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    a=n.pop(i)
    return a
print (main([1,3,5,8,34567,3,5,6,7],4))