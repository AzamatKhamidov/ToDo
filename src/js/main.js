console.log('start');

let todoItems = [];
let todo_unchecked = 'icons/unchecked.png';

function addItem() {
	todoItems.push({
		'text' : document.getElementById('addInput').value,
		'checked' : false,
		'decs' : null,
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
	todoItems.splice(item_id, 1);
	todoItemsList();
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
		trLast.onclick = function() {check_item(todoItems.indexOf(entry));};
		let tdText = document.createElement('td');
		tdText.className = 'todoText';
		tdText.innerHTML = entry['text'];
		if (entry['checked']) {
			tdText.innerHTML = '<b><del>'+entry['text']+'</del></b>';
		}
		let tdImg = document.createElement('td');
		tdImg.className = 'todoImg';
		let imgCheck = document.createElement('div');
		imgCheck.className = todo_checkeds;
		let imgGarbage = document.createElement('div');
		imgGarbage.className = 'delete_btn';
		imgGarbage.onclick = function() {delete_item(todoItems.indexOf(entry));};
		tdImg.append(imgCheck, imgGarbage);
		trLast.append(tdText, tdImg);
		document.getElementById('todoItems_ul').append(trLast);
	})
}
function ItemsList () {
	console.log(todoItems.length);
	todoItems.forEach(function(entry) {
		console.log(entry);
		if (entry['checked']) {
			todo_checked = 'icons/checked.png';
		};
		var lists  = document.getElementById('todoItems');
		// console.log(document.getElementById('todoItems').text)
		lists.innerHTML = lists.innerHTML+'<li class="todo_item">'+entry['text']+'</li><img src="'+todo_unchecked+'" alt="" class="todo_delete"><img src="" alt="" class="todo_checked">';
	});
}


todoItemsList()