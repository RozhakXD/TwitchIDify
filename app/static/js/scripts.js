function showNotification(message, isSuccess = true) {
    const notification = document.getElementById("notification");
    notification.textContent = message;
    notification.style.backgroundColor = isSuccess ? "#28a745" : "#d9534f";
    notification.classList.add("show");

    setTimeout(() => {
        notification.classList.remove("show");
    }, 5000);
}

function getTwitchID() {
    const username = document.getElementById("username").value.trim();
    const result = document.getElementById("result");
    const userID = document.getElementById("userID");
    const followers = document.getElementById("followers");

    result.style.display = "none";

    if (!username) {
        showNotification("Username tidak boleh kosong!", false);
        return;
    }

    fetch(`/api/twitch/${username}`)
        .then(response => response.json())
        .then(data => {
            if (data.user) {
                const followersFormatted = new Intl.NumberFormat("id-ID").format(data.user.followers);
                showNotification("Pengguna ditemukan!", true);
                userID.textContent = `ID Pengguna: ${data.user.id}`;
                followers.textContent = `Pengikut: ${followersFormatted}`;
                result.style.display = "block";
            } else {
                showNotification("Pengguna tidak ditemukan!", false);
            }
        })
        .catch(error => {
            showNotification("Terjadi kesalahan saat mengambil data!", false);
        });
}