console.log('start');

let todoItems = [];
let todo_unchecked = 'icons/unchecked.png';


function editText(item_id) {
	todoItems[item_id]['edit'] = true;
	todoItemsList();
}

function editKeys(item_id, event) {
	if (event.keyCode == 13) {
		edited(item_id);
		todoItemsList();
	} else {
		document.getElementById(item_id).style.width = ((document.getElementById(item_id).value.length + 1) * 8)  + "px";
	}
}


function addItem() {
	if (document.getElementById('addInput').value.trim() == ''){
		document.getElementById('addInput').value = '';
		return false;
	}
	todoItems.push({
		'text' : document.getElementById('addInput').value,
		'checked' : false,
		'decs' : null,
		'edit' : false,
		'id' : new Date().getTime()
	});
	document.getElementById('addInput').value = '';
	todoItemsList();
	return false;
}

function check_item(item_id) {
	if (todoItems[item_id]['checked'] == false) { 
		todoItems[item_id]['checked'] = true;
	} else {
		todoItems[item_id]['checked'] = false;
	};
	todoItemsList();
}

function delete_item(item_id) {
	askings = confirm('Delete task?')
	if (askings) {
		todoItems.splice(item_id, 1);
		todoItemsList();
	}
}

function edited(item_id) {
	todoItems[item_id]['text'] = document.getElementById(item_id).value;
	todoItems[item_id]['edit'] = false;
	todoItemsList();
}

function make_visibale(items_id, make_visibale) {
	if (make_visibale) {
		document.getElementsByClassName(items_id)[0].style.display = 'inline';
		document.getElementsByClassName(items_id)[1].style.display = 'inline';
		return
	}
	document.getElementsByClassName(items_id)[0].style.display = 'none';
	document.getElementsByClassName(items_id)[1].style.display = 'none';
}
function todoItemsList() {
	document.getElementById('todoItems_ul').innerHTML = ''
	todoItems.forEach(function(entry) {
		var todo_checkeds = 'unchecked todo_img';
		if (entry['checked']) {
			todo_checkeds = 'checked todo_img';
		};
		let trLast = document.createElement('tr');
		trLast.className = 'todoItem';
		trLast.ondblclick = function() {check_item(todoItems.indexOf(entry));};
		trLast.onmouseover = function() {make_visibale('hidden_btn_'+String(todoItems.indexOf(entry)), true)}
		trLast.onmouseout = function() {make_visibale('hidden_btn_'+String(todoItems.indexOf(entry)), false)}
		let tdText = document.createElement('td');
		tdText.className = 'todoText';
		if (entry['edit']) {
			let editInput = document.createElement('input');
			editInput.value = entry['text'];
			editInput.id = String(todoItems.indexOf(entry));
			editInput.className = 'editText';
			editInput.autofocus = true;
			editInput.onkeypress = function() {editKeys(todoItems.indexOf(entry), event)};
			editInput.onfocusout = function() {editKeys(todoItems.indexOf(entry), {keyCode : 13})};
			editInput.style.width = ((entry['text'].length + 1) * 8)  + "px";
			let tdImg = document.createElement('td');
			let imgDone = document.createElement('div');
			imgDone.className = 'edited_btn';
			imgDone.onclick = function() {edited(todoItems.indexOf(entry))};
			tdImg.className = 'todoImg';	
			tdText.append(editInput)
			tdImg.append(imgDone);
			trLast.append(tdText, tdImg);
			document.getElementById('todoItems_ul').append(trLast);
			return false;
		} else {
			tdText.innerHTML = entry['text'];
		}
		if (entry['checked']) {
			tdText.innerHTML = '<b><del>'+entry['text']+'</del></b>';
		}
		let tdImg = document.createElement('td');
		tdImg.className = 'todoImg';
		let imgCheck = document.createElement('div');
		imgCheck.className = todo_checkeds;
		imgCheck.onclick = function() {check_item(todoItems.indexOf(entry));};
		let imgGarbage = document.createElement('div');
		imgGarbage.className = 'delete_btn hidden_btn_'+String(todoItems.indexOf(entry));
		imgGarbage.onclick = function() {delete_item(todoItems.indexOf(entry));};
		let imgEdit = document.createElement('div');
		imgEdit.className = 'edit_btn hidden_btn_'+String(todoItems.indexOf(entry));
		imgEdit.onclick = function() {editText(todoItems.indexOf(entry));};
		tdImg.append(imgCheck, imgEdit, imgGarbage);
		trLast.append(tdText, tdImg);
		document.getElementById('todoItems_ul').append(trLast);
	})
}


todoItemsList()
