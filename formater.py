
from param_wrapper import TranspTaskInfo

class Formater:
    '''
    A set of static methods that print predefined messages and formats of the output.
    '''

    @staticmethod
    def notBalanced() -> str:
        return "The problem is not balanced!"

    @staticmethod
    def notApplicable() -> str: 
        return "The method is not applicable!"

    @staticmethod
    def getTable(matrix: list[list[int]], supply = [], demand = []) -> str:
        '''
        Returns formated matrix with sources and destinations. Optionally adds supplies and demands.
        '''
        n = len(matrix)
        m = len(matrix[0])

        formatted_row = '|' + '{:>4} |' *  (m + 1 + int(len(supply) != 0))
        
        arr = [""]
        arr += ["D" + str(i) for i in range(m)]
        #Optional parameter
        if len(supply) != 0:
            arr.append("Sup")


        initial_row = formatted_row.format(*arr)  + "\n"
        num_of_dashes= len(initial_row) - 1

        table = "-" * num_of_dashes + "\n"
        table += initial_row
        for i in range(2 * n + 1):
            if i % 2 == 0:
                table += "-" * num_of_dashes
            else:
                row = i // 2
                arr = ["S" + str(row)] 
                arr += [str(matrix[row][col]) for col in range(m)]

                #Optional parameter
                if len(supply) != 0:
                    arr.append(str(supply[row])) 


                table += formatted_row.format(*arr)
            table += "\n"

        #Optional parameter
        if len(demand) != 0:
            arr = ["Dem"]
            arr += [str(demand[col]) for col in range(m)]
            arr.append("")
            table += formatted_row.format(*arr) + "\n"
            table += "-" * num_of_dashes

        return table

    @staticmethod
    def originalParameterTable(given_parameters: TranspTaskInfo) -> str:
        '''
        Returns cost matrix, supply vector and demand vector formated as a table.
        '''
        costs, supply, demand, _, _ = given_parameters.unpack()
        return Formater.getTable(costs, supply, demand)

    @staticmethod
    def solutionMatrix(matrix: list[list[int]]) -> str:
        '''
        Returns a formated table with sorces, destinations and number of products between them.
        '''
        return Formater.getTable(matrix)
