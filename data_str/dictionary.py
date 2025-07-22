person = {
    "name": "alice",
    "age": 30,
    "email": "alice@example.com"
}

print(person["name"])
person["age"] = 31
print(person.get("email"))

del person["email"]

person ["new eamil"] = "newalice@.com"

new_data = {"job": "Engineer", "age": 32}
person.update(new_data)  # adds 'job', updates 'age'
print(person)
