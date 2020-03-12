"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import time

start_time = time.time()


def name_score(name):
    return sum([ord(c) - 96 for c in name])


filename = "names.txt"
with open(filename, 'r') as file:
    names = file.read().lower()
    names = names.replace("\"", "")
    names = names.split(",")
    names.sort()

    name_scores = []
    for name in names:
        name_scores.append(name_score(name))

    total_score = sum([score * (i + 1) for i, score in enumerate(name_scores)])

    print(total_score)

print("Took %s seconds to complete" % (time.time() - start_time))
