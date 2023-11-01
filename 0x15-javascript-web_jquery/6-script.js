$(document).ready(function () {
	const updateHeader = $("#update_header");
	const header = $("header");
	updateHeader.click(function () {
		header.text("New Header!!!");
	});
});
