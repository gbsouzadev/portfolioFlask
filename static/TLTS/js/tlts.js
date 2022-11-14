const year = document.getElementById("year")
const thisYear = new Date().getFullYear()
year.setAttribute("datetime", thisYear)
year.textContent = thisYear

function formBehavior(){
    document.getElementById('contactForm').style.display = 'none';
    document.getElementById('contactH2').innerHTML = 'Your message has been successfully sent!';
}