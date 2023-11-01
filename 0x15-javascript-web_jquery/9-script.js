$(document).ready(function () {
	const helloEl = $("DIV#hello");
	const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

	$.get(url, function (data) {
		helloEl.text(data.hello);
	});
});
