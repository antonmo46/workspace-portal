$(function () {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            build: '196',
            fail: 39,
            total: 159
        }, {
            build: '197',
            fail: 38,
            total: 159
        }, {
            build: '198',
            fail: 31,
            total: 160
        }, {
            build: '199',
            fail: 31,
            total: 160
        }],
        xkey: 'build',
        ykeys: ['fail', 'total'],
        labels: ['Fail', 'Total'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });   

});
