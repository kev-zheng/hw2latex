# hw2latex

An easy to use command line interface for a standard LaTeX homework template
using Jinja2 in Python 3

# Example
(copy & paste straight from homework PDF)
<pre>
$ python3 hw2latex

* DOCUMENT INPUT *

Your name: <b>Kevin Zheng</b>
Class name: <b>Probabilistic Methods in Engineering (VE401)</b>
Assignment Number: <b>1</b>
Term (i.e. Summer 2017): <b>Summer 2017</b>
Due Date: <b>May 29, 2017</b>

* PROBLEM INPUT *

Problem number: <b>1.1</b>
Problem description: <b>Sample Space, Events, Probabilities</b>
Short excerpt of problem: <b>To get the opportunity to enter the McNeill</b>
Points:<b>7</b>
Hit enter to continue. Type "exit" to exit. 

Problem number:<b>1.2</b>
Problem description:<b>DAlemberts Approach to Coin Tossing</b>
Short excerpt of problem:<b>The French mathematician Jean DAlembert claimed</b>
Points:<b>4</b>
Hit enter to continue. Type "exit" to exit. <b>exit</b>
</pre>

# Result

### LaTeX Output:
![alt tag](https://github.com/kev-zheng/hw2latex/blob/master/Example/A1_code_example.png)

### Resulting example PDF:
![alt tag](https://github.com/kev-zheng/hw2latex/blob/master/Example/A1_pdf_example.png)

# Installation

Clone this repository
```
git clone https://github.com/kev-zheng/hw2latex.git
```

# Dependencies
hw2latex.py uses __Python 3__ and __Jinja 2__
```
pip3 install jinja2
```

# Usage
Simply run
```
python3 hw2latex
```
and follow the command line instructions.


