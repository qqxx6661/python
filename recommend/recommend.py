# -*- coding: utf-8 -*-
import math

def load_matrix():
    matrix = {}
    f = open("train.csv")
    columns = f.readline().split(',')

    for line in f:
        scores = line.split(',')
    for i in range(len(scores))[1:]:
        matrix[(scores[0], columns[i])] = scores[i].strip("\n")

    return matrix
   
matrix = load_matrix()  
print "matrix:", matrix


def sim_distance(matrix, row1, row2):
    columns = set(map(lambda l: l[1], matrix.keys()))
    si = filter(
        lambda l: matrix.has_key((row1, l)) and matrix[(row1, l)] != "" and matrix.has_key((row2, l)) and matrix[(row2, l)] != "", columns)
    if len(si) == 0:
        return 0
    sum_of_distance = sum([pow(float(matrix[(row1, column)]) - float(matrix[(row2, column)]), 2) for column in si])
    return 1 / (1 + math.sqrt(sum_of_distance))


print sim_distance(matrix, "Kai Zhou", "Shuai Ge")


def top_matches(matrix, row, similarity=sim_distance):
    rows = set(map(lambda l: l[0], matrix.keys()))
    scores = [(similarity(matrix, row, r), r) for r in rows if r != row]
    scores.sort()
    scores.reverse()
    return scores


person = "Kai Zhou"
print "top match for:", person
print top_matches(matrix, person)


def transform(matrix):
    rows = set(map(lambda l: l[0], matrix.keys()))
    columns = set(map(lambda l: l[1], matrix.keys()))
    transform_matrix = {}
    for row in rows:
        for column in columns:
            transform_matrix[(column, row)] = matrix[(row, column)]
    return transform_matrix


trans_matrix = transform(matrix)
print "trans:", trans_matrix

film = "Friends"
print "top match for:", film
print top_matches(trans_matrix, film)


def get_recommendations(matrix, row, similarity=sim_distance):
    rows = set(map(lambda l: l[0], matrix.keys()))
    columns = set(map(lambda l: l[1], matrix.keys()))

    sum_of_column_sim = {}
    sum_of_column = {}

    for r in rows:
        if r == row: continue
        sim = similarity(matrix, row, r)
        if sim <= 0:  continue

        for c in columns:
            if matrix[(r, c)] == "": continue

            sum_of_column_sim.setdefault(c, 0)
            sum_of_column_sim[c] += sim
            sum_of_column.setdefault(c, 0)
            sum_of_column[c] += float(matrix[(r, c)]) * sim

    scores = [(sum_of_column[c] / sum_of_column_sim[c], c) for c in sum_of_column]
    scores.sort()
    scores.reverse()
    return scores


print get_recommendations(matrix, person)

# trans_matrix = transform(matrix)
# print get_recommendations(trans_matrix,  "Friends")