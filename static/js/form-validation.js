document.addEventListener("DOMContentLoaded", function () {

    const forms = document.querySelectorAll("form");

    forms.forEach(form => {

        form.addEventListener("submit", function (e) {

            const invalidField = form.querySelector(":invalid");

            if (invalidField) {

                e.preventDefault();

                invalidField.scrollIntoView({
                    behavior: "smooth",
                    block: "center"
                });

                invalidField.focus();

                invalidField.style.borderColor = "red";
                invalidField.style.borderWidth = "2px";

                form.reportValidity();

                alert("Please fill all required fields.");

            }

        });

    });

});