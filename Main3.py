# Exercice 1
string_variable = "MESSI est le meilleur joueur du monde "
# Upper_case = string_variable.upper()
# print(Upper_case)
lower_case = string_variable.lower()
# print(lower_case)
Capitalize_sentence = string_variable.title()
# print(Capitalize_sentence)
new_sentence = string_variable.replace("MESSI", "ronaldo")
# print(new_sentence)
words_list = string_variable.split()
# print(words_list)
words_list = ["messi", "est", "le", "meilleur", "joueur"]
joined_sentence = "-".join(words_list)
# print(joined_sentence)
 
string_variable = ["  Messi est un grand joueur du barca  "]
# Donald = string_variable.index("du")
# print(Donald)
# start_with = string_variable.startswith("nyekesi")
# print(start_with)
facts = ["   Messi est un goat   "]
cleaning = facts[0].strip()
# print(cleaning)

# Exercice 2
name = "nduwimana"
age = 53
ville = "abuja"
full_sentence = "je m'appelle {}, j'ai {}, j'habite à {}".format(name, age, ville)
# print(full_sentence)
sentence = f"je m'appelle {name}, j'ai {age} ans, j'habite {ville}."
print(sentence)
