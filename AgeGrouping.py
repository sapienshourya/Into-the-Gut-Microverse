import csv

def get_age_group(age):
    if age < 10:
        return '0-9'
    elif age < 20:
        return '10-19'
    elif age < 30:
        return '20-29'
    elif age < 40:
        return '30-39'
    elif age < 50:
        return '40-49'
    elif age < 60:
        return '50-59'
    elif age < 70:
        return '60-69'
    else:
        return '70+'

def convert_age_to_group(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)
        age_index = header.index('Age')
        header.remove('Age')
        header.append('Age Group')
        writer.writerow(header)
        for row in reader:
            try:
                age = float(row[age_index])
                age_group = get_age_group(age)
                del row[age_index]
                row.append(age_group)
                writer.writerow(row)
            except ValueError:
                print(f"Skipping row with non-numeric age in file {input_file}")
convert_age_to_group('/home/group16/MLBIO/Studies used/iHMP/iHMP_IBDMDB_2019/iHMP_4_columns.csv', 'iHMP_4_col_age_range.csv')

input_files = ['/home/group16/MLBIO/Studies used/iHMP/iHMP_IBDMDB_2019/iHMP_4_columns.csv', '/home/group16/MLBIO/Studies used/FRANZOSA/FRANZOSA_IBD_2019/Franzosa_4_columns.csv','/home/group16/MLBIO/Studies used/SINHA CRC/SINHA_CRC_2016/SINHA CRC_4_columns.csv','/home/group16/MLBIO/Studies used/YACHIDA CRC/YACHIDA_CRC_2019/YACHIDA CRC_4_columns.csv','/home/group16/MLBIO/Studies used/MARS IBS/MARS_IBS_2020/MARS IBS_4_columns.csv','/home/group16/MLBIO/Studies used/ERAWIJINTARI/ERAWIJANTARI_GASTRIC_CANCER_2020/Erawijintari_4_columns.csv']  # Add more filenames if needed
output_files = ['iHMP_4_col_age_range.csv', 'FRANZOSA_4_col_age_range.csv','SINHA_4_col_age_range.csv','YACHIDA_4_col_age_range.csv','MARS_4_col_age_range.csv','ERAWIJINTARI_4_col_age_range.csv']  # Make sure the order matches input_files

convert_age_to_group(input_files, output_files)
