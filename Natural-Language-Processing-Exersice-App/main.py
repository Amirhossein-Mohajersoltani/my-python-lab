from sheety import Sheety
from nutritionix import Nutritionix
from ui import UserInterface

# Nutritionix api for language processing
nutrition = Nutritionix()

# sheety api
sheety = Sheety()

# UI
ui = UserInterface(nutrition, sheety)