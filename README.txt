Welcome to Group 23 Machine Learning Project.
Created by Karan and Manabputra
For CS460 taught by Shubhankar Mishra

Procedural Generation of Portal 2 levels using DCGANs.

Summary using a corpus of example levels as data to train a DCGAN to be able to generate level file for Portal 2.

Original Goal: Create very basic playable levels with interesting structures.

------------------------------------------------------------------------------------------------------------------

INSTRUCTIONS FOR RUNNING THE ALGORITHM.

------------------------------------------------------------------------------------------------------------------
The level encoder folder includes all the files necessary to run the training algorithm.

1. The "Final 3 layer GAN" notebook contains the Algorithm code. that trains on the 38 training levels.
	- The code runs on Keras tensorflow, it runs smoothly on google colab. The code has not been run on a local machine.
	
2. The Algorithm saves an example level from each epoch "Data<epoch number><level index>.csv". These are then ran through makelevel() 
   to do the appropriate 1 hot encoding and conversion into binary values, from the the floating point values.
3. The resulting "finalevel.csv" file is then ran through "levelinterpreter.py" to convert into .p2c format.
4. This .p2c can then be ran inside the game to see what the resultant level looks like.
------------------------------------------------------------------------------------------------------------------

NOTES

------------------------------------------------------------------------------------------------------------------
- The level manipulation code that creates the dataset is copied into the notebook and need not be run separately.
- The level interpreter code currently only creates the geometry generation of the level. Item placement is very buggy and will only
  be added in later updates.


