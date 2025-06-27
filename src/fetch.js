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
        
        const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${wsProtocol}//${window.location.host}/ws/downloads/${data.id}`;
        var ws = new WebSocket(wsUrl);
        
        ws.onopen = () => {
          ws.send(formData.get("url"));
        };
        ws.onmessage = function (event) {
          try {
            value = JSON.parse(event.data);
            status.innerHTML += `<br>${value.message}`;

            status.scrollTop = status.scrollHeight;
            window.location.href = value.url;
            form.reset();
          } catch (e) {
            status.innerHTML += `<br>${event.data}`;

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
