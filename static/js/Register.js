



// addEventListener waits for loading the content to html dom and execute the anonymous function.
document.addEventListener("DOMContentLoaded", function () {
    const register = document.querySelectorAll("#Register");
    console.log(register[0]);
  
    register[0].addEventListener("click", () => {
      window.location.href = "/register/";
    });
  });
  