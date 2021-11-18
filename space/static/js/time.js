$(document).ready(function () {
    $('#time1').timepicker({
        timeFormat: 'h:mm p',
        interval: 30,
        minTime: '9',
        maxTime: '8:00pm',
        startTime: '9:00am',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});

$(document).ready(function () {
    $('#time2').timepicker({
        timeFormat: 'h:mm p',
        interval: 30,
        minTime: '10',
        maxTime: '9:00pm',
        startTime: '10:00am',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});