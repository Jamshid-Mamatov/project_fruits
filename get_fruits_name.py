def get_frutis_name(data:str)->list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """
    listdata=data.split('\n')
    listname=[]
    for name in listdata[1:]:
        listname.append(name.split(',')[0])
    return listname
    

with open("fruits.csv",'r') as f:
    fr=f.read()
    get_frutis_name(data=fr)

    