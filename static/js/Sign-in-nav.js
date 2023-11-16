

// // addEventListener waits for loading the content to html dom and execute the anonymous function.
// document.addEventListener("DOMContentLoaded", function () {
//   // selects all elements with the id "submit
//   const s = document.querySelectorAll("#submit");
//   // console.log("c", s[0]);

//   // addEventListener listen for the click event on the node or that HTML element
//   s[0].addEventListener("click", () => {
//     // this code effectively instructs the browser to navigate to the root path of the website (the base URL).
//     window.location.href = "/";
//   });

//   const login = document.querySelectorAll("#login");
//   console.log(login[0]);

  
// });


function validateForm() {
    const inputValue1 = document.querySelectorAll("#myInput1")[0].value;
    const inputValue2 = document.querySelectorAll("#myInput2")[0].value;

    // If everything is okay, return true; otherwise, return false;
    if (inputValue1 && inputValue1) {
        console.log(inputValue1)
        console.log(inputValue2)
        return true;  // Form submission will proceed
        
    } else {
        return false;  // Form submission will be canceled
    }
}