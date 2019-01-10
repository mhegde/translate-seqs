# Translate nucleotide sequences to amino acid sequences

This script takes a file with nucleotide sequences and translates them into amino acid sequences.

<b>Author</b>: Mudra Hegde  
<b>Email</b>: mhegde@broadinstitute.org  

<b>Required packages</b>
1. pandas 

<b>Inputs</b>
1. <b>Input File</b>: .txt file with list of sequences to translate in the first column. The consecutive columns can have anything. The column with the translated sequences will be included as the last column. 
2. <b>Frame</b>: Reading frame of sequence (1,2 or 3) 
3. <b>Codon File</b>: .txt file with codons in the first column and the corresponding amino acid in the second column. Default: Codon_map.txt (provided in this folder).
4. <b>Output File</b>

<b>To run this script, type the following on the terminal:</b>  
python translate_seqs.py --inputfile \<Path to input file\> --frame \<1, 2  or 3\> --codon-file \<Path to codon file\> --outputfile \<Name of output file\>  