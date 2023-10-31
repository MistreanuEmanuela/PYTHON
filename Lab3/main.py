# 1. Write a function that receives as parameters
# two lists a and b and returns a list of sets containing: ( aa intersected with b, a reunited with b, a - b, b - a)
print("--------------------------------------------1----------------------------------------------------------")


def operation(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersect = set_a.intersection(set_b)
    reunion = set_a.union(set_b)
    diff_ab = set_a.difference(set_b)
    diff_ba = set_b.difference(set_a)
    op_result = [intersect, reunion, diff_ab, diff_ba]
    return op_result


result = operation([1, 2, 3], [2, 3, 4, 5])
print(f"Intersection: {result[0]}, Reunion: {result[1]} Difference a-b: {result[2]}, difference b-a: {result[3]}")

print("--------------------------------------------2----------------------------------------------------------")


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given text.


def dictionary(string):
    dict_nr_app = {}
    for ch in string:
        if ch in dict_nr_app.keys():
            dict_nr_app[ch] = dict_nr_app[ch] + 1
        else:
            dict_nr_app[ch] = 1

    # sorted_dict_nr_app = sorted(dict_nr_app.items(), key=lambda element: element[1], reverse = True)
    return dict_nr_app


print(dictionary("Ana has apples."))

print("--------------------------------------------3----------------------------------------------------------")


# 3.Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively
# covered because they can contain other containers, such as dictionaries, lists, sets, etc.)


def compare_dictionary(dict1, dict2):
    if type(dict1) != type(dict2):
        return False
    for key in dict2.keys():
        if key not in dict1.keys():
            return False
    for key in dict1.keys():
        value1 = dict1[key]
        if key not in dict2.keys():
            return False
        value2 = dict2[key]
        if type(value1) != type(value2):
            return False
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dictionary(value1, value2):
                return False
        elif isinstance(value1, (list, set)) and isinstance(value2, (list, set)):
            if len(value1) != len(value2):
                return False
            else:
                for i in range(len(value1)):
                    if value1[i] != value2[i]:
                        return False
        else:
            if value1 != value2:
                return False

    return True


x1 = {"A": 1, "B": {"a": 2, "b": 4}, "C": (1, 2, 3)}
x2 = {"A": 1, "B": {"a": 2, "b": 4}, "C": (1, 2, 3)}
print(compare_dictionary(x1, x2))

print("--------------------------------------------4----------------------------------------------------------")


# 4.The build_xml_element function receives the following parameters: tag,
# content, and key-value elements given as name-parameters. Build and return a string
# that represents the corresponding XML element. Example: build_xml_element ("a", "Hello there",
# href =" http://python.org ", _class =" my-link ", id= " someid ")
# returns the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "


def build_xml_element(tag, content, **arguments):
    tagg = f"<{tag} "
    for key, value in arguments.items():
        tagg += f'{key} = "{value}\ "'
    tagg += f'>'
    end = f'</{tag}>'
    return f'"{tagg} {content} {end}"'


print(build_xml_element("a", "Hello there", href="http://python.org ", _class=" my-link ", id=" someid "))
print("--------------------------------------------5----------------------------------------------------------")


# 5. The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix",
# "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules,
# False otherwise. Example: the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
# => False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.


def validate_dict(rules_set, dictionary_test):
    for key in dictionary_test.keys():
        con = 0
        for item in rules_set:
            if key == item[0]:
                con = 1
        if con == 0:
            return False

    for item in rules_set:
        if item[0] in dictionary_test:
            value = dictionary_test[item[0]]
            prefix, middle, suffix = item[1], item[2], item[3]

            if prefix and not value.startswith(prefix):
                return False
            if middle and middle not in value[1:-1]:
                return False
            if suffix and not value.endswith(suffix):
                return False
            if prefix == suffix == value:
                return False
    return True


print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                    {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
print(validate_dict({("key1", "start", "", "start")},
                    {"key1": "start"}))
print("--------------------------------------------6----------------------------------------------------------")


# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list,
# and b representing the number of duplicate elements in the list (use sets to achieve this objective).

def number_of_unique(list_input):
    unique_elements = set(list_input)
    a = len(unique_elements)
    b = len(list_input) - a
    nr_unique = a - b
    return nr_unique, b


print(number_of_unique([1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8]))


print("--------------------------------------------7----------------------------------------------------------")


# Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "aa op b",
# where a and b are two sets, and op is the applied operator: |, &, -. Ex:


def operation_between_sets(*argv_set):
    dictionary_operation_beetwen_sets = {}
    if len(argv_set) < 2:
        return "Nu putem aplica aceasta functie pe un numar asa mic de instante"
    for i in range(len(argv_set)-1):
        for j in range(i + 1, len(argv_set)):
            key = str(argv_set[i]) + " | " + str(argv_set[j])
            if key not in dictionary_operation_beetwen_sets.keys():
                dictionary_operation_beetwen_sets[key] = argv_set[i].union(argv_set[j])
            key2 = str(argv_set[i]) + " & " + str(argv_set[j])
            if key2 not in dictionary_operation_beetwen_sets.keys():
                dictionary_operation_beetwen_sets[key2] = argv_set[i].intersection(argv_set[j])
            key3 = str(argv_set[i]) + " - " + str(argv_set[j])
            if key3 not in dictionary_operation_beetwen_sets.keys():
                dictionary_operation_beetwen_sets[key3] = argv_set[i].difference(argv_set[j])
            key4 = str(argv_set[j]) + " - " + str(argv_set[i])
            if key4 not in dictionary_operation_beetwen_sets.keys():
                dictionary_operation_beetwen_sets[key4] = argv_set[j].difference(argv_set[i])
    return dictionary_operation_beetwen_sets


print(operation_between_sets({1, 2}, {2, 3}))


print("--------------------------------------------8----------------------------------------------------------")
# Write a function that receives a single dict parameter named mapping.
# This dictionary always contains a string key "start".
# Starting with the value of this key you must obtain a list of objects
# by iterating over mapping in the following way: the value of the current key is
# the key for the next value, until you find
# a loop (a key that was visited before). The function must return the
# list of objects obtained as previously described. Ex:


def loop(mapping):
    vizited_key = []
    key = "start"
    new_key = mapping[key]
    vizited_key.append(new_key)
    while mapping[new_key] not in vizited_key:
        vizited_key.append(mapping[new_key])
        new_key = mapping[new_key]
    return vizited_key


print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


print("--------------------------------------------9----------------------------------------------------------")

# Write a function that receives a variable number of positional
# arguments and a variable number of keyword arguments adn will return
# the number of positional arguments whose values can be found among keyword arguments values. Ex:


def ex9(*positional_args, **keyword_args):
    positional_set = set(positional_args)
    keyword_set = set(keyword_args.values())
    matching = positional_set.intersection(keyword_set)
    return len(matching)


print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
