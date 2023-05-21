# Genebank-anaysis-tool
The GenBank File Analysis Tool is a Python script that allows you to search for specific genes in GenBank files, extract relevant information, and save the results in separate output files.

# Prerequisites
Python: Make sure you have Python installed on your system.
Biopython: The script relies on the Biopython library to process GenBank files. You can install it using the following command:
pip install biopython

#Usage
1. Download the Python script containing the GenBank File Analysis Tool.

2. Prepare Input Files: Place your GenBank files (.gb or .gbk extension) in a separate folder. Ensure that only the GeneBank files you want to analyze are located in this folder

3. Run the Script: Open a terminal or command prompt and navigate to the folder where you downloaded the script. Run the following command to execute the script:

python genbank_analysis.py

4. Enter Folder Path: When prompted, enter the path to the folder containing your GenBank files. For example:

Enter the folder path: /path/to/genbank_files
5. Enter Search Phrase: Specify the search phrase to look for in the product qualifier of the GenBank file features. This phrase should help identify the genes you want to extract. 

View Progress: As the script analyzes each file, it will display the filename and the number of genes found in that file. For example:

sample1.gb, genes found: 3
sample2.gbk, genes found: 1
Output Folder: The script will create an "output" folder in the same directory as the script file. Inside the output folder, you will find the results for each input file. Each output file will have the same name as the corresponding input file, followed by "_output.txt".

Review Output Files: After the script finishes analyzing all the input files, you can open the output folder to review the extracted gene, mRNA, and protein information for each file.

Created by Iwo Szemprych, with assistance of ChatGPT
