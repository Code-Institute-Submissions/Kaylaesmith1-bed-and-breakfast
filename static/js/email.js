function sendMail(contactForm) {
    emailjs.send("service_6a8xgnp", "template_ub9mghj", {
            "from_fname": contactForm.firstname.value,
            "from_lname": contactForm.lastname.value,
            "from_email": contactForm.emailaddress.value,
            "message": contactForm.message.value
        })
        .then(
            function (response) {
                console.log("Email successfully sent", response);
            },
            function (error) {
                console.log("Email failed to send", error);
            }
            
        );
    return false;
}
