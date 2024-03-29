// This function is called when any of the tab is clicked
// It is adapted from https://www.w3schools.com/howto/howto_js_tabs.asp

function openInfo(evt, tabName) {

	// Get all elements with class="tabcontent" and hide them
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}

	// Get all elements with class="tablinks" and remove the class "active"
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}

	// Show the current tab, and add an "active" class to the button that opened the tab
	document.getElementById(tabName).style.display = "block";
	evt.currentTarget.className += " active";

}


	
// generate a checkbox list from a list of products
// it makes each product name as the label for the checkbos

function populateListProductChoices(slct1, slct2, slct3, slct4, slct5, slct6) {
    var s1 = document.getElementById(slct1); //NutFree
    var s2 = document.getElementById(slct2); //LactoseFree
    var s3 = document.getElementById(slct3); //Organic
	var s4 = document.getElementById(slct4); //Snacks
	var s5 = document.getElementById(slct5); //Meals
	var s6 = document.getElementById(slct6); //List
	
    s6.innerHTML = "";
		
	// obtain a reduced list of products based on restrictions
	console.log(s1.checked, s2.checked, s3.checked, s4.checked, s5.checked)
    var optionArray = restrictListProducts(products, s1.checked, s2.checked, s3.checked, s4.checked, s5.checked);

	// for each item in the array, create a checkbox element, each containing information such as:
	// <input type="checkbox" name="product" value="Bread">
	// <label for="Bread">Bread/label><br>
		
	for (i = 0; i < optionArray.length; i++) {
			
		var productName = optionArray[i].name;
		var productPrice = optionArray[i].price;
		// create the checkbox and add in HTML DOM
		var checkbox = document.createElement("input");
		checkbox.type = "checkbox";
		checkbox.name = "product";
		checkbox.value = productName;
		s6.appendChild(checkbox);
		
		// create a label for the checkbox, and also add in HTML DOM
		var label = document.createElement('label')
		label.htmlFor = productName;
		label.appendChild(document.createTextNode(productName));
		label.appendChild(document.createTextNode(" ($"+productPrice+")"));
		s6.appendChild(label);
		
		// create a breakline node and add in HTML DOM
		s6.appendChild(document.createElement("br"));    
	}
}
	
// This function is called when the "Add selected items to cart" button in clicked
// The purpose is to build the HTML to be displayed (a Paragraph) 
// We build a paragraph to contain the list of selected items, and the total price

function selectedItems(){
	
	var ele = document.getElementsByName("product");
	var chosenProducts = [];
	
	var c = document.getElementById('displayCart');
	c.innerHTML = "";
	
	// build list of selected item
	var para = document.createElement("P");
	para.innerHTML = "<h2>You selected: </h2>";
	var item_number = 1;
	for (i = 0; i < ele.length; i++) { 
		if (ele[i].checked) {
			para.appendChild(document.createTextNode("- " + ele[i].value));
			para.appendChild(document.createElement("br"));
			chosenProducts.push(ele[i].value);
			item_number++;
		}
	}
		
	// add paragraph and total price
	c.appendChild(para);
	var price = document.getElementById('totalPrice');
	price.innerHTML = null;
	price.appendChild(document.createTextNode("Total Price is $" + getTotalPrice(chosenProducts)));
	price.appendChild(document.createElement("br"));
	price.appendChild(document.createTextNode("If Delivered $" + (getTotalPrice(chosenProducts)*1.10).toFixed(2)));
}