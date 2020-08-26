emailjs.sendForm("l", "recipe_blog", "contact_form")
    .then(function(response) {
       console.log("SUCCESS!", response.status, response.text);
    }, function(error) {
       console.log("FAILED...", error);
    });
