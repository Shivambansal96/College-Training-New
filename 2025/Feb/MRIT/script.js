const output = document.getElementById("output");
const plus = document.getElementById("plus");
const minus = document.getElementById("minus");
const reset = document.getElementById("reset");

let count = 0;

function add() {
    count++;
    output.innerText = count;
    plus.style.backgroundColor = "red";
}

plus.addEventListener("click", add);

function resetFn() {
    
    let confirmation = confirm("Do you want to start the count again?");
    
    if(confirmation) {
        count = 0;
        output.innerText = count;
    }

    else {
        alert("Reset cancelled!");
    }

}

reset.addEventListener("click", resetFn);