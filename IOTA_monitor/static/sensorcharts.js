// Line Chart

function getTempData() {
    return tempdata;
}

function getHummData() {
    return hummdata;
}

function getLabels() {
    return labels;
}


var lineChartSensors = {
    labels: getLabels(),
    datasets: [{
        label: "one-wire",
        fill: true,
        lineTension: 0.9,
        backgroundColor: "rgba(75,192,192,0.4)",
        borderColor: "rgba(75,192,192,1)",
        borderCapStyle: "butt",
        borderdash: [],

        fillColor: "rgba(41, 128, 185, 0.5)",
        strokeColor: "none",
        pointColor: "rgba(41, 128, 185, 0.9)",
        pointStrokeColor: "rgba(41, 128, 185, 0)",
        pointHighlightFill: "rgba(41, 128, 185, 0.9)",
        pointHighlightStroke: "rgba(41, 128, 185, 0)",
        data: getTempData()
    },
        {
            label: "DHT-11",
            fill: true,
            lineTension: 0.9,
            backgroundColor: "rgba(232,58,61,0.4)",
            borderColor: "rgba(232,58,61,1)",
            borderCapStyle: "butt",
            borderdash: [],

            fillColor: "rgba(232,58,61, 0.5)",
            strokeColor: "none",
            pointColor: "rgba(232,58,61, 0.9)",
            pointStrokeColor: "rgba(232,58,61, 0)",
            pointHighlightFill: "rgba(232,58,61, 0.9)",
            pointHighlightStroke: "rgba(232,58,61, 0)",
            data: getHummData()

        }]
};


window.onload = function () {
    var ctx1 = document.getElementById("tempChart").getContext("2d");
    window.myLine = new Chart(ctx1, {
            type: "line",
            data: lineChartSensors,
            responsive: true,
            options: {
                legend: {
                    fontColor: 'rgb(255, 255, 255)'

                },
                scales: {
                    xAxes: [{
                        display: true,
                        labelString: "time (t)",
                        stepSize: 20,
                        ticks: {
                            fontColor: "white",
                            fontSize: 12

                        }
                    }],
                    yAxes: [{
                        stacked: false,
                        ticks: {
                            fontColor: "white",
                            fontSize: 12,
                            beginAtZero: true
                        }
                    }]
                },
                title: {
                    display: true,
                    text: 'sensorvalues',
                    fontColor: "white",
                    fontFamily: "Source Sans Pro",
                    fontSize: 14

                }


            }

        }
    )
    ;
};


