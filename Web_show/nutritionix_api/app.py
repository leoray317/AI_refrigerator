from usda import UsdaClient
import configparser

# read token
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = (config['USDA']['ACCESS_TOKEN'])
# input token
client = UsdaClient(TOKEN)

def search_nutrient(food_name):

     try:
          foods_search = client.search_foods(food_name,1)
          search_item = next(foods_search)
          report = client.get_food_report(search_item.id)
          result=dict()
          for nutrient in report.nutrients:
               result[nutrient.name] = str(nutrient.value) + str(nutrient.unit)
               
               #print(nutrient.name, nutrient.value, nutrient.unit)
               
               
          return result
     except:
          return "keyword error"

if __name__ == "__main__":
    a = search_nutrient("sweet potato")
    print(a)