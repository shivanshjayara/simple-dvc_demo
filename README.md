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

''' bash
    create stage-1: load_data
'''


'''bash
dvc repro. This will create dvc.lock file which will be having all the dependencies which we have tracked in a code.
No wif we ru it again, it shows that nothing has changes so it is skipping this step.
Now to se ehwo it affects the changes, lets comment out some where. Then if we run dvc repro command then it will sends those changes and it will run the same command. In this way this works.
It takes the stages from the dvc.lock file where all the dependencies are stored. It contains the size of the data or whatever things are stored there and it will track the size. So bascially if there is any changes occur in it it will change the md file and it will reproduce that change to the entrie process. 
In simple terms, dvc repro will go to the oarams.yaml file and check the stages. Whatever the changes has occurred in any of the dependencies, it will reproduce those into entire process.  
''' 


'''bash
created split.py file
'''


''' bash
    create stage-2: split_data
'''


'''bash
update the dvc.yaml file with all the depedencies and outputs location
'''

''' bash
run command dvc.repro
'''

''' bash
    To track the changes with git, run:

        git add dvc.lock 'data\processed\.gitignore'
    Use `dvc push` to send your updates to remote storage.
'''

''' bash
whene ever we run dvc.repro command, it will go and check dvc.yaml file and it will the stages mention in that file like what command are in the load_data and split_data ike dependencies and output location ,etc.
It will always run if there is any change in the respective dependencies else it will skip this step.
'''


''' bash
    train_and_evaluate.py file created
'''


''' bash
    updated the dvc.yaml file with stage 3 i.e. train_and_evaluate
'''


''' bash
    run dvc repro. New stage will added into dvc.lock file.
'''


''' bash
    create another folder named report where all the parameters and score of metrices will be saved in the form of json structure
'''


''' bash
    now nothing we have to do by our own. All this saving of parameters and score will be taken care and done by dvc.yaml file. Only thing which we have to do is, we need to add extra or call the metrics in dvc.yaml file i.e. we have to update one more parametrs in dvc.yaml file which is metrics section.
    We will also do some addition in train_and_evaluate.py file. We just need to add those metrics score file which we will be creating in report folder
'''


''' bash
    for above we have to specify the path for above files in params.yaml file also.
'''


''' bash
    dvc metrics show: This command will show the value sof all the mentioned metrics
    dvc metrics diff: This command wil show the old and new values and the changed in the values
'''


''' bash
    just for experiment purpose, we can change the paramaters values of alpha and l1_ration in params.yaml file.
    Then run the command "dvc metrics diff" to check the difference/change. This will show the difference between the previous values and current values
'''


''' bash
    Later on if again we run dvc metrics diff: Then it will not show any changes because now there is no changes done.
'''

''' BASIC CODING IS DONE. NOW TESTING PART WILL START.
    INSTALL pytest, tox
    
    tox: creates a virtual env. We can specifi for all version of python like py27 or py36
    deps = pytest
    commands = [Note: we can un any commands here not only tests]
    pytest

Note 2: To run above we need to install tox.in file in our root directory. 
'''




