## - Created by Chris Ng 20201215
## - 
## - main.sh is a bash script that will run asSeq2Int
## - copy/rename the output file, temp_results.csv as (Data+time)SeqHit.csv
## - then rsync the file to a SeqHitResults directory

module load Python

python3 asSeq2Int.py

## - The following sets the current data and time as now
now=$(date +"%F-%H-%M-%S")
## - Copies and renames the temp_result.csv output from asSeq2Int.py
## - as SeqHit$now.csv
cp temp_results.csv SeqHit$now.csv
## - then prints out the file name for the user
echo "SeqHit Filename: SeqHit-$now.csv"


## - This renamed file is then rsync'd to SeqHitResults directory
rsync -a SeqHit-$now.csv SeqHitResults


## - The Seqeunce Hit results are now ready to be opened and interpreted!
