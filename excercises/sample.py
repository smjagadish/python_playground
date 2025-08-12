import json


def cmp(k):
    if k.startswith("n"):
        return True
    else:
        return False


json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
json_list = "[1,2,3]"
data = json.loads(json_string)
print(sorted(data, key=cmp))
print(data)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(json.loads(json_list))
es = set()
es.add(11)
es.add(12)
es.add(33)
es.add((4, 5))
#es.add([9, 8])
print(es)
tpl = ((1,2,3,4,5),(0,))
gb = (x for subtpl in tpl for x in subtpl if x >=0)
ltpl = tuple(gb)
print(ltpl)
filtered_tpl = tuple(tuple(x for x in subtuple if x >= 0) for subtuple in tpl)

print(filtered_tpl)

