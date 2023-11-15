


// addEventListener waits for loading the content to html dom and execute the anonymous function.
document.addEventListener("DOMContentLoaded", function () {
  // selects all elements with the id "submit
  const s = document.querySelectorAll("#submit");
  // console.log("c", s[0]);

  // addEventListener listen for the click event on the node or that HTML element
  s[0].addEventListener("click", () => {
    // this code effectively instructs the browser to navigate to the root path of the website (the base URL).
    window.location.href = "/";
  });

  const login = document.querySelectorAll("#login");
  console.log(login[0]);
});
