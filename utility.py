import json
import pickle
import numpy as np
datacolumns=None
locations=None
model=None

def load():
    global datacolumns
    global locations
    global model
    with open("./static/columns.json", 'r') as f:
        datacolumns = json.load(f)['data_columns']
        locations = datacolumns[3:]
    with open('./artifects/banglore_home_prices_model.pickle', 'rb') as f:
        model = pickle.load(f)
def get_locations():
    return locations
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = datacolumns.index(location.lower())
    except:
        loc_index=-1
    x = np.zeros(len(datacolumns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
        if model.predict([x])[0] >0:
            return round(model.predict([x])[0],2)
        else:
            return "The house with given parameters is not possible in that specified area"

    

if __name__=="__main__":
    load()
    print(get_estimated_price('1st block jayanagar',3000,2,2))

