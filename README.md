# coffee-sow
In this project a dataset was created from a brief research on coffee plantations, it is not intended to be an excellent dataset, it is only for educational purposes about neural networks.

## Endpoint
POST/ https://coffeesow.herokuapp.com/predict

## Request
| Name        | Data type   |  Required   | Range       | Description                       |
| :---------  |:-----------:|:-----------:|:-----------:|----------------------------------:|
| Temperature | Float       | True        | [0,50]      | Temperature in degrees centigrade |
| Humidity    | Float       | True        | [0,1]       | Relative air humidity             |
| Altitude    | Float       | True        | [0,5000]    | Meters above sea level            |
| Rain        | Float       | True        | [0,1000]    | Liter per square meter per month  |
| Sunshine    | Float       | True        | [0,24]      | Hours of sunshine a day           |
