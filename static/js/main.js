// Get the alert element
var alert = document.getElementById("alert");

// Set a timeout to remove the alert after 3 seconds

if (alert) {
    setTimeout(function () {
        alert.style.display = "none";
    }, 2000);
}