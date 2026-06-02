function nextSection() {

    document.getElementById("section1").classList.remove("active-section");

    document.getElementById("section1").classList.add("hidden-section");

    document.getElementById("section2").classList.remove("hidden-section");

    document.getElementById("section2").classList.add("active-section");

}

function previousSection() {

    document.getElementById("section2").classList.remove("active-section");

    document.getElementById("section2").classList.add("hidden-section");

    document.getElementById("section1").classList.remove("hidden-section");

    document.getElementById("section1").classList.add("active-section");

}

function goToSection3(){

    document.getElementById("section2").classList.remove("active-section");

    document.getElementById("section2").classList.add("hidden-section");

    document.getElementById("section3").classList.remove("hidden-section");

    document.getElementById("section3").classList.add("active-section");

}

function backToSection2(){

    document.getElementById("section3").classList.remove("active-section");

    document.getElementById("section3").classList.add("hidden-section");

    document.getElementById("section2").classList.remove("hidden-section");

    document.getElementById("section2").classList.add("active-section");

}
function goToSection4(){

    document.getElementById("section3").classList.remove("active-section");

    document.getElementById("section3").classList.add("hidden-section");

    document.getElementById("section4").classList.remove("hidden-section");

    document.getElementById("section4").classList.add("active-section");

}

function backToSection3(){

    document.getElementById("section4").classList.remove("active-section");

    document.getElementById("section4").classList.add("hidden-section");

    document.getElementById("section3").classList.remove("hidden-section");

    document.getElementById("section3").classList.add("active-section");

}
function goToSection5(){

    document.getElementById("section4").classList.remove("active-section");

    document.getElementById("section4").classList.add("hidden-section");

    document.getElementById("section5").classList.remove("hidden-section");

    document.getElementById("section5").classList.add("active-section");

}

function backToSection4(){

    document.getElementById("section5").classList.remove("active-section");

    document.getElementById("section5").classList.add("hidden-section");

    document.getElementById("section4").classList.remove("hidden-section");

    document.getElementById("section4").classList.add("active-section");

}