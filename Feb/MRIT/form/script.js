function validateForm() {
let isValid = true;

// Get input values
let name = document.getElementById("name").value.trim();
let email = document.getElementById("email").value.trim();
let password = document.getElementById("password").value;
let confirmPassword = document.getElementById("confirmPassword").value;

// Clear previous errors
document.getElementById("nameError").innerText = "";
document.getElementById("emailError").innerText = "";
document.getElementById("passwordError").innerText = "";
document.getElementById("confirmPasswordError").innerText = "";

// Name validation
if (name === "") {
    document.getElementById("nameError").innerText = "Name is required";
    isValid = false;
}

// Email validation (simple regex)
let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
if (!emailPattern.test(email)) {
    document.getElementById("emailError").innerText = "Enter a valid email";
    isValid = false;
}

// Password validation (minimum 6 characters)
if (password.length < 6) {
    document.getElementById("passwordError").innerText = "Password must be at least 6 characters";
    isValid = false;
}

// Confirm Password validation
if (password !== confirmPassword) {
    document.getElementById("confirmPasswordError").innerText = "Passwords do not match";
    isValid = false;
}

return isValid; // Prevent form submission if validation fails
}