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