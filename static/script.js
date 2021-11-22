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
        }, 3000);
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
  var API_KEY = "AIzaSyCfB-d8Dz5-0eAWuJ-KcQ21waiylx38KzY";
  var video = "";
  var counter = 0;

  $("#yt_form").submit(function (event) {
    event.preventDefault();
    video = "";

    // $("#search").val() = $("result").val();

    var search = $(".final").text();

    videoSearch(API_KEY, search, 1);
  });

  function videoSearch(key, search, maxResults) {
    counter++;
    if (counter > 1) return;
    $.get(
      "https://www.googleapis.com/youtube/v3/search?key=" +
        API_KEY +
        "&type=video&part=snippet&maxResults=" +
        maxResults +
        "&q=" +
        search,
      function (data) {
        console.log(data);
        console.log("LENGTH: ", data.items.length);

        data.items.forEach((item) => {
          video = ` <iframe class="yt_iframe" height="450" src="http://www.youtube.com/embed/${item.id.videoId}?autoplay=1&cc_load_policy=1" allow="autoplay" frameborder="0" allowfullscreen></iframe> `;
          const videodiv = document.createElement("div");
          videodiv.classList.add("yt_videos");
          videodiv.innerHTML = video;

          $("#videos").append(videodiv);
          setTimeout(function () {
            $(".yt_iframe").click();
          }, 5000);
        });
      }
    );
  }
});
