# CS-4400---2019-Spring

## To work on the project, please set up your environment  with the following instruction  
1.install anaconda   
https://docs.anaconda.com/anaconda/install/  
2.create a python environment  
</p> conda create -n ENV_NAME python=3.5 </p>  
3.activate the python environment  
</p> source activate ENV_NAME </p>  
4.install mysql-connector  
</p> pip install mysql-connector-python </p>
5.install pyqt5
</p> pip install pyqt</p>  
6.set database connection
modify the variables in init.py file  
function *pooling.MySQLConnectionPool*  
set *host* , *user* , *password*, *database* used to connect your local database  

**as the password in the example data is not hashed,** you need to run </p> pyhton clean_pwd.py </p> to make the stored password hashed if you want to use example data

## everytime to test the project ##  
activate your conda environment  
</p>source activate ENV_NAME </p>  
run init.py file  
</p>python init.py</p>


## Error ##
1. Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'beltline_version2.connect.Name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

-mysql  SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

=======
change the user of the logging in info of mysql in initial.py/init.py 



