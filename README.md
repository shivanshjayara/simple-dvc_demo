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

git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"