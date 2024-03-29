Vm requirements 

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

**To have this run if you close the SSh session you need to detach the terminal window by hitting Ctrl + A followed by D 


you can view the session with 
screen -ls


and reattach with screen -r  (this reattached the most recent session)


