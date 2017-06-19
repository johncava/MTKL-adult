
##
# Loader for the Adult dataset from UCI Database
##
workclass = {'Private' : 0.0, 'Self-emp-not-inc' : 1.0, 'Self-emp-inc': 2.0, 'Federal-gov': 3.0, 'Local-gov': 4.0, 'State-gov': 5.0, 'Without-pay': 6.0, 'Never-worked': 7.0}
education = {'Bachelors' : 0.0, 'Some-college' : 1.0, '11th': 2.0, 'HS-grad': 3.0, 'Prof-school': 4.0, 'Assoc-acdm': 5.0, 'Assoc-voc': 6.0, '9th': 7.0, '7th-8th': 8.0, '12th': 9.0, 'Masters': 10.0, '1st-4th': 11.0, '10th': 12.0, 'Doctorate': 13.0, '5th-6th': 14.0, 'Preschool': 15.0}
marital = {'Married-civ-spouse' : 0.0, 'Divorced': 1.0, 'Never-married' : 2.0, 'Separated' : 3.0, 'Widowed' : 4.0, 'Married-spouse-absent' : 5.0, 'Married-AF-spouse' : 6.0}
occupation = {'Tech-support' : 0.0, 'Craft-repair' : 1.0, 'Other-service' : 2.0, 'Sales' : 3.0, 'Exec-managerial' : 4.0, 'Prof-specialty' : 5.0, 'Handlers-cleaners' : 6.0, 'Machine-op-inspct' : 7.0, 'Adm-clerical' : 8.0, 'Farming-fishing' : 9.0, 'Transport-moving' : 10.0, 'Priv-house-serv' : 11.0, 'Protective-serv' : 12.0, 'Armed-Forces' : 13.0}
relationship = {'Wife' : 0.0, 'Own-child' : 1.0, 'Husband' : 2.0, 'Not-in-family' : 3.0, 'Other-relative' : 4.0, 'Unmarried' : 5.0}
race = {'White' : 0.0, 'Asian-Pac-Islander' : 1.0, 'Amer-Indian-Eskimo' : 2.0, 'Other' : 3.0, 'Black' : 4.0}
sex = { 'Male' : 0.0, 'Female' : 1.0 } 
country = {'United-States' : 0.0, 'Cambodia': 1.0, 'England':2.0, 'Puerto-Rico': 3.0, 'Canada':4.0, 'Germany': 5.0, 'Outlying-US(Guam-USVI-etc)': 6.0, 'India': 7.0, 'Japan': 8.0, 'Greece' : 9.0, 'South' : 10.0, 'China' : 11.0, 'Cuba' : 12.0, 'Iran' : 13.0, 'Honduras' : 14.0, 'Philippines' : 15.0, 'Italy' : 16.0, 'Poland' : 17.0, 'Jamaica' : 18.0, 'Vietnam' : 19.0, 'Mexico' : 20.0, 'Portugal' : 21.0, 'Ireland' : 22.0, 'France' : 23.0, 'Dominican-Republic' : 24.0, 'Laos' : 25.0, 'Ecuador' : 26.0, 'Taiwan' : 27.0, 'Haiti' : 28.0, 'Columbia' : 29.0, 'Hungary' : 30.0, 'Guatemala' : 40.0, 'Nicaragua' : 41.0, 'Scotland' : 42.0, 'Thailand': 43.0, 'Yugoslavia' : 44.0, 'El-Salvador' : 45.0, 'Trinadad&Tobago' : 46.0, 'Peru' : 47.0, 'Hong' : 48.0, 'Holand-Netherlands' : 49.0}
salary = {'>50K': 0.0, '<=50K': 1.0}

def load():
    data = []
    line = []
    num = 0
    with open('adult.data') as file:
        for item in file:
            num = num + 1
            line = item.split(',')
            for index, column in enumerate(line):
                column = column.strip()
                if column == '?':
                    column = -1.0
                    line[index] = column
                    continue
                if index == 0:
                    column = float(column)
                if index == 1:
                    column = float(workclass[column])
                if index == 2:
                    column = float(column)
                if index == 3:
                    column = float(education[column])
                if index == 4:
                    column = float(column)
                if index == 5: 
                    column = float(marital[column])
                if index == 6:
                    column = float(occupation[column])
                if index == 7:
                    column = float(relationship[column])
                if index == 8:
                    column = float(race[column])
                if index == 9:
                    column = float(sex[column])
                if index == 10:
                    column = float(column)
                if index == 11:
                    column = float(column)
                if index == 12:
                    column = float(column)
                if index == 13:
                    column = float(country[column])
                if index == 14:
                    column = float(salary[column])
                line[index] = column
            data.append(line)
            if num == 100:
                break
    return data