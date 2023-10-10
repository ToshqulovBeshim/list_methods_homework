def main(f,x):
    """
    You will be given a list of fruits. Add x fruit to it from the end and return.
    Args:
        fruits(list): parameter 
        x(str): parameter
    Returns:
        list: return answer
    """
    f.append(x)
    return f
print(main(f=["apple","banana","sprait"],x="kivi"))