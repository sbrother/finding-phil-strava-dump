import os
from glob import glob
import subprocess
from gpx_converter import Converter


RAW_ACTIVITIES_DIR = 'activities/raw'


def convert_all_fit_to_gpx():
    for activity in glob(os.path.join(RAW_ACTIVITIES_DIR, '*.fit')):
        new_name = os.path.splitext(activity)[0] + '.gpx'
        subprocess.call(['fitdump', '-t', 'gpx', '-o', new_name, activity])

def convert_all_gpx_to_csv():
    for activity in glob(os.path.join(RAW_ACTIVITIES_DIR, '*.gpx')):
        new_name = os.path.splitext(activity)[0] + '.csv'
        try:
            Converter(input_file=activity).gpx_to_csv(output_file=new_name)
        except:
            print("Failed:", activity)


if __name__ == '__main__':
    convert_all_fit_to_gpx()
    convert_all_gpx_to_csv()
