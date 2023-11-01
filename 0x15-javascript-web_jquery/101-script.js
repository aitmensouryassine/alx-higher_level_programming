$(document).ready(() => {
	const list = $("UL.my_list");
	const add = $("DIV#add_item");
	const remove = $("DIV#remove_item");
	const clear = $("DIV#clear_list");

	add.click(() => list.append("<li>Item</li>"));
	remove.click(() => list.children().last().remove());
	clear.click(() => list.empty());
});
