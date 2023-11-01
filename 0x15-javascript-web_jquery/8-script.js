$(document).ready(function () {
	const list = $("UL#list_movies");
	const url = "https://swapi-api.alx-tools.com/api/films/?format=json";

	$.get(url, function (data) {
		data.results.forEach(({ title }) => {
			list.append(`<li>${title}</li>`);
		});
	});
});
