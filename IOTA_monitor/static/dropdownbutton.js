console.log("this is dropdownbuttonjs speaking: ");

var dropdown = document.getElementsByClassName("analytics_link");
console.log(dropdown);
var i;
console.log("---------------");
console.log(window.screen.availWidth);

function show_hide_dropdown() {
    console.log('triggered');
    var dropdownContent = document.getElementsByClassName("dropdown-container");
    console.log(dropdownContent);
    var dropdown = document.getElementsByClassName("analytics_link");
    if(dropdownContent[0].style.display == 'block'){
        dropdownContent[0].style.display = 'none';
    }
    else{
        dropdownContent[0].style.display = 'block';
    }


        }

for (i = 0; i < dropdown.length; i++) {
    console.log(i);
    dropdown[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var dropdownContent = document.getElementsByClassName("dropdown-container");
        console.log(dropdownContent);
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
    });
}