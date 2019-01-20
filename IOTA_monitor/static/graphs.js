// Line Chart

function getTempData() {
    return tempdata;
}

function getHummData(){
    return hummdata;
}

var templabel = [];
for (i = 0; i < tempdata.length; i++) {
    templabel.push(i);
}

var hummlabel = [];
for (i = 0; i < hummdata.length; i++) {
    hummlabel.push(i);
}

var lineChartData = {
    labels: templabel,
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
            data: lineChartData,
            responsive: true,
            options: {
                scales: {
                    xAxes: [{
                        display: false,
                        labelString: "time (t)"
                    }],
                    yAxes: [{
                        stacked: true
                    }]
                }

            }

        }
    )
    ;
}
;

