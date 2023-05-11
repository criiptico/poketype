const pokemon1 = document.getElementById("pokemon1") as HTMLInputElement
const printButton = document.getElementById("printBtn") as HTMLButtonElement
const printValue = document.getElementById("enteredPokemon") as HTMLOutputElement

function printEnteredValue(): void{
    printValue.textContent = pokemon1.value.toString();
    // printValue.textContent = pokemon1;
}

printButton.addEventListener("click", printEnteredValue);