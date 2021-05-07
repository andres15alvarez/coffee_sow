let temperature_, humidity_, altitude_, rain_, sunshine_;

$(document).ready(function(){
    temperature_ = document.getElementById("temperature");
    humidity_ = document.getElementById("humidity");
    altitude_ = document.getElementById("altitude");
    rain_ = document.getElementById("rain");
    sunshine_ = document.getElementById("sunshine");
});

$(document).on('click','#predict',function(){
    let temperature = temperature_.value;
    let humidity = humidity_.value;
    let altitude = altitude_.value;
    let rain = rain_.value;
    let sunshine = sunshine_.value;
    if(temperature == "" || humidity == "" || altitude == "" || rain == "" || sunshine == ""){
      $(".prediction").html("Please, complete all entries");
    } else{
        temperature = parseFloat(temperature);
        humidity = parseFloat(humidity);
        altitude = parseFloat(altitude);
        rain = parseFloat(rain);
        sunshine = parseFloat(sunshine)
        if((temperature < 0 || temperature > 50) || (humidity < 0 || humidity > 1) || (altitude < 0 || altitude > 5000) || (rain < 0 || rain > 1000) || (sunshine < 0 || sunshine > 24)){
            $(".prediction").html("Please, enter valid values");
        } else{
            const requestURL = "https://coffeesow.herokuapp.com/predict";
            fetch(requestURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    temperature,
                    humidity,
                    altitude,
                    rain,
                    sunshine,
                })
            })
            .then(response => response.json())
            .then(result => {
                console.log(result);

                if(result['error']){
                    $(".prediction").html("An error has occurred");
                } else{
                    $(".prediction").html("Prediction: " + result['predict']);
                }
            })
        }
    }
});