!#/bin/bash
echo 'attempting to set up folders and download data files.'
mkdir data/
mkdir data/output/
mkdir data/processed/
mkdir data/raw/
mkdir graphs/
mkdir models/

curl https://s3-eu-west-1.amazonaws.com/adthena-ds-test/trainSet.csv --output data/raw/trainSet.csv
curl https://s3-eu-west-1.amazonaws.com/adthena-ds-test/candidateTestSet.txt --output data/raw/candidateTestSet.csv
echo 'completed setting up folders and downloading data files.'