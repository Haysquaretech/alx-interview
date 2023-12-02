#!/usr/bin/python3
"""
    this function returns a list of lists of integers
        representing the Pascal’s triangle of n:
            Returns an empty list if n <= 0
                You can assume n will be always an integer
                """


                def pascal_triangle(n):
                        """
                                checks for n value of < 0, 1 and 2 and returns directly
                                        starts from n value of 3 to generate the triangle lists
                                            """
                                                row = []

                                                    if n <= 0:
                                                                return row
                                                                elif n == 1:
                                                                            row = [[1]]
                                                                                    return row
                                                                                    elif n == 2:
                                                                                                row = [[1], [1, 1]]
                                                                                                        return row
                                                                                                        else:
                                                                                                                    row = [[1], [1, 1]]
                                                                                                                            temp = [0, 1, 1, 0]
                                                                                                                                    for x in range(2, n):
                                                                                                                                                    new = []
                                                                                                                                                                for y in range(x + 1):
                                                                                                                                                                                    a = temp[y] + temp[y + 1]
                                                                                                                                                                                                    new.append(a)
                                                                                                                                                                                                                row.append(new)
                                                                                                                                                                                                                            temp = [0, 0]
                                                                                                                                                                                                                                        for k in range(x + 1):
                                                                                                                                                                                                                                                            temp.insert((k + 1), new[k])
                                                                                                                                                                                                                                                                    return row
