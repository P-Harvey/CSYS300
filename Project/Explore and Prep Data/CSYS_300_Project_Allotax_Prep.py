# CSYS 300 Working Project (Python Version)
# PATRICK HARVEY

import pickle

def prep_for_allotaxonometer():
    FEA_data = pickle.load(open('FEA_data.pkl', 'rb'))
    for key in FEA_data.keys():
        filename = "{}.txt".format(key)
        with open(filename, 'w') as f:
            line = FEA_data[key]
            for index, row in line.iterrows():
                fips = str(row['FIPS'])
                county = str(row['County'])
                state = str(row['State'])
                row_id = str((fips + ' ' + 
                              county + ' ' +
                              state))
                row_val = str(row['Value'])
                out_line = str((row_id + ',' + 
                                row_val + '\n'))
                f.write(out_line)