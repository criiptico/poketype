var pokemon1 = document.getElementById("pokemon1");
var printButton = document.getElementById("printBtn");
var printValue = document.getElementById("enteredPokemon");
function printEnteredValue() {
    printValue.textContent = pokemon1.value.toString();
    // printValue.textContent = pokemon1;
}
printButton.addEventListener("click", printEnteredValue);
