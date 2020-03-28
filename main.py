years=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
columns = ['Years'] + ['MaleName','MaleCount','FemaleName','FemaleCount'] * 100
female_result=[]
male_result=[]
with open('result.csv', 'w+') as result:
    result.write(','.join(columns)+'\n')
    for i in range(len(years)):
        files = open('./data/yob'+years[i]+'.txt', 'r')
        result.write(years[i] + ',')
        for line in files:
            line = line.rstrip().split(",")
            if len(female_result) >= 100 and len(male_result) >= 100:
                break
            else:
                if line[1]=='F':
                    female_result.append(','.join([line[0], line[2]]))
                elif line[1]=='M':
                    male_result.append(','.join([line[0], line[2]]))

        for j in range(100):
            result.write(','.join([male_result[j], female_result[j]]) + ',')
        result.write('\n')
        female_result=[]
        male_result=[]