from typing import List
import pandas as pd

def fibonacci_sequence(number: int) -> int:
    """
    return the number at the position in the Fibonacci
    
    Parameters
    ----------
    number: int

    F(n) = F(n-1) + F(n-2)
    """

    # initialize the first two fibonacci numbers
    nums: List[int] = [0,1]

    # ensure that the number passed in parameter is not less than zero
    if number < 0:
        raise Exception("number must be 0")

    # Generate the next fibonacci numbers upto the number passed as parameter
    for i in range(2, number+1):
        nums.append(nums[i-1] + nums[i-2])

    return nums[number-1]


print(fibonacci_sequence(9))



def reverse_word(s:str) -> str:
    """
    reverse the order of the words

    Parameters
    ----------
    s: str
    """
    # remove leading and trailing whitespaces
    s: str = s.strip()

    # return a string of the words in reverse order concatenated by a single space
    return " ".join(s.split()[::-1])

print(reverse_word("Brian Kivuti"))
print(reverse_word("Hello world two"))
print(reverse_word("Joseph"))



def server_access(filename: str, top: int = 10):
    """    
    Parameters
    ----------
    filename: str - the name of csv file
    top: filter value defaults to 10
    """
    
    # create a dataframe and read the csv
    df = pd.read_csv(filename)

    # count the number of times each ip address is visible
    ip_address_access_count = df["IP"].value_counts().to_dict()


    # top 10 IP address that accessed the server the most
    # dictionary comprehension to only filter the first 10 values from result og ip_address_access_count
    first_10 = { k:v for (k,v) in [x for x in ip_address_access_count.items()][:top]}

    return first_10


print(server_access("serverlog.csv"))