# CoffeeMachine
Write the working code to create a working coffee machine with the desired features

1 . It will be serving some beverages. <br/>
2 . Each beverage will be made using some ingredients.  <br/>
3 . Assume time to prepare a beverage is the same for all cases.  <br/>
4 . The quantity of ingredients used for each beverage can vary. Also, the same ingredient (ex: water) can be used for multiple beverages.  <br/>
5 . There would be N ( N is an integer ) outlet from which beverages can be served.  <br/>
6 . Maximum N beverages can be served in parallel. <br/>
7 . Any beverage can be served only if all the ingredients are available in terms of quantity. <br/>
8 . There would be an indicator that would show which all ingredients are running low. We need some methods to refill them. <br/>

<br />
Input Test Json :- 
<br />

```
https://www.npoint.io/docs/77e0bf528e4af43cdc10
```

<br />
Expected Output :- 

Output 1
(This input can have multiple outputs. )
<br />
```
hot_tea is prepared
hot_coffee is prepared 
green_tea cannot be prepared because green_mixture is not available 
black_tea cannot be prepared because item hot_water is not sufficient
```
<br />


Command to run the file
```
(venv) $ ls
beverage.py                     coffee_machine.py               main.py
coffee-machine-test-input.json  inventory.py                    venv
(venv) $ python3 main.py coffee-machine-test-input.json 
hot_tea is prepared
hot_coffee is prepared
black_tea cannot be prepared, hot_water is not sufficient
green_tea cannot be prepared, sugar_syrup is not sufficient
(venv) $ 

```


## Others things that can be added:
1. Logging
2. Pytests
3. Explain you design choices
4. Maybe add a .gitignore
5. If you will be using logger then talking about virtual env in Readme
6.  For each funct define args and return vals