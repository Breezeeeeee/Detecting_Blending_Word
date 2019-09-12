# Detecting_Blending_Word
This is a project that detecting the blending word in Twitter data
We both run program on CPU and turn string into numpy vector then run on GPU, which the results are the same. The testing environment including: python 3.7, jupyter notebook  1.0,  Anaconda 1.7, CPU i7-9700, GPU RTX 2080Ti.
Before run the program, please change the file path to open "blend.txt","candidatas.txt"."dictionary.txt"
File guides:
	report.py: Contains the normal methods in the report, import this file and use by report.*
	repeat_character.py: This file is used to remove bad input which have repeat character
	spell_mistake.py: This is the file to remove words that have spell mistakes
	GED.py: This is the file to find maximum global edit distance for all tokens in candidates
	LED.py: This is the file to find maximum local edit distance for all tokens in candidates
	NGram2.py: This is the file to find minimum 2-Gram distance for all tokens in candidates
	NGram3.py: This is the file to find minimum 3-Gram distance for all tokens in candidates
	JARO.py: This is the file to find maximum jaro-winkler similarity for all tokens in candidates.

The data that generated in this project are store in data floder:
	GEDTotal: This is the file that contains: token, maximum global edit distance, match word in dictionary for all tokens in candidates
	LEDTotal: This is the file that contains: token, maximum local edit distance, match word in dictionary for all tokens in candidates
	2GramTotal: This is the file that contains: token, minimum 2-Gram distance, match word in dictionary for all tokens in candidates
	3GramTotal: This is the file that contains: token, minimum 3-Gram distance, match word in dictionary for all tokens in candidates
	JAROTotal: This is the file that contains: token, maximum Jaro-winkler similarity, match word in dictionary for all tokens in candidates
	All of the results are based on "blend.txt","candidatas.txt"."dictionary.txt"
	Thank you for reading
