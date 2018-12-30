

// Line Chart

function getData() {
    return tempdata;
}

var arraylabel = [];
for (i = 0; i < tempdata.length; i++) {
    arraylabel.push(i);
}

var lineChartData = {
    labels:arraylabel,
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
        data: getData()
    }]
};

window.onload = function () {
    var ctx1 = document.getElementById("myChart").getContext("2d");
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
                    yAxes:[{
                        stacked: true
                    }]
                }

            }

        }
    )
    ;
}
;

