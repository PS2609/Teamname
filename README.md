## Problem Statement
Develop an AI-driven system that augments support agents' abilities to resolve customer issues promptly. The solution should analyze incoming tickets, provide relevant knowledge base articles, suggest potential solutions, and learn from each interaction to enhance future recommendations.

## StakeHolders
- **Customers:** Have an AI Chatbot to quickly address basic queries and streamline various processes
- **Agent:** Uses AI based tools to resolve tickets efficiently
- **Buisnesses:** AI-driven support system enhances efficiency, reduces costs, and improves customer satisfaction for businesses

## UserFlow

![Flowchart](https://github.com/Edward4762/Teamname/blob/main/image/Flowchart.png)

## Features
### Customers 
- Human Intervention Detection
- Reinforced Learning
- Providing a tag based system for ticket classification

![Customers](https://github.com/Edward4762/Teamname/blob/main/image/Customer.jpg)

### Agents
- Real time analysis of ticket resolution
- Faster ticket resolution leading to better efficiency

![Agents](https://github.com/Edward4762/Teamname/blob/main/image/Agent.jpg)
### Businesses
- Meeting customer satisfaction leading to strong relationship with the customers
- Reduced ticket backlog leading to improved customer service efficiency

![Buisnesses](https://github.com/Edward4762/Teamname/blob/main/image/Buisnesses.jpg)

## Installation 

### Chatbot

Create a virtual environment
```
$ python3 -m venv venv
$ .venv\scripts\activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk flask-cors
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python train.py
$ (venv) python chat.py
```
Run
```
$ (venv) python -m flask run
```


## Video Demo



https://github.com/Edward4762/Teamname/assets/123575108/17fb304a-0087-42a8-b656-492f9f316184



## Contributors
- Priyanshi Sharma
- Sakshi Jha
- Ansh Singh
- Harsh Kumar
- Satyam Raj
