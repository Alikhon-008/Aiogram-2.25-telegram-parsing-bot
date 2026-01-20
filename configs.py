
CATEGORIES = {
    'Iphone': "katalog/smartfony-apple/",
    'Tv': "katalog/televizor-samsung/",
    'Fridge': "katalog/holodilniki/",
    'Samsung': "katalog/smartfon-samsung/",
    'Washer': "katalog/stiralnaja-mashina/",
    'Laptop': "katalog/noutbuki-hp/"
}


def get_value(category):
    for key, value in CATEGORIES.items():
        if key == category:
            return value