

// addEventListener waits for loading the content to html dom and execute the anonymous function.
document.addEventListener("DOMContentLoaded", function () {
  const login = document.querySelectorAll("#login");
  console.log(login[0]);

  login[0].addEventListener("click",() => {
    window.location.href = "/sign-in/";
  });
});
