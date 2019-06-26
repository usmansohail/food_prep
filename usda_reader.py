import requests

# save the api key
API_KEY = 'PRlaNFB3LpWOn14ICWIqupBkZa4ZKKdSkvpDwIJC'
USDA_ENDPOINT = '@api.nal.usda.gov/fdc/v1/search'


def make_post(api_key, endpoint, d):
    # concatinate the request
    req_st = 'https://api_key=' + str(api_key) + str(endpoint)

    #print debug info
    print("request string: ", req_st)

    return requests.post(url=req_st, data = d)

def search_for_food(search_dict):
    return make_post(API_KEY, USDA_ENDPOINT, search_dict).json()


# do a test run
test_dict = {
        "api_key":API_KEY,
        "generalSearchInput":"Eggplant"
    }

print(search_for_food(test_dict))

