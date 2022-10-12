import pyperclip
NotNow = ("hello there what are you doing my man do you really think that everyone is that stupid?, like if you think you are stupid then sure I know that you are stupid but please don't think we are the same as you you dumb fuck, so shut the fuck up man")
cat = {"fangs": "Sharp",
        "teeth":"yellow",
        "fur": "gray",
        "hair":"black"
        ,"eyes": "yellow"}

items = {"Laptop": 2, "Desktops": 1, "Phones": 4}
## Using the get method:
# print("We have " + str(items.get("TVs", "no")) + " TVs in our house")

##Using the setdefault method:
items.setdefault("TVs", 'one')
print("We have " + str(items["TVs"] + " TV in our house"))