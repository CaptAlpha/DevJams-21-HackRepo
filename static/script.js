window.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("button_4");
  const result = document.getElementById("result");
  const main = document.getElementsByTagName("main")[0];
  let listening = false;
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;
  if (typeof SpeechRecognition !== "undefined") {
    const recognition = new SpeechRecognition();

    const stop = () => {
      main.classList.remove("speaking");
      recognition.stop();
      button.textContent = "Start listening";
    };

    const start = () => {
      main.classList.add("speaking");
      recognition.start();
      button.textContent = "Stop listening";
    };

    const onResult = (event) => {
      result.innerHTML = "";
      for (const res of event.results) {
        const text = document.createTextNode(res[0].transcript);
        const p = document.createElement("p");
        if (res.isFinal) {
          p.classList.add("final");
          stop();
          listening = !listening;
        }
        p.appendChild(text);
        result.appendChild(p);

        setTimeout(function () {
          document.getElementById("yt_submit").click();
        }, 5000);
      }
    };
    recognition.interimResults = true;
    recognition.continuous = true;
    recognition.addEventListener("result", onResult);
    button.addEventListener("click", (event) => {
      listening ? stop() : start();
      listening = !listening;
    });
  } else {
    button.remove();
    const message = document.getElementById("message");
    message.removeAttribute("hidden");
    message.setAttribute("aria-hidden", "false");
  }
});

$(document).ready(function () {
  var API_KEY = "AIzaSyBhPae4rr9_wih418gaj5HK0K9wLXz3Zx4";
  var video = "";

  $("#yt_form").submit(function (event) {
    event.preventDefault();

    // $("#search").val() = $("result").val();

    var search = $(".final").text();

    videoSearch(API_KEY, search, 10);
  });

  function videoSearch(key, search, maxResults) {
    $.get(
      "https://www.googleapis.com/youtube/v3/search?key=" +
        API_KEY +
        "&type=video&part=snippet&maxResults=" +
        maxResults +
        "&q=" +
        search,
      function (data) {
        console.log(data);

        data.items.forEach((item) => {
          video = ` <iframe width="420" height="315" src="http://www.youtube.com/embed/${item.id.videoId}" frameborder="0" allowfullscreen></iframe> `;

          $("#videos").append(video);
        });
      }
    );
  }
});
