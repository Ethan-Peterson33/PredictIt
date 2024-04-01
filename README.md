Problem Statement: 
PredictIt show betting markets for current political races.  This project pulls the data from their API twice a day and dumps it in a Bigquery table where you can see the changes over time for each Market.  You can make whatever visualizations you want with Looker studio and switch between the markets to see the current data and how it has changed over time. With the timeseries visualizations you can see the trends or lack of trends between the contracts giving you a good idea of which candidate is predicted to win or which candidate you should to buy shares for to bet on.  This pipeline runs on the cloud with minimal setup and cost.   


Instructions:

from your local machine or where ever you have terraform installed

git clone https://github.com/Ethan-Peterson33/PredictIt.git

cd into terraform
mkdir keys
add your key file in this my_creds.json
update the variables file with your projectid

terraform init
terraform apply

create a vm on your project
Vm requirements:
  - e2-micro
  - add your ssh Keys 

ssh into your VM


sudo apt install python3-venv &&
python3 -m venv myenv &&
source myenv/bin/activate &&
pip install google-cloud-storage &&
pip install google-cloud-bigquery &&
pip install git &&
pip install pandas &&
pip install db_dtypes


git clone https://github.com/Ethan-Peterson33/PredictIt.git

cd PredictIt 

mkdir keys
put service account keys in this folder 


Should be set up like this:

PredictIt
__app_files
__Keys
   __keys.json

In order to keep the script running in the vm while the terminal is closed you need to run to create screen session by using the command screen.

screen

then..

cd into app_files


run python main.py

**To have this run if you close the ssh session you need to detach the terminal window by hitting Ctrl + A followed by D 


you can view the session with 
screen -ls


and reattach with screen -r  (this reattached the most recent session)



Dashboard:

Looker Studio
Make new Dataset based on markets_contracts table. 
See example below for the dashboard to display data. 
https://lookerstudio.google.com/reporting/029ccbe0-50d7-4a63-94bd-202c3af6e71e
- Remove Record count from base module. 
- Add Pie Chart
  - dimension contract_name
  - metric lascloseprice
- Time series
  - breakdown dimension - contract_name
  - metric lascloseprice
- Drag contract_image onto dashboard(make sure you have this field set to the image subtype for the url datatype


