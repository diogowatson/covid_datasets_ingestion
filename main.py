import pandas as pd
import os, sys
from api_urls import canada_covid_public_api_address
from datasets import data_response_for_covid_public_api
from extract_api import extract_api
from datetime import datetime
from argument_parser import create_argument_parser

parser = create_argument_parser()
args = parser.parse_args()

extracted_data = extract_api(canada_covid_public_api_address)

# extract desired data from response json
for att in extracted_data['features']:
    for key, value in att['attributes'].items():
        data_response_for_covid_public_api[key].append(value)
df = pd.DataFrame.from_dict(data_response_for_covid_public_api)

# create temp directory to save files
current_path = os.getcwd()
path = current_path + "//temp_storage"
try:
    os.mkdir(current_path + "/temp_storage")
except OSError:
    print("directory not created.")
else:
    print("directory created")

# save dataframe as csv file

now = datetime.now()
current_time = current_time = now.strftime("%d_%m_%Y")
filename = "canada_covid_provincial_data_" + current_time + ".csv"
save_path = path + "/" + filename
df.to_csv(save_path)

# check if path to GCP bucket exist. If exists save the files in the bucket
if args.bucket is None and args.cloud is None:
    print("No buckets to save")
    print("data is saved at ", save_path)
    sys.exit()

cloud_option = str(args.cloud).lower()
bucket_path = "gs://" + str(args.bucket).lower()
print(cloud_option)
if cloud_option == "gcp" or cloud_option == "google":
    if args.bucket is not None:
        print("copying files into bucket " + str(args.bucket))
        try:
            os.system("gsutil cp " + path + "/*.* " + bucket_path)
            print("file copied")
        except Exception as e:
            print(e)
    else:
        print("Bucket path can't be empty")
