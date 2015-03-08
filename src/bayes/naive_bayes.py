#file_name = 'E:/NEIU/AI/haberman.csv'
file_name = input("Enter the location of the .csv file: ")
file = open(file_name, 'r')

age_dict_live = {'30_39':0, '40_44':0, '45_49':0, '50_54':0, '55_59':0, '60_64':0, '65_89':0}
year_dict_live = {'58_60':0, '61_63':0, '64_66':0, '67_69':0}
nodes_dict_live = {'0':0, '1':0, '2_3':0, '4_9':0, '10_52':0}
age_dict_die = {'30_39':0, '40_44':0, '45_49':0, '50_54':0, '55_59':0, '60_64':0, '65_89':0}
year_dict_die = {'58_60':0, '61_63':0, '64_66':0, '67_69':0}
nodes_dict_die = {'0':0, '1':0, '2_3':0, '4_9':0, '10_52':0}
count_live = 0
count_die = 0
count_entries = 0

    
def categorize_age(num):
    age = int(num)
    if age>=30 and age<=39:
        return '30_39'
    elif age>=40 and age<=44:
        return '40_44'
    elif age>=45 and age<=49:
        return '45_49'
    elif age>=50 and age<=54:
        return '50_54'
    elif age>=55 and age<=59:
        return '55_59'
    elif age>=60 and age<=64:
        return '60_64' 
    elif age>=65 and age<=89:
        return '65_89'

def categorize_year(num):
    year = int(num)
    if year>=58 and year<=60:
        return '58_60'
    elif year>=60 and year<=63:
        return '61_63'
    elif year>=64 and year<=66:
        return '64_66'
    elif year>=67 and year<=69:
        return '67_69'
    
def categorize_nodes(num):
    nodes = int(num)
    if nodes == 0:
        return '0'
    elif nodes == 1:
        return '1'
    elif nodes == 2 or nodes == 3:
        return '2_3'
    elif nodes>=4 and nodes<=9:
        return '4_9';
    elif nodes>=10 and nodes<=52:
        return '10_52'
    
def likelihood_live(age, year, nodes):
    prob_live = count_live/count_entries
    prob_age = age_dict_live[age]/count_live
    prob_year = year_dict_live[year]/count_live
    prob_nodes = nodes_dict_live[nodes]/count_live
    return round((prob_live * prob_age * prob_year * prob_nodes), 8)

def likelihood_die(age, year, nodes):
    prob_die = count_die/count_entries
    prob_age = age_dict_die[age]/count_die
    prob_year = year_dict_die[year]/count_die
    prob_nodes = nodes_dict_die[nodes]/count_die
    return round((prob_die * prob_age * prob_year * prob_nodes), 8)


        
for line in file:
    entry = line.split(',')
    age = categorize_age(entry[0])
    year = categorize_year(entry[1])
    nodes = categorize_nodes(entry[2])
    if (int(entry[3]) == 1):
        count_live += 1
        age_dict_live[age] += 1
        year_dict_live[year] += 1
        nodes_dict_live[nodes] += 1
    else:
        count_die += 1
        age_dict_die[age] += 1
        year_dict_die[year] += 1
        nodes_dict_die[nodes] += 1
    count_entries += 1

  
age_input = input("Enter patient's age at time of surgery (30 - 89) ")
age_input = categorize_age(age_input)
year_input = input("Enter last two digits of the year the surgery took place (1958 - 1969): 19")
year_input = categorize_year(year_input)
nodes_input = input("Enter number of axillary nodes (0 - 52) ")
nodes_input = categorize_nodes(nodes_input)
live = likelihood_live(age_input, year_input, nodes_input)
die = likelihood_die(age_input, year_input, nodes_input)
if (live > die):
    print ("The patient is likely to live past five years")
else:
    print ("The patient is likely to die within five years")
    



