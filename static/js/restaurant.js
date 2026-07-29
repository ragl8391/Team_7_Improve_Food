// Restaurant Location Elements
const button = document.getElementById("share-location");
const status = document.getElementById("status");

// Listen for button click to verify address
button.addEventListener("click", () => {
    if (!navigator.geolocation) {
        status.textContent= "Geolocation not operating properly. Please try a different browser.";
        return;
    }

    status.textContent = "Retrieving location";

    navigator.geolocation.getCurrentPosition(
        // Find location
        async (position) => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            status.textContent = "Location confirmed!"

            // Send location to backend
            const response = await fetch ("/location", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    latitude,
                    longitude
                })
            });

            const result = await response.json();
            console.log(result);
        },
        (error) => {
            status.textContent = "Cannot retrieve location.";
            console.error(error);
        }
    );
});
                
    