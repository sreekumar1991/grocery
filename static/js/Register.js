// addEventListener waits for loading the content to html dom and execute the anonymous function.
document.addEventListener("DOMContentLoaded", function () {
  const register = document.querySelectorAll("#Register");
  console.log(register[0]);

  register[0].addEventListener("click", () => {
    window.location.href = "/register/";
  });
});

function validateCreditCardInput() {
  var input = document.getElementById("creditCardNumber");
  input.value = input.value.replace(/[^0-9]/g, ""); // Remove non-numeric characters

  if (input.value.length > 16) {
    // If more than 16 digits, truncate the input
    input.value = input.value.slice(0, 16);
  }

  if (input.value.length === 16) {
    const Credit_card_num = input.value;
    console.log(Credit_card_num);
  }
}
