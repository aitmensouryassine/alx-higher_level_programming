$(document).ready(function () {
	const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
	const character = $("#character");

	$.get(url, function (data) {
		character.text(data.name);
	});
});
