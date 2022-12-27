def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    listdata=data.split('\n')
    total_amount=0
    for item in listdata[1:]:
        total_amount+=float(item.split(',')[1])
    return total_amount

    
with open("fruits.csv",'r') as f:
    fr=f.read()
    get_total_price(data=fr)