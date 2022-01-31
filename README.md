# Examtopics Question Parser
A python script to parse questions from ExamTopics question dumps. The script turns the raw input into an interactive quiz.

### Currently Supported Features
* Parses a raw question dump from ExamTopics into a quiz.
* Changable quiz length and passing score.
* Random questions from dump each time.

### Requirements
* There are no requirements for this script.

### Installation
1. Clone this repository using the command:
```
git clone https://github.com/d4rkflam1ngo/examtopics-question-parser && cd examtopics-question-parser
```
2. Visit [ExamTopics](https://www.examtopics.com/) and find the exam questions you would like to parse.
3. When viewing the questions select `Custom View Settings` and change the number of questions per page to the amount you would like to parse (you may need a premium account to view a large number at once).
4. Ensure `Generate a printer-friendly version` and ` Render the questions with answers exposed` are both selected then select `Set Session Settings`.

![Custom View Settings](https://github.com/d4rkflam1ngo/examtopics-question-parser/blob/main/custom-view-settings.png)

5. Once the questions have rendered, select all the text on the page `Ctrl-A`. Paste this text into a file and remove the text from the page header and footer. (See the [example file](https://github.com/d4rkflam1ngo/examtopics-question-parser/blob/main/example-dump.txt) for what the final dump should look like).
6. Customise the script where necersarry, change the file name and the passing percentage.
7. Launch the script by running:
```
python3 examtopics-question-parser.py
```

### Requested Features
- [ ] Web scraper
