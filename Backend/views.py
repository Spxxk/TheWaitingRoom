import os
from django.http import HttpResponse


def diagnosis(request):
    import random
    import pandas as pd

    file_path = './dataset.xlsx'
    df = pd.read_excel(file_path)
    questionnare = df.columns.to_list()[:-2]

    answer = {x: random.randint(0, 1) for x in questionnare[1:]}
    answer["ag+1:629e"] = 10

    def custom_calculation(row):
        # Example calculation: Let's say we calculate a score based on the length of the city name and age
        score = sum([abs(row[x] - answer[x]) for x in questionnare])
        return score

    df['CalculatedValue'] = df.apply(custom_calculation, axis=1)
    min_value = df['CalculatedValue'].min()
    min_value_rows = df[df['CalculatedValue'] == min_value]
    result = min_value_rows['Disorder'].to_list()

    count = {}
    for x in result:
        if x not in count:
            count[x] = 0
        count[x] += 1
    for x in count:
        count[x] = count[x] / len(result)

    return HttpResponse(str(count))
