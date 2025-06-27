document.addEventListener("DOMContentLoaded", (event) => {
  const form = document.getElementById("urlForm");
  const status = document.getElementById("status");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    status.textContent = "spotGrab: Download started";
    fetch("api/download", {
      method: "GET",
    })
      .then(async (response) => {
        test = await response.json();
        console.log(test);
        if (!response.ok) {
          const errorData = await response.json().catch(() => null);
          throw new Error(
            errorData?.detail || `Server error: ${response.status}`
          );
        }

        return test;
      })
      .then((data) => {
        var ws = new WebSocket("ws://localhost:8000/ws/downloads/" + data.id);
        ws.onopen = () => {
          ws.send(formData.get("url"));
        };
        ws.onmessage = function (event) {
          try {
            value = JSON.parse(event.data);
            status.innerHTML += `<br>${value.message}`;
            // Auto-scroll to bottom
            status.scrollTop = status.scrollHeight;
            window.location.href = value.url;
            form.reset();
          } catch (e) {
            status.innerHTML += `<br>${event.data}`;
            // Auto-scroll to bottom
            status.scrollTop = status.scrollHeight;
          }
        };
      })
      .catch((error) => {
        console.error("Error:", error);
        status.textContent = "spotGrab: An error occurred. Please try again.";
      });
  });
});
