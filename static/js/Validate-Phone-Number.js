function ValidatePhoneNumber() {
    var num = document.getElementById("PhoneNumber");
    num.value = num.value.replace(/[^0-9]/g, ""); // Remove non-numeric characters
  
    if (num.value.length > 10) {
      // If more than 10 digits, truncate the num
      num.value = num.value.slice(0, 10);
    }
  
    if (num.value.length === 10) {
      const PhoneNumber = num.value;
      console.log(PhoneNumber);
    }
  }
  