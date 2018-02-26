var nav = document.getElementById('slide_menu');
var closeMenu = document.getElementById('close_menu');
var openMenu = document.getElementById('open_menu');
var main = document.getElementsByClassName('main');

closeMenu.onclick = function() {
	nav.style.left = -300 + 'px';
	openMenu.style.display = 'block';
	closeMenu.style.display = 'none';
	main.style.left = 75 + 'px';
}

openMenu.onclick = function() {
	nav.style.left = 0 + 'px';
	openMenu.style.display = 'none';
	closeMenu.style.display = 'block';
}




