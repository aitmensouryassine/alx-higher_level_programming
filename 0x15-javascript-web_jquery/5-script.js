$(document).ready(function () {
	const addItem = $("#add_item");
	const list = $("ul.my_list");
	addItem.click(function () {
		list.append("<li>Item</li>");
	});
});
