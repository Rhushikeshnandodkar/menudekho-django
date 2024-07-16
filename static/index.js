const ocbtn = document.querySelector(".ocbtn");
const links = document.querySelector(".links");
const maincontent = document.querySelector(".maincontent");

ocbtn.addEventListener('click', function(){
    ocbtn.classList.toggle("active");
    links.classList.toggle("active");
    maincontent.classList.toggle("active");
})

// const navli = document.querySelectorAll(".navli");
// navli.forEach(function(){
//     navli.addEventListener('click', function(){
    
//     ocbtn.classList.remove("active");
// })
// })


document.querySelectorAll(".navli").forEach(n => n.addEventListener("click", function(){
    ocbtn.classList.remove("active")
    links.classList.remove("active")
}))

function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");
  
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }