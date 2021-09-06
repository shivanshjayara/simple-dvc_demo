create env


'''bash
conda create -n wineq python==3.7 -y
'''
conda activate wineq

created requirements.txt file

installed the requirements.txt
'''bash
pip install -r requirements.txt
'''

download the data set and saved to data_given folder. Google drive link.
https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec

git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"

'''
git add . && git commit -m "update Readme.md" this is for commiting all the changes in this file at once
'''