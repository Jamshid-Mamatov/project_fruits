def get_cheapest_fruit(data:str)->str:
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
    listdata=data.split('\n')
    target=1
    min=float(listdata[1].split(',')[1])
    for ind,value  in enumerate(listdata[1:],1):
       
        if min>float(value.split(',')[1]):
            min=float(value.split(',')[1])
            target=ind
            

    return listdata[target].split(',')[0]
    
with open("fruits.csv",'r') as f:
    fr=f.read()
    get_cheapest_fruit(data=fr)