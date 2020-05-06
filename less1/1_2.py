country = {
    "Ukraine": "Kyiv",
    "Belarus": "Minsk",
    "Poland": "Warsaw"
    }

country_extended = ["Ukraine", "Slovakia", "Hungary", "Poland"]

for i in country_extended:
    if i in country:
        print(country[i])
