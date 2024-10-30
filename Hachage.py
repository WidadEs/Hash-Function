import time


def custom_hash_function(input_string):
    hash_value = 0
    prime = 31  # Un nombre premier utilisé pour une distribution plus uniforme
    print(f"Calcul du hachage pour la chaîne : '{input_string}'")

    for index, char in enumerate(input_string):
        char_value = ord(char)
        print(f"Caractère '{char}' (ASCII: {char_value}) à l'index {index}")

        # Calcul intermédiaire pour chaque caractère
        intermediate_value = hash_value * prime
        print(f"Valeur intermédiaire après multiplication par {prime}: {intermediate_value}")

        # Ajout de la contribution du caractère actuel
        hash_value = (intermediate_value + char_value * (index + 1)) % (2 ** 32)
        print(f"Valeur de hachage après ajout du caractère: {hash_value}\n")

        # Pause pour ralentir l'exécution
        time.sleep(0.5)

    print(f"Valeur de hachage finale pour '{input_string}': {hash_value}\n")
    return hash_value


# Quelques exemples d'utilisation
strings_to_test = ["Hello", "hello", "HELLO", "World", "world"]
hashed_values = {string: custom_hash_function(string) for string in strings_to_test}

# Affichage des valeurs de hachage obtenues
for string, hashed_value in hashed_values.items():
    print(f"String: {string} => Hash: {hashed_value}")

