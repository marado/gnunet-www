$(window).scroll(function() {
    if ($(this).scrollTop() >= 50) {
        $('#jump-top').fadeIn(200);
    } else {
        $('#jump-top').fadeOut(200);
    }
});
$('#jump-top').click(function() {
    $('html').animate({
        scrollTop : 0
    }, 500);
});
