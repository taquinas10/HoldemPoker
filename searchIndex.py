"""We need a function to quickly search through an ordered table of integers and find an entry.
    """
def search(entry,list):
    l=len(list)
    high=l-1
    low=0
    while low<=high:
        mid=(high+low)>>1
        if entry<list[mid]:
            high=mid-1
        elif entry>list[mid]:
            low=mid+1
        else: return mid

