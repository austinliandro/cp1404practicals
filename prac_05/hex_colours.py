COLOR_TO_CODE = {"Absolute Zero": '#0048ba', "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                 "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Army Green": "	#4b5320"}

for name_color in COLOR_TO_CODE:
    print(f"{name_color}")

name_color = input("Enter a color name: ").title()
while name_color != "":
    try:
        color_code = COLOR_TO_CODE[name_color]
        print(f"{name_color}:{color_code}")
    except KeyError:
        print("Invalid color name.")
    name_color = input("Enter a color name: ").title()