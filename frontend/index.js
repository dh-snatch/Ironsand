document.addEventListener('DOMContentLoaded', () => {

    fetch('endpoint.php').then(response => response.json()).then(deposits => {

    // For reference: https://leafletjs.com/examples/quick-start/


    // New Zealand bounds
    const nzBounds = [
        [-56, 170],  
        [-30, 179]   
    ];

    // TODO: needs better adjustment, a bit finicky
    const map = L.map('map', {
        maxBounds: nzBounds,
        maxBoundsViscosity: 1.0, // prevents panning outside New Zealand
        minZoom: 5.2, 
        maxZoom: 15
    }).setView([-43, 172], 5); 

    // OSM Tile usage requirements: https://operations.osmfoundation.org/policies/tiles/
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
    }).addTo(map);


    // the sidebar list in index.php
    const sidebarList = document.getElementById('sidebar').querySelector('ul');

    // for each item in json data from PHP
    deposits.forEach(deposit => {
        // Add a marker to the map
        const marker = L.marker([deposit.latitude, deposit.longitude]).bindPopup(`
            <p>Name: ${deposit.name}</p>
            <p>Latitude: ${deposit.latitude}</p>
            <p>Longitude: ${deposit.longitude}</p>
            <p>Rock Type: ${deposit.rock_type}</p>
        `).addTo(map);

        // Create a list element
        const li = document.createElement('li');

        // Make the name clickable, and add a sublist for details
        li.innerHTML = `
        <span class="clickable-name">${deposit.name}</span>
        <ul>
            <li>Latitude: ${deposit.latitude}</li>
            <li>Longitude: ${deposit.longitude}</li>
            <li>Rock Type: ${deposit.rock_type}</li>
        </ul>
        `;

        // When the name is clicked, set the map view to the marker and open the popup
        li.querySelector(".clickable-name").addEventListener('click', () => {
            map.setView([deposit.latitude, deposit.longitude], 10);
            marker.openPopup();
        });
        // Add the list item to the sidebar
        sidebarList.appendChild(li);
    });

    }).catch(error => {
        console.error('Error fetching deposits:', error);
    }
    );
});
