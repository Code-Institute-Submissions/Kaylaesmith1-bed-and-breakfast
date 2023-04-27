function sendMail(contactForm) {
    emailjs.send("service_6a8xgnp", "template_ub9mghj", {
        "from_fname": contactForm.firstname.value,
        "from_lname": contactForm.lastname.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    });
    return false;
}


function popup() {
    var fname = document.getElementById('firstname');
    var lname = document.getElementById('lastname');
    var email = document.getElementById('emailaddress');
    var message = document.getElementById('message');
    const success = document.getElementById('success');
    const danger = document.getElementById('danger');

    if (fname.value === '' || lname.value === '' || email.value === '' || message.value === '') {
        danger.style.display = 'block';
    } else {
        setTimeout(() => {
            fname.value = '';
            lname.value = '';
            email.value = '';
            message.value = '';
        }, 3000);

        success.style.display = 'block';
    }


    setTimeout(() => {
        danger.style.display = 'none';
        success.style.display = 'none';
    }, 3000);

}
