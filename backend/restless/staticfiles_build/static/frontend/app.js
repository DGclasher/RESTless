const navLinks = document.querySelector(".nav-links");
const ham = document.getElementById("ham")

function onToggleMenu(e) {
  e.name = e.name === "menu" ? "close" : "menu";
  navLinks.classList.toggle("top-[9%]");
}

ham.onclick = onToggleMenu(ham)
