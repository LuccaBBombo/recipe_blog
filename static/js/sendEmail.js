function sendMail(contactForm) {
    emailjs.send("l", "rrecipe_blog", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "recipe_blog": contactForm.recipeblogconten.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}