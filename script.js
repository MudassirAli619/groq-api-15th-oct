// This function gets our data, like going to the store to get some candy.
async function fetchData() {
    // Here we go to our backend URL to get the info.
    let response = await fetch('http://localhost:5000/data');
    // We unwrap the data, like unwrapping candy.
    let data = await response.json();
    // This shows our info on the page.
    document.getElementById('output').innerText = data.info;
}

// This calls our function when the page loads.
window.onload = fetchData;
