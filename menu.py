#import the required modules from sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setup import Biryani_restaruant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class 
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Menu for first one
restaurant_1 = Biryani_restaruant(name="Indian Dining")

session.add(restaurant_1)
session.commit()

menuItem2 = MenuItem(name="veggie samosa", description="Crispy fried buns stuffed with potatoes and veggies then deep-friedfried to perfection",
                     price="$3.50", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name="Pakora", description="Mild fresh Indian cheese cooked to perfection with such a potato and mint basil middle ",
                     price="$2.99", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Vegetarian Platter", description="2 vegetable samosas, batata vadas, and various vegetable pakoras were included in the sampler",
                     price="$5.50", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Gulab jamun", description="Round sweets made with milk, deep fried and marinated in sweet syrup",
                     price="$3.99", course="Dessert", restaurant=restaurant_1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Golden Veggie Biryani", description="Vegetable Biriyani Traditional Indian basmati rice with vegetables, golden raisins, and mixed nuts served with a side of raita",
                     price="$12.99", course="On Tray", restaurant=restaurant_1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Chicken Biryani", description="Traditional Indian basmati rice with chicken, golden raisins, and mixed nuts served with a side of raita",
                     price="$15.99", course="On Tray", restaurant=restaurant_1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Garlic Naan", description="Bread baked and topped with roasted garlic and cilantro.",
                     price="$.99", course="On TRay", restaurant=restaurant_1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Mongo ice cream", description="Ice cream with mango flavor",
                     price="$3.49", course="Dessert", restaurant=restaurant_1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="Prawn malai curry", description="Prawn served in a sweet coconut milk and saffron gravy.",
                     price="$14.99", course="Entree", restaurant=restaurant_1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Biryani_restaruant(name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="$7.99", course="Entree", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    name="Peking Duck", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="15", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant_1 = Biryani_restaruant(name="Panda Garden")

session.add(restaurant_1)
session.commit()


menuItem1 = MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="$8.99", course="Entree", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="$6.99", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     price="$9.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", course="Entree", restaurant=restaurant_1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="veggie samosa", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant_1 = Biryani_restaruant(name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant_1)
session.commit()


menuItem1 = MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="$2.99", course="Dessert", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     price="$4.50", course="Dessert", restaurant=restaurant_1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$6.95", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="$7.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(name="veggie samosa", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$6.80", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant_1 = Biryani_restaruant(name="Tony\'s Bistro ")

session.add(restaurant_1)
session.commit()


menuItem1 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="$13.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken and Rice", description="Chicken... and rice",
                     price="$4.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", course="Dessert", restaurant=restaurant_1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="$7.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant_1 = Biryani_restaruant(name="Andala\'s")

session.add(restaurant_1)
session.commit()


menuItem1 = MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="veggie samosa", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant_1 = Biryani_restaruant(name="Auntie Ann\'s Diner ")

session.add(restaurant_1)
session.commit()

menuItem9 = MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     price="$8.99", course="Entree", restaurant=restaurant_1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", course="Dessert", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     price="$7.50", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="veggie samosa", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", course="Dessert", restaurant=restaurant_1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant_1 = Biryani_restaruant(name="Cocina Y Amor ")

session.add(restaurant_1)
session.commit()


menuItem1 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                     price="$5.95", course="Entree", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", course="Entree", restaurant=restaurant_1)

session.add(menuItem2)
session.commit()


restaurant_1 = Biryani_restaruant(name="State Bird Provisions")
session.add(restaurant_1)
session.commit()

menuItem1 = MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="$5.95", course="Appetizer", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                     price="$6.95", course="Dessert", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     price="$4.25", course="Dessert", restaurant=restaurant_1)

session.add(menuItem1)
session.commit()


print ('added menu items')