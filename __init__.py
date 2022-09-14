article = '''This is a photograph of our village.
Our village is in a valley.
It is between two hills.
The village is on a river.
Here is another photograph of the village.
My wife and I are walking along the banks of the river.
We are on the left.
There is a boy in the water.
He is swimming across the river.
Here is another photograph.
This is the school building.
It is beside a park.
The park is on the right.
Some children are coming out of the building.
Some of them are going into the park.
'''

new_words = [
    'photograph',
    'village',
    'valley',
    'between',
    'hills',
    'another',
    'prep',
    'wife',
    'along',
    'banks',
    'water',
    'swimming',
    'building',
    'park',
    'into'
]


def get_word_count(article):
    word_count = {}
    word_list = article.lower().replace('.', '').split()

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def get_difficulty(word_count, new_words):
    difficulty = 0

    for word in new_words:
        if word in word_count:
            difficulty += 5 * word_count[word]

    return difficulty


word_count = get_word_count(article)
difficulty = get_difficulty(word_count, new_words)
print(difficulty)