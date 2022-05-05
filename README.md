# NSMsearch (Unfinished)
Python scripts for reads (containing NSM codon) identification in public transcriptome data
## Procedure
### Step1    
Create the signature sequence of each NSM    

**Input files**: *DNA_Base_info.txt*; *Substitution_in_POOL1andPOOL2.tab*
**Code files**: *step1.py*
**Output files**: *NSM_signature.fasta*    

**NOTE:**  
Each NSM signature sequence in the output file (NSM_signature.fasta) has 9 bases (three codon).  The middle three bases were the mutational codon corresponding to the substitution. The head three bases and the tail three bases were reference sequence codon.
