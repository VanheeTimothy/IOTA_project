function getdur_txsobject() {
    return dur_txobject;
}

function getsamples_txobject() {
    return samples_txobject
}

function getdur_gettransfer() {
    return dur_gettransfer;
}

function getSamples_transfers() {
    return samples_gettransfer;
}

function get_labels() {
    return dt_gettransfers;

}

function get_dstransfer() {
    return ds_transfer;
}

function get_dstxobject() {
    return ds_txobject;
}
function togglegraph() {
    var ctx1 = document.getElementById("scatter");
    var ctxl2 = document.getElementById("line");

    if (ctx1.style.display === "none") {
        ctx1.style.display = "block";
        ctxl2.style.display = "none";

    } else {
        ctx1.style.display = "none";
        ctxl2.style.display = "block";
    }
}

var lineChartSamples = {
    labels: get_labels(),
    datasets: [{
        label: "duration get_transfers",
        fill: false,
        lineTension: 0.9,
        backgroundColor: "rgba(130,255,67,0.9)",
        borderColor: "rgba(130,255,67,0.9)",
        borderCapStyle: "butt",
        borderdash: [],

        fillColor: "rgba(41, 128, 185, 0.5)",
        strokeColor: "none",
        pointColor: "rgba(41, 128, 185, 0.9)",
        pointStrokeColor: "rgba(41, 128, 185, 0)",
        pointHighlightFill: "rgba(41, 128, 185, 0.9)",
        pointHighlightStroke: "rgba(41, 128, 185, 0)",
        data: getdur_gettransfer()
    },

        {
            label: "sample get_transfers",
            fill: false,
            lineTension: 0.9,
            backgroundColor: "rgba(130,255,67,0.9)",
            borderColor: "rgba(130,255,67,0.9)",
            borderCapStyle: "butt",
            borderdash: [],

            fillColor: "rgba(232,58,61, 0.5)",
            strokeColor: "none",
            pointColor: "rgba(232,58,61, 0.9)",
            pointStrokeColor: "rgba(232,58,61, 0)",
            pointHighlightFill: "rgba(232,58,61, 0.9)",
            pointHighlightStroke: "rgba(232,58,61, 0)",
            data: getSamples_transfers()
        }
        ,
        {
            label: "duration transaction_object",
            fill: false,
            lineTension: 0.9,
            backgroundColor: "rgba(255,255,255,0.9)",
            borderColor: "rgba(255,255,255,0.9)",
            borderCapStyle: "butt",
            borderdash: [],

            fillColor: "rgba(255,255,255,0.9)",
            strokeColor: "none",
            pointColor: "rgba(255,255,255,0.9)",
            pointStrokeColor: "rgba(232,58,61, 0)",
            pointHighlightFill: "rgba(232,58,61, 0.9)",
            pointHighlightStroke: "rgba(232,58,61, 0)",
            data: getdur_txsobject()

        },
        {
            label: "samples transaction_object",
            fill: true,
            lineTension: 0.9,
            backgroundColor: "rgba(255,255,255,0.9)",
            borderColor: "rgba(255,255,255,0.9)",
            borderCapStyle: "butt",
            borderdash: [],

            fillColor: "rgba(255,255,255,0.9)",
            strokeColor: "none",
            pointColor: "rgba(64,255,219,0.8)",
            pointStrokeColor: "rgba(232,58,61, 0)",
            pointHighlightFill: "rgba(232,58,61, 0.9)",
            pointHighlightStroke: "rgba(232,58,61, 0)",
            data: getsamples_txobject()

        }
    ]
};


var scatterplot = {
    datasets: [{
        label: "duration get_transfers",
        fill: false,
        lineTension: 0.9,
        backgroundColor: "rgba(130,255,67,0.9)",
        borderColor: "rgba(130,255,67,0.9)",
        borderCapStyle: "butt",
        borderdash: [],

        fillColor: "rgba(41, 128, 185, 0.5)",
        strokeColor: "none",
        pointColor: "rgba(41, 128, 185, 0.9)",
        pointStrokeColor: "rgba(41, 128, 185, 0)",
        pointHighlightFill: "rgba(41, 128, 185, 0.9)",
        pointHighlightStroke: "rgba(41, 128, 185, 0)",
        data: get_dstransfer()
    },
        {
            label: "samples transaction_object",
            fill: false,
            lineTension: 0.9,
            backgroundColor: "rgba(255,255,255,0.9)",
            borderColor: "rgba(255,255,255,0.9)",
            borderCapStyle: "butt",
            borderdash: [],

            fillColor: "rgba(255,255,255,0.9)",
            strokeColor: "none",
            pointColor: "rgba(64,255,219,0.8)",
            pointStrokeColor: "rgba(232,58,61, 0)",
            pointHighlightFill: "rgba(232,58,61, 0.9)",
            pointHighlightStroke: "rgba(232,58,61, 0)",
            data: get_dstxobject()
        }
    ]
};


window.onload = function () {
    var ctx1 = document.getElementById("scatterChart").getContext("2d");
    var ctxl2 = document.getElementById("lineChart").getContext("2d");

    window.myLine = new Chart(ctx1, {
            type: "scatter",
            data: scatterplot,
            responsive: true,
            options: {
                legend: {
                    fontColor: 'rgb(255, 255, 255)'

                },
                scales: {
                    xAxes: [{
                        display: true,
                        labelString: "time (t)",
                        ticks: {
                            fontColor: "white",
                            fontSize: 12
                        }

                    }],
                    yAxes: [{
                        stacked: false,
                        ticks: {
                            fontColor: "white",
                            fontSize: 12

                        }
                    }]
                },
                title: {
                    display: true,
                    text: 'get_transfer vs find_transaction_objects',
                    fontColor: "white",
                    fontFamily: "Source Sans Pro",
                    fontSize: 14

                }

            }

        }
    );

    window.myLine = new Chart(ctxl2, {
            type: "line",
            data: lineChartSamples,
            responsive: true,
            options: {
                legend: {
                    fontColor: 'rgb(255, 255, 255)'

                },
                scales: {
                    xAxes: [{
                        display: true,
                        labelString: "time (t)",
                        ticks: {
                            fontColor: "white",
                            fontSize: 12
                        }

                    }],
                    yAxes: [{
                        stacked: false,
                        ticks: {
                            fontColor: "white",
                            fontSize: 12

                        }
                    }]
                },
                title: {
                    display: true,
                    text: 'loadtime versus number of datapoints',
                    fontColor: "white",
                    fontFamily: "Source Sans Pro",
                    fontSize: 14

                }

            }

        }
    )
    ;
};

