
# This program reads the data from the states tsv file

#     Each line has the state name, abbreviation, postal code, area and population.

# It stores the items in each line in a dictionary whose keys represent the column names.

#     It print the state name, abbreviation and population for each state.


import csv

infile = 'states_data.tsv'


# create new empty list

statesList = []

with open(infile, 'rU') as csvfile:

    # the csv file reader returns a list of the csv items on each line

    stateReader = csv.reader(csvfile,  dialect='excel', delimiter='\t')


    # from each line, a list of row items, put each element in a dictionary

    #   with a key representing the data

    for line in stateReader:

      # skip lines without data, specific for each file to catch non-data lines

      if line[0] == '' or line[0].startswith('Data') or line[0].startswith('*'):

          continue

      else:

          # create a dictionary for each state

          state = {}

          # add each piece of data under a key representing that column data

          state['name'] = line[0]

          state['abbrev'] = line[1]

          state['code'] = line[2]

          state['area'] = int(line[3].replace(',',''))

          state['pop'] = int(line[4].replace(',',''))

  
          # add this state to the list

          statesList.append(state)

    
csvfile.close()


print ("Read", len(statesList), "state data")


# print a few fields from all of the states read from the file


for state in statesList:

    print ('State:', state['name'], ' Abrv: ', state['abbrev'], ' Population: ', state['pop'])

