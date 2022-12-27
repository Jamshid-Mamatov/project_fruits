def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    pass
    listdata=data.split('\n')
    target=1
    max=float(listdata[1].split(',')[1])
    for ind,value  in enumerate(listdata[1:],1):
       
        if max<float(value.split(',')[1]):
            max=float(value.split(',')[1])
            target=ind
            

    return listdata[target].split(',')[0]

with open("fruits.csv",'r') as f:
    fr=f.read()
    get_expensive_fruit(data=fr)