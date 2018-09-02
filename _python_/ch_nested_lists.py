if __name__ == '__main__':
    x = []
    score_list = []
    final_list = []
    second_lowest_score = 0
    str = " "
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x.append([name, score])

    for i in range(len(x)):
        score_list.append(x[i][1])

    for j in range(len(score_list)):
        if score_list[j] > (min(score_list)):
            final_list.append(score_list[j])

    second_lowest_score = min(final_list)



    for index in range(len(x)):
        for i in range(len(x[index])):
            #for k in range(len(str)):
            #print(x[index][i])
            if x[index][i] == second_lowest_score:
                #print("if")
                str += x[index][i - 1]
    print(str)

    //ATTENTION FILTRE ALPHABETIC => créer autre liste ne contenant que les deux prénoms
    => sort cette liste
    => print les éléments de la liste
