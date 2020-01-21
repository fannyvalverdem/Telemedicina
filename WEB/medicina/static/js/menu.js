$(function(){
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault()
    	
       $('body, main').animate(
            {
            scrollTop: $($(this).attr('href')).offset().top,
            },
            500,
            'linear'
        )
        oldObjChild=$('.active > a'); //gets active nav-item child nav-link
        oldObj = $('.active'); //gets the active nav-item
        oldObj.removeClass('active'); //remove active from old nav-item
        oldObjChild.css('color','white'); //clear old active nav-item and nav-link style for bg color
        $(this).parent().addClass('active'); //set the active class on the nav-item that called the function
        $(this).css('color','#e53956'); //set active clas background to red
      });