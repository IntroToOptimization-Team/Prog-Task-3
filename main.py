import os
from transp_problem import Formater, NorthWestMethod, VogelMethod, RusselMethod, TranspTaskInfo, transportationTask

test_folder_path = os.getcwd()+"/tests"
for filename in sorted(os.listdir(test_folder_path)):
    if not filename.startswith("test_"): continue

    with open(os.path.join(test_folder_path, filename), 'r') as file:
        #Parse input
        n, m = map(int, file.readline().strip().split())
        costs = []
        supply = list(map(int, file.readline().strip().split()))
        for i in range(n):
            arr = list(map(int, file.readline().strip().split()))
            costs.append(arr)

        demand = list(map(int, file.readline().strip().split()))


        methods = {"North-West Method" : NorthWestMethod(),
                   "Vogel's method" : VogelMethod(), 
                   "Russell's method" : RusselMethod()}


        #Format: 'name of the method' -> correct answer from the input of string type
        correct_ans = dict()
        # order: North-West, Vogel's, Russell's
        ans_list = list(file.readline().strip().split())
        for name in methods:
            correct_ans[name] = ans_list[0]
            ans_list.pop(0)


        print(filename)
        print("Initial matrix:")
        print(Formater.originalParameterTable(TranspTaskInfo(costs, supply, demand)))
        print()

        for name, method in methods.items():
            print(name)
            try:
                res_matrix = transportationTask(TranspTaskInfo(costs[:], supply[:], demand[:], [], []), method)
                total_cost = sum([
                    sum(res_matrix[row][col] * costs[row][col] for row in range(n) for col in range(m))
                ])

                if correct_ans[name] != str(total_cost):
                    raise Exception("Wrong answer: " + str(total_cost) +
                                    " Expected: " + str(correct_ans[name]))

                print("Total cost = " + str(total_cost))
                print("Solution matrix:")
                print(Formater.solutionMatrix(res_matrix))
            except Exception as e:
                print(str(e))

        print()
