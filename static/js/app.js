$(function () {
	$('[data-toggle="tooltip"]').tooltip();

	$('.navbar-toggle').click(function () {
		$('.navbar-nav').toggleClass('slide-in');
		$('.side-body').toggleClass('body-slide-in');
		$('#search').removeClass('in').addClass('collapse').slideUp(200); 
	});

	$('#search-trigger').click(function () {
		$('.navbar-nav').removeClass('slide-in');
		$('.side-body').removeClass('body-slide-in');
	});
	$('#btn-toggle-menu').click(function() {
		$('#side-menu').toggleClass('side-menu');
		$('#side-menu').toggleClass('side-menu2');
		$('#side-body').toggleClass('side-body');
	});
});