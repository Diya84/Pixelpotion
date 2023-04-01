if (api === "") {
  alert("Please enter your OpenAI API key");
}

const url = "https://api.openai.com/v1/images/generations";
const text = document.getElementById("text");
const image = document.getElementById("image");
const btn = document.getElementById("btn");

function generateImage() {
  if (text.value === "") {
    alert("Please enter a description or keyword");
  } else {
    const data = {
      prompt: text.value,
      n: 2,
      size: "1024x1024",
    };
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${api}`,
      },
      body: JSON.stringify(data),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        const arraySize = data.data.length;
        for (let i = 0; i < arraySize; i++) {
          image.innerHTML += `<img src="${data.data[i].url}" alt="Generated image ${i+1}" class="w-full p-2">`;
        }
      });
  }
}

// Add event listener to input field to change button style
text.addEventListener("input", function () {
  if (text.value === "") {
    btn.classList.remove("bg-slate-900", "text-slate-50");
    text.classList.add("border-r-2", "border-gray-200");
  } else {
    text.classList.remove("border-r-2", "border-gray-200");
    btn.classList.add("bg-slate-900", "text-slate-50");
  }
});
