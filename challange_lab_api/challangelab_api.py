#!/usr/bin/env python3

astro= {"number": 3, "message": "success", "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}]}

print("People in space:", astro["number"], "\n")
for x in astro["people"]:
    print(x["name"], "is on the", x["craft"])

#fprint
print(f"People in space: {astro['number']} \n")
for x in astro["people"]:
    print(f"{x['name']} is on the {x['craft']}")
