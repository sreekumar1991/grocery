// addEventListener waits for loading the content to html dom and execute the anonymous function.
document.addEventListener("DOMContentLoaded", function () {
  const registerButton = document.querySelectorAll("#Register");
  // console.log(registerButton[0]);

    registerButton[0].addEventListener("click",() => {
      window.location.href = "/register/";
    });

});
