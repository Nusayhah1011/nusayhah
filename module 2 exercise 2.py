# Create a dictionary representing a person
person = {"name": "Hurry Furry", "age": 30, "City": "Vacoas"}
#Access each value by key
print("name :",person["name"])
print("Age:", person["age"])   
print("City:", person["City"])
#Add a new key
person["Country"] = "Mauritius"
print("Country:", person["Country"])

# Try accessing a key that does not exist
#print(person["job"]) # This will cause an error

# Using .get() with a default value
country = person.get("Hobby", "Not specified")
print("Hobby:", country)