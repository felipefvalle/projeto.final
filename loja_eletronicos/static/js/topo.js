const btnTopo = document.getElementById("btnTopo");
window.onscroll = function() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        btnTopo.style.display = "block";
    } else {
        btnTopo.style.display = "none";
    }
};
function topFunction() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}
