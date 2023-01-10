const siteUrl  = "//127.0.0.1:8000/";
const styleUrl = siteUrl + "static/css/bookmark.css";
const minHeight = 250;
const minWidth = 250;


//Load css
var head = document.getElementsByTagName("head")[0];

var link = document.createElement("link");
link.rel = "stylesheet";
link.type = "text/css";
link.href = styleUrl+ "?r=" + Math.floor(Math.random()*9999999999999999);

head.appendChild(link);

//Load html
var body = document.getElementsByTagName("body")[0];

boxHtml = `
        <div class="bookmarklet">
        <a href="#" id="close">&times;</a>
        <h1>Select an image to bookmark:</h1>
        <div class="images" ></div>
        </div>
`;

body.innerHTML += boxHtml;


//Load function
function bookmarkletLaunch (){
    
    var bookmarklet = document.getElementById('bookmark');
    var imagesFound = bookmarklet.querySelector('.images');

    //clear images found
    imagesFound.innerHTML = '';

    //display bookmark
    bookmarklet.style.display = 'block';

    //Close event
    bookmarklet.querySelector('close').addEventListener('click', function(){
        bookmarklet.style.display = 'none';
    })


    //Find images
    var images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"');

    images.forEach(image => {
        if(image.naturalWidth >= minWidth && image.naturalHeight >= minHeight){
            var imageFound = document.createElement("img");
            imageFound.src = image.src;
            imagesFound.append(imageFound);

        }
    })

}

//Launch the bokmarklet
bookmarkletLaunch();

