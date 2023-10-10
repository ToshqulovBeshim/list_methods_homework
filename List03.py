def main(f1, f2):
    """
    You will be given a list of several fruits called fruits1 and fruits2. Return the result by adding the second to the first list.
    Args:
        fruits1(list): parameter
        fruits2(list): parameter
    Returns:
        list: return answer
    """
  
    f1.extend(f2)
    return (f1)
print(main(["fghj","ghjkl","hjkl;l"],["rtfgyuhji","beshim dalbayop"]))