function sendMail(contactForm) {
    emailjs.send("lucca", "recipe_blog", {
        "recipe_blog_content": contactForm.recipeblogcontent.value,
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
    })
    .then(
        function(response) {
            alert("Your email has been sent!", response);
        },
        function(error) {
            alert("Email has not been sent!", error);
        }
    );
    return false;  // Blocks from loading a new page
}