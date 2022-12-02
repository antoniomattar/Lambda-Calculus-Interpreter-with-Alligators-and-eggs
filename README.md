# Alligators-python

<img align="right" width="200" height="100" src="https://i.imgur.com/C5MWF5V.png">

## About the project

The main goal of the program is to generate the result of the beta_reduction of a lambda term given as an input and to show the images of the alligator's families that represents the lambda term and the different steps of it's beta_reduction. It also allows us to see how logical, boolean and arithmetic expressions are written in lambda calculus.

## Table of contents


<!-- TOC -->- [The structures](#structures)<br />    - [What to install](#needs)<br />    - [How to install](#how)<br />    - [Usage](#utilisation)<br />    - [Parsing syntax ](#parse)<br />    - [Documentation](#docu)<br />    - [Project status and Contribution](#status)<br /> <!-- /TOC -->

## Structures <a name="structures"></a>

Lambda terms are respresented by lists, the first element of the list is an indication to the type of the lambda term that it represents.<br />
<strong>Variable</strong>: [VAR, name]<br />
<strong>Abstraction</strong>: [ABS, input, output] input and output are also lambda terms<br />
<strong>Application</strong>: [APP, first_Term, second_Term] first_term and second_term are also lambda terms<br />

The JPEG images are already created, to build the image of a lambda term, we just have to concatenate the existing images and to colorate the alligators and eggs by random colors.

## What to install <a name="needs"></a>

1. PIL library (used to generate images)
2. PYFIGLET library(used to implement a new font)
3. keyboard module (used to get an enter char)
4. shutil module (manipulate directories)

## How to install <a name="how"></a>

- To install the needed tools, you have to use the following command:<br />
 `pip: -r requirements.txt`

## Usage <a name="utilisation"></a>
The program is very simple to use, these are some advices once we run the code: <br />
1. When you have to make a choice, click a button which is indicated, the code won't stop asking you to re-enter a choice until you press a right button.
2. The lambda term that is given as an input has to respect some syntactic rules, you can find the rules in the section parsing syntax.
3. When you choose an option in the menu, the images that could have been generated are stocked in a temporary directory which you are free to save or delete at the end.

## Parsing Syntax <a name="parse"></a>
In order to parse a lambda term, we have to respect some rules:<br />
1. The lambda term has to be written in a single line.<br />
2. Represent the lambda by a hashtag '#'<br />
3. For the variable, the name of the variables cannnot contain spaces or it wont be considered a variable (it would be considered an application)<br />
4. For the abstraction, the input has to be written between the hashtag '#' and the point '.' which seperates the input from the output, then WITHOUT SPACE directly after the dot the output of the term should be written<br />
5. For the application, the first term has to be written between parantheses only if it is not a variable and then a SPACE seperates the first term from the second, which should be written between parantheses only if it is an application<br />
EXAMPLES:<br />
` λx.x ---> #x.x`<br />
`λx.x λy.y ---> (#x.x) #y.y`     ( NOT `#x.(x #y.y)` )<br />
`λf.(λx.(f(x x)))λx.(f(x x)) ---> #f.(#x.(#f.(x x)))c#f.(#x.(#f.(x x)))`

##  Documentation <a name="docu"></a>
<a href='https://en.wikipedia.org/wiki/Lambda_calculus'>WikiPedia: Lambda Calculus</a> <br>
<a href='https://brilliant.org/wiki/lambda-calculus/'>Brilliant: Lambda Calculus</a> <br>
<a href='https://mpsib-camille-guerin.pagesperso-orange.fr/Python/Lambda/Lambda2/Lambda2.pdf'>MPSIB-CAMILLE-GUERIN: Lambda Calculus</a>
***


## Authors and acknowledgment
Authors:<br> 
<a href="mailto:antoniomattar132@gmail.com>">Antonio MATTAR</a>
<a href="mailto:aiteldjouditamazouzt@gmail.com">Tamazouzt AIT ELDJOUDI</a>

Under the supervision of:<br>
<a href="https://pageperso.lis-lab.fr/~benjamin.monmege">Benjamin MONMEGE</a>
<a href="http://perso.eleves.ens-rennes.fr/people/julie.parreaux/index.html">Julie PARREAUX</a>


## License
GNU General Public License v3.0

## Project status <a name = 'status'></a>
The project development finished. However,
If you want to contribute in this project, we did a small unfinished todo list:<br />
TO DO LIST:<br>
. Add a menu to choose the language of the program (English or French)<br />
. Add a menu to choose the quality of images generated by the program.
<font size='1'>(HIGH, MEDIUM, LOW)</font><br />
.Add an option to save the reduction as an animation with alligators eating and sound effects.<br />
.Add the possibility to deal with relative integers in the arithmetic operations.
<font size ='1'> (NEED A GOOD KNOWLEDGE OF LAMBDA CALCULUS)</font><br />