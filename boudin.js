document.getElementById("frere").addEventListener("click", () => {

    const image = document.getElementById("boudin");
    image.style.transition = "width 1s ease-out, height 1s ease-out";
    image.style.width = "1000px";
    image.style.height = "500px";
    
    setTimeout(() => {
        image.style.transition = "width 1s ease-out, height 1s ease-out,transform 1s ease-out";
        image.style.width = "1500px"; 
        image.style.height = "500px"; 
        image.style.transform = "rotate(180deg)";
    }, 2000);
    
    setTimeout(() => {
        image.style.transition = "width 1s ease-out, height 1s ease-out,transform 1s ease-out";
        image.style.width = "500px"; 
        image.style.height = "150px"; 
        image.style.transform = "rotate(0deg)";
    }, 5000);
    
});