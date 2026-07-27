// Restaurant Location Elements
const VerifyBtn = document.getElementById("verify-btn");
const AddressInput = document.getElementById("restaurant_address");
const MapDisplay = document.getElementById("map-display");

// Listen for button click to verify address
VerifyBtn.addEventListener("click", verifyAddress);

function verifyAddress() {
    const address = AddressInput.value.trim();

    if (address == "") {
        alert("Please enter an address.");
        return;
    }

    // Test verification
    MapDisplay.innerHTML = `<p>Verifying: ${address}</p>`;

    // Encode verified address
    const EncodedAddress = encodeURIComponent(address);

    // Display address using Google Maps
    MapDisplay.innerHTML = `
    <iframe
        width="100%"
        height="300"
        style="border:0;"
        loading="lazy"
        src="https://www.google.com/maps?q=${EncodedAddress}&output=embed">
    </iframe>
    `;
}
    