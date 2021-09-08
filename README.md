''> 
create env
'''

'''bash
conda create -n wineq python==3.7 -y
'''

'''bash
conda activate wineq
'''

'''bash
created requirements.txt file
'''

'''bash
installed the requirements.txt
'''

'''bash
pip install -r requirements.txt
'''

'''bash
download the data set and saved to data_given folder. Google drive link.
https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec
'''

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
(afetr doing any updation further, please push it to the origin like: git push origin main.
If not then do this: git push origin main  --force  )
'''

'''bash
    git remote add origin http://github.com/shivanshjayara/sample-dvc_demo.git
'''

'''bash
    git branch -M main
'''

'''bash
git push origin main
'''

'''bash
dvc repro. This will create dvc.lock file which will be having all the dependencies which we have tracked in a code.
No wif we ru it again, it shows that nothing has changes so it is skipping this step.
Now to se ehwo it affects the changes, lets comment out some where. Then if we run dvc repro command then it will sends those changes and it will run the same command. In this way this works.
It takes the stages from the dvc.lock file where all the dependencies are stored. It contains the size of the data or whatever things are stored there and it will track the size. So bascially if there is any changes occur in it it will change the md file and it will reproduce that change to the entrie process. 

In simple terms, dvc repro will go to the oarams.yaml file and check the stages. Whatever the changes has occurred in any of the dependencies, it will reproduce those into entire process.  
''' 
