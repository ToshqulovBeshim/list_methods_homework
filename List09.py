def main(f):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    x=f.count("apple")
    a=0
    ls=[]
    while a<len(f):
        if f[a]=="apple":
            ls.append(a)
        a+=1
    ls.insert(0,x)
    return ls
print(main(f = ["apple", "banana", "apple", "pear", "apple"]))