function ValidatePassword() {
  const Pass1 = document.getElementById("Pass1").value;
  const Pass2 = document.getElementById("Pass2").value;

  if (Pass1 == Pass2) {
    console.log("Match");
  } else {
    console.log("Dont_Match");
  }
}
