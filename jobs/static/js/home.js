function goToLocalURL(link) {
    // console.log(window.location.href + link)
    window.location = window.location.href + link
}

$(document).ready(() => {
    let psquare = $('.project-square');

    psquare.mouseenter(function(){
        $(this).find('.project-image').css('filter', 'blur(8px)')
        $(this).find('.project-info').css('z-index', '3')
    });
    psquare.mouseleave(function(){
        $(this).find('.project-image').css('filter', 'blur(0px)')
        $(this).find('.project-info').css('z-index', '1')
    });
});