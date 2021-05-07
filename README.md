# coffee-sow
In this project a dataset was created from a brief research on coffee plantations, it is not intended to be an excellent dataset, it is only for educational purposes about neural networks.  

https://coffeesow.netlify.app/

## Endpoint
POST/ https://coffeesow.herokuapp.com/predict

## Request
| Name        | Data type   |  Required   | Range       | Description                       |
| :---------: |:-----------:|:-----------:|:-----------:|:---------------------------------:|
| temperature | Float       | True        | [0,50]      | Temperature in degrees centigrade |
| humidity    | Float       | True        | [0,1]       | Relative air humidity             |
| altitude    | Float       | True        | [0,5000]    | Meters above sea level            |
| rain        | Float       | True        | [0,1000]    | Liter per square meter per month  |
| sunshine    | Float       | True        | [0,24]      | Hours of sunshine a day           |
