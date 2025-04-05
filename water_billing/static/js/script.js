document.addEventListener("DOMContentLoaded", function () {
    const profileForm = document.getElementById("profileForm");

    if (profileForm) {
        profileForm.addEventListener("submit", function (event) {
            event.preventDefault();
            let formData = new FormData(profileForm);

            fetch("", {
                method: "POST",
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        document.getElementById("message").style.display = "block";
                        setTimeout(() => {
                            document.getElementById("message").style.display = "none";
                        }, 3000);
                    }
                })
                .catch((error) => console.error("Error:", error));
        });
    }
});
