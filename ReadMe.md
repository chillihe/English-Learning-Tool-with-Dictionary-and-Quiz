# English Learning Tool with Dictionary and Quiz Functions

## How Does the Program Work?
The English learning tool is an executable program that runs on Windowns. It is a simple program that mainly has the following two functions, which can be accessed via the buttons on the start page:
* **Dcitionary**: users can enter English word in the Entry box and click the "Search" button. The program will find the definition for the word in the attached dictionary database and display the definitions. If there is a typo, or if the exact word can not be found, the program will find similar words for the user to choose. Additionally, after the search, users can save words, view all saved words, and delete words from the saved database.
![Image of Search](Search.png)
* **Quiz**: the program can generate random multiple-choice questions for the users on different words or definitions. Each correct answer adds one point and each incorrect answer deducts one point. Users can choose to reset the point counter. There are four types of questions:
    * *Random Learned Word*: display one random word from the word list that the user has saved and four options for definitions.
    * *Random Learned Definition*: display one random definition from the word list that the user has saved and four options for words.
    * *Random All Word*: display one random word from the dictionary and four options for definitions.
    * *Random All Definition*: display one random definition from the dictionary and four options for wrods
    ![Image of Quiz](quiz.png)

## How to Download the Program?
Download the **dictionary.db** and **DictionaryExe.exe** from the [**exe**](https://github.com/chillihe/English-Learning-Tool-with-Dictionary-and-Quiz/tree/master/exe) folder and save both files in the same folder. Run the **DictionaryExe.exe** application and start to use the tool. A **learned_words.db** database file will be generated automatically when users start to save searched words.

## How to Edit the Python Code?
Users need to install **Python** to run and edit the Python code. No third-party libraries need to be installed. The [**PageController.py**](https://github.com/chillihe/English-Learning-Tool-with-Dictionary-and-Quiz/blob/master/PageController.py) file serves as the master code. It initiates the program.