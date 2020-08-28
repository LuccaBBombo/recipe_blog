function sendMail(contactForm) {
    emailjs.send("lucca", "recipe_blog", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "recipe_blog_content": contactForm.recipeblogcontent.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // Blocks from loading a new page
}