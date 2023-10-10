def main(f):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    a=0
    ls=[]
    while a<len(f):
        if f[a]!="apple":
            ls.append(f[a])
        a+=1
    return ls
print(main(f=["apple","apple","banana","bear"]))
print(main(["apple", "apple", "apple", "apple", "kiwi"]))