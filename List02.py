def main(f,x,i):
    """
    You will be given a list of fruits. Add the x fruit to the i index and return it.
    Args:
        fruits(list): parameter 
        x(str): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    f.insert(i,x)
    return f
print(main(f=["banana","apelsin","asdf"],x="kivi",i=1))