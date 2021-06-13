# for each of the file name t1 under python/
#   for each of the question title t2 of response.json
#     if t1 matches t2:
#       rename t1 to be t2

import json
import os


def get_filename(stat):
    question_id = stat['frontend_question_id']
    question_title = stat['question__title_slug']
    return f"{question_id}.{question_title}.py"


def match(f1, f2):
    i = j = 0
    while i < len(f1) and j < len(f2):
        if f1[i] == ' ':
            i += 1
            continue
        if f2[j] == ' ':
            j += 1
            continue
        if f1[i].lower() != f2[j].lower():
            return False
        i += 1
        j += 1
    while i < len(f1) and f1[i] == ' ':
        i += 1

    while j < len(f2) and f2[j] == ' ':
        j += 1

    return i == len(f1) and j == len(f2)


if __name__ == '__main__':
    PYTHON_DIR = '../python/'
    API_PROBLEMS_ALL = 'response.json'

    with open(API_PROBLEMS_ALL) as f:
        response = json.loads(f.read())
        stats = [kv['stat'] for kv in response['stat_status_pairs']]
    filenames = os.listdir(PYTHON_DIR)
    filenames_no_match = []
    for filename in filenames:
        print(filename)
        found = False
        for stat in stats:
            if filename == get_filename(stat):
                found = True
                break
            if match(os.path.splitext(filename)[0], stat['question__title']):
                print(f"{filename} -> {get_filename(stat)}")
                os.rename(PYTHON_DIR+filename, PYTHON_DIR+get_filename(stat))
                found = True
                break
        if not found:
            filenames_no_match.append(filename)
            print(f"no match for {filename}")
    print(filenames_no_match)
