/* Author: Adam Bard

*/

function onResize(){
	var width = $(window).width();
	b = $('body')
	b.removeClass('narrow').removeClass('mobile')

	if(width <= 480){
		b.addClass('mobile')
	}
	if(width <= 940){
		b.addClass('narrow')
	}
}

$(window).resize(onResize);
onResize();





















