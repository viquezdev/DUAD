

let objects = [];
let currentPage = 1;
const itemsPerPage = 5;


async function fetchObjects() {
  try {
    const response = await axios.get("https://api.restful-api.dev/objects");

    const data = await response.data;

    objects = data.filter((obj) => obj.data);

    renderPage();
  } catch (error) {
    console.log("Error fetching objects");
  }
}


function renderPage() {
  const container = document.getElementById("list-container");
  container.innerHTML = "";

  const start = (currentPage - 1) * itemsPerPage;
  const end = start + itemsPerPage;

  const pageItems = objects.slice(start, end);

  pageItems.forEach((obj) => {
    const item = document.createElement("p");

    const details = Object.entries(obj.data)
      .map(([key, value]) => `${key}: ${value}`)
      .join(", ");

    item.innerHTML = `${obj.name} (${details})`;

    container.appendChild(item);
  });
}


document.getElementById("next").addEventListener("click", () => {
    const totalPages = Math.ceil(objects.length / itemsPerPage);

    if (currentPage < totalPages) {
        currentPage++;
        renderPage();
    }
});

document.getElementById("prev").addEventListener("click", () => {
    if (currentPage > 1) {
        currentPage--;
        renderPage();
    }
});

fetchObjects();