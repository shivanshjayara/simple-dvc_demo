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

'''bash
git init
'''

'''bash
    dvc init
'''

'''bash
    dvc add data_given/winequality.csv
'''

'''bash
    git add .
'''

'''bash
    git commit -m "first commit"
'''

'''bash
    git add . && git commit -m "update Readme.md" this is for commiting all the changes in this file at once
    (afetr doing any updation further, please push it to the origin like: git push origin main)
'''

'''bash
    git remote add origin http://github.com/shivanshjayara/sample-dvc_demo.git
'''

'''bash
    git branch -M main
'''bash

'''bash
    git push origin main
'''bash