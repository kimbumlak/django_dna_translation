# django_dna_translation

This dna_translation website is made for researchers who are interested in revealing whether frequencies of particular amino acids are simply a consequence of random permuations of the genetic code or instead a product of natural selection. Meaning, is there are any correlation between certain amino acids and protein structure or is it just a random.

To use this web application, this project is published using heroku: https://dna-translation.herokuapp.com/ 

* Users can obtain FASTA file from Genbank, copy paste everything in FASTA file into text area and submit to see result. The nucleotide sequence in FASTA file should only contain A,C,G,T or U. If else, will give error message.

* This web application translates dna sequence to protein sequence and shows protein sequence in table as well as frequency visualization bar graph for better overall view of protein sequences.

* Bioinformaticians and researchers can visually identify protein distribution of DNA sequence.

* Used Pandas library for data manipulation and analysis of interpreted DNA sequence and Matplotlib library for plotting manipulated data for visualization.
