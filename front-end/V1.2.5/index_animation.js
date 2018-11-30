$("#main_text").click(function (event) {

    // get size of element and divide bitmap size on it
    var rect = this.getBoundingClientRect();
    var scaleX = this.width  / rect.width;
    var scaleY = this.height / rect.height;

    // scale position: (first adjust, then scale)
    var mouseX = Math.round((event.clientX - rect.left) * scaleX);
    var mouseY = Math.round((event.clientY - rect.top ) * scaleY);

    var x = 250;
    var y = 150;
    var w = 50;
    var h = 50;

    if (mouseX >= x && mouseX <= x + w && mouseY >= y && mouseY <= y + h) {
        alert("You clicked on image");
    }
}
