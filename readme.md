# Currency Convertor 

Use this API to get a JSON response about current Currency rates

## Getting Started

####Usage
```
https://currency-converter-api97.herokuapp.com/api?a=1&f=usd&t=inr
```
####Output
```
{"data":[{"from":["USD","1"]},{"to":["INR","67.2050"]}]}
```
## Parameters Explained
- a => amount to be converted
- f => code of currency from which conversion is to be performed
- t => code of currency to which conversion is to be performed

## Currency Codes

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Built With

* [Bottle](https://bottlepy.org/docs/dev/) - Micro web-framework for Python
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/) - Used for web scrapping
