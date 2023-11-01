var myHeading = document.querySelector("h1");
myHeading.textContent = "SUS!";

function handleTerminalChange() {
    const selectElement = document.getElementById('terminals');
    const selectedTerminnal = selectElement.value;
    alert('Вы выбрали: ' + selectedTerminnal);
}