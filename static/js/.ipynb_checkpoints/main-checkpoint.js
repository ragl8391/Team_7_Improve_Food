let selectedFulfillment = 'pickup';

function selectFulfillment(type) {
    selectedFulfillment = type;
    document.getElementById('fulfillment_type').value = type;

    document.getElementById('pickup-btn').classList.toggle('active', type === 'pickup');
    document.getElementById('delivery-btn').classList.toggle('active', type === 'delivery');

    if (type === 'delivery') {
        openAddressModal();
    }
}

function openAddressModal() {
    document.getElementById('address-modal').classList.remove('hidden');
}

function closeAddressModal() {
    document.getElementById('address-modal').classList.add('hidden');
    // If they cancel, fall back to pickup
    selectFulfillment('pickup');
}

async function checkRadius() {
    const address = document.getElementById('address-input').value.trim();
    const messageEl = document.getElementById('radius-message');

    if (!address) {
        messageEl.textContent = 'Please enter an address.';
        messageEl.className = 'radius-message blocked';
        return;
    }

    try {
        const response = await fetch('/check-radius', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ address: address })
        });
        const data = await response.json();

        if (data.allowed) {
            messageEl.textContent = 'Delivery available to this address.';
            messageEl.className = 'radius-message allowed';
            document.getElementById('address_hidden').value = address;
            setTimeout(closeAddressModalSuccess, 800);
        } else {
            messageEl.textContent = 'Sorry, this address is outside our 5-mile delivery range. Please choose pickup instead.';
            messageEl.className = 'radius-message blocked';
        }
    } catch (err) {
        messageEl.textContent = 'Could not verify address. Please try again.';
        messageEl.className = 'radius-message blocked';
    }
}

function closeAddressModalSuccess() {
    document.getElementById('address-modal').classList.add('hidden');
}