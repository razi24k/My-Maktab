from pprint import pprint
print("Enter a string: ")
raw_input = input()
raw_input += " " + input()
raw_input += " " + input()
words = raw_input.split(" ")
unique_words = set(words)
result_dict = {}
for i in unique_words:
    count_dict = dict()
    count_dict["count"] = words.count(i)
    result_dict[i] = count_dict

pprint(result_dict)