import requests
import json

# save the api key
API_KEY = 'PRlaNFB3LpWOn14ICWIqupBkZa4ZKKdSkvpDwIJC'
USDA_ENDPOINT = '@api.nal.usda.gov/fdc/v1/search'
req_str2 = 'https://api.nal.usda.gov/ndb/search/?'              # < -------- the one that works
API2 = 'Xcso2Fs6BTwI4pe5xIUXtM00ygqHq2UDq4hb4Qwv'               # < ------- -also the one that works

def request_get(api_key, endpoint, data):
    # concatinate the request
    #req_st = 'https://api_key=' + str(api_key) + str(endpoint)
    req_st = endpoint

    return requests.get(req_st, data)

# input: 
#   - search term: a string describing what's being searched
# output: 
#   - a json from USDA's sick API
def search_for_food(search_term, api_key=API2, sort='r'):

    # make the dictionary 
    search_dict = {
        "api_key":api_key,
        "q":search_term,
        "sort":sort
    }
    return request_get(api_key, req_str2, search_dict).json()


def get_calories_for_food(food_id, endpoint, api_key):

    # make the search dictionary 
    req_dict = {
        "api_key":api_key,
        "ndbno":food_id,
        "format":"json"
    }
    return request_get(api_key, endpoint, req_dict).json()

# try a few searches
js_res = search_for_food("raw potato")

# list the items, and store them 
item_ndbnos = {}
print("List: ----------------\n")
for item in js_res['list']['item']:
    #print("    ", item['name'], "\n             ----data source", item['ds'], '\n              ---NDB ID: ', item['ndbno'])
    item_ndbnos[item['name']] = item['ndbno']


# try and print detailed nutrition info for some item
for item in item_ndbnos.keys():
    # try and get the info for the ndbno id
    response = get_calories_for_food(item_ndbnos[item], req_str2, API2)
    print('For item: {} \n                 '.format(item))
    for key in response['list']['item']:
        print("--             ", key)
ENDPOINT2 = 'https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=Xcso2Fs6BTwI4pe5xIUXtM00ygqHq2UDq4hb4Qwv&location=Denver+CO'


# try and get this 
req_2 = ENDPOINT2
#print(requests.get(req_2).json())

#print(requests.get(req_str2, test_dict).json())


