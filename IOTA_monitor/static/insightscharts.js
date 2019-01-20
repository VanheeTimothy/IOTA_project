function getDuration() {
    return duration;
}

function getSamples() {
    return samples;
}

var samplelabel = [];
for (i = 0; i < samples.length; i++) {
    samplelabel.push(i);
}


var lineChartSamples = {
    labels: samplelabel,
    datasets: [{
        label: "duration",
        fill: false,
        lineTension: 0.9,
        backgroundColor: "rgba(130,255,67,0.4",
        borderColor: "rgba(130,255,67,0.4",
        borderCapStyle: "butt",
        borderdash: [],

        fillColor: "rgba(41, 128, 185, 0.5)",
        strokeColor: "none",
        pointColor: "rgba(41, 128, 185, 0.9)",
        pointStrokeColor: "rgba(41, 128, 185, 0)",
        pointHighlightFill: "rgba(41, 128, 185, 0.9)",
        pointHighlightStroke: "rgba(41, 128, 185, 0)",
        data: getDuration()
    },
        {
            label: "samples",
            fill: true,
            lineTension: 0.9,
            backgroundColor: "rgba(255,244,0,0.4)",
            borderColor: "rgba(255,244,0,0.4)",
            borderCapStyle: "butt",
            borderdash: [],

            fillColor: "rgba(232,58,61, 0.5)",
            strokeColor: "none",
            pointColor: "rgba(232,58,61, 0.9)",
            pointStrokeColor: "rgba(232,58,61, 0)",
            pointHighlightFill: "rgba(232,58,61, 0.9)",
            pointHighlightStroke: "rgba(232,58,61, 0)",
            data: getSamples()

        }]
};


window.onload = function () {
    var ctx1 = document.getElementById("sampleChart").getContext("2d");
    window.myLine = new Chart(ctx1, {
            type: "line",
            data: lineChartSamples,
            responsive: true,
            options: {
                legend: {
                    fontColor: 'rgb(255, 255, 255)'

                },
                scales: {
                    xAxes: [{
                        display: false,
                        labelString: "time (t)"

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
                    text: 'loadtime versus number of datapoints',
                    fontColor: "white",
                    fontFamily: "Source Sans Pro",
                    fontSize: 14,

                }

            }

        }
    )
    ;
}