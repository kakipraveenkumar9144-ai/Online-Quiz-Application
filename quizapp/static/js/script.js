const btn = document.getElementById("animateBtn");
const rightBox = document.querySelector(".right-box");

btn.addEventListener("click", () => {
  rightBox.style.transform = "scale(1.05)";

  setTimeout(() => {
    rightBox.style.transform = "scale(1)";
  }, 500);
});
